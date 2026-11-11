import hashlib
from collections import Counter

def schema_state(onto):
    classes = {c.get('id') for c in onto.get('classes', [])}
    relations = {r.get('id') for r in onto.get('relations', [])}
    props = {p.get('id') for p in onto.get('properties', [])}
    abox = Counter(r.get('relation') for r in onto.get('relation_instances', []))
    facts = set()
    fact_evidence = {}
    for f in onto.get('relation_instances', []):
        fid = f"{f.get('relation')}|{f.get('subject')}|{f.get('object')}|{f.get('role','')}"
        facts.add(fid)
        fact_evidence[fid] = hashlib.sha256((f.get('evidence') or '').encode('utf-8')).hexdigest()[:8]
    return {'classes': classes, 'relations': relations, 'properties': props, 'abox': abox,
            'facts': facts, 'fact_evidence': fact_evidence, 'version': onto.get('version')}

ROLE_KEYS = ('研究站点', '观测来源', '背景提及', 'background_mention', 'research_site', 'observation_source', 'role=')
MODEL_ROLE_KEYS = ('实际采用', '仅提及', '对比基线', 'applied_model', 'mentioned_model')
RATIO_KEYS = ('比例', '平均', '每篇', '分母', '分母从', '率', '占比')

def has_any(text, keys):
    return any(k in text for k in keys)

def stage_a(task_input, evidence, state, flags=None, state_spec=None):
    """Deterministic Stage A. Uses only question, PopulationSpec and ontology state."""
    flags = flags or {}
    state_spec = state_spec or {}
    if not flags.get('schema_audit_enabled', True):
        return {'trigger_class': 'none', 'trigger_type': 'audit_disabled', 'schema_coverage': 0.0,
                'required_elements': [], 'tbox_present': [], 'abox_counts': {}, 'proposal': None,
                'candidate_rule': 'no audit', 'flags': flags}
    q = task_input.get('question', '') or ''
    spec = task_input.get('population_spec', {}) or {}
    blob = q + ' ' + str(spec)
    classes, relations, abox = state['classes'], state['relations'], state['abox']
    required = []
    tbox_present = []
    proposal = None
    result = {'trigger_class': 'none', 'trigger_type': 'none', 'schema_coverage': 1.0,
              'required_elements': [], 'tbox_present': [], 'abox_counts': {}, 'proposal': None,
              'candidate_rule': 'membership from evidence', 'flags': flags}

    # 1) proposal validity case
    if '提案' in q and any(k in q for k in ('父类', '定义域', '值域', '证据', '是否应批准')):
        result.update(trigger_class='ontology_upgrade', trigger_type='proposal_gap',
                      required_elements=['valid_proposal'], candidate_rule='reject invalid proposal')
        return result

    # 2) explicit intervention words in the question
    if any(k in q for k in ('遮蔽', '移除', '去掉', '没有')):
        if 'AlpineMeadow' in q or '高寒草甸' in q:
            target = 'AlpineMeadow'
            result.update(trigger_class='ontology_upgrade', trigger_type='class_missing',
                          required_elements=[target], candidate_rule='restore class before membership')
            return result
        if 'station_has_type' in q or '关系' in q:
            target = 'station_has_type'
            result.update(trigger_class='ontology_upgrade', trigger_type='relation_missing',
                          required_elements=[target], candidate_rule='restore relation before membership')
            return result
        if 'sameAs' in q or '去重' in q:
            result.update(trigger_class='ontology_upgrade', trigger_type='alias_gap',
                          required_elements=['sameAs'], candidate_rule='dedup aliases')
            return result
    if '清空' in q or '实例为空' in q or 'ABox' in q or '不遮蔽' in q:
        rel = 'uses_station' if '站点' in q or '研究站点' in q else 'station_has_type'
        result.update(trigger_class='abox_repair', trigger_type='abox_incomplete',
                      required_elements=[rel], abox_counts={rel: abox.get(rel, 0)},
                      candidate_rule='backfill ABox; do not add schema')
        return result

    # 3) role schema missing
    if has_any(blob, ROLE_KEYS) and 'hasStationRole' not in relations and 'hasStationRole' not in classes:
        result.update(trigger_class='ontology_upgrade', trigger_type='role_schema_missing',
                      required_elements=['hasStationRole'], candidate_rule='distinguish research/observation/background')
        return result
    if has_any(blob, MODEL_ROLE_KEYS) and 'hasModelRole' not in relations and 'hasModelRole' not in classes:
        result.update(trigger_class='ontology_upgrade', trigger_type='role_schema_missing',
                      required_elements=['hasModelRole'], candidate_rule='distinguish applied/mentioned/baseline')
        return result

    # 4) definition / subclass / alias
    if ('不大于' in q or '父子类' in q or '等价类' in q or '定义' in q) and 'AlpineMeadow' in str(spec):
        result.update(trigger_class='ontology_upgrade', trigger_type='definition_gap',
                      required_elements=['AlpineMeadow ⊑ Meadow'], candidate_rule='use subclass closure')
        return result
    if ('去重' in q or '别名' in q) and 'sameAs' not in relations:
        result.update(trigger_class='ontology_upgrade', trigger_type='alias_gap',
                      required_elements=['sameAs'], candidate_rule='dedup aliases')
        return result
    if ('提到' in q or '提及' in q) and 'mentions' not in relations:
        result.update(trigger_class='ontology_upgrade', trigger_type='relation_missing',
                      required_elements=['mentions'], candidate_rule='separate mention from report')
        return result

    # 5) denominator/unit belongs to PopulationSpec
    if has_any(q, RATIO_KEYS) or spec.get('unit_q') in ('ratio', 'per_paper'):
        result.update(trigger_class='spec_only', trigger_type='spec_only',
                      candidate_rule='write denominator/unit into PopulationSpec')
        return result

    # 6) fact-level ABox availability from the task's state spec.
    target_relations = list(state_spec.get('target_relations') or [])
    fact_ids = list(dict.fromkeys(state_spec.get('fact_ids') or []))
    if target_relations and fact_ids and state.get('facts') is not None:
        present_facts = set(state.get('facts') or [])
        missing_facts = [fid for fid in fact_ids if fid not in present_facts]
        ref_evidence = state_spec.get('evidence_hashes') or {}
        current_evidence = state.get('fact_evidence') or {}
        evidence_mismatch = [fid for fid in fact_ids
                             if fid in present_facts and ref_evidence.get(fid) and
                             current_evidence.get(fid) != ref_evidence.get(fid)]
        rels_present = all(rel in relations for rel in target_relations)
        if rels_present and (missing_facts or evidence_mismatch):
            result.update(trigger_class='abox_repair', trigger_type='abox_incomplete',
                          required_elements=target_relations,
                          tbox_present=[True for _ in target_relations],
                          abox_counts={rel: abox.get(rel, 0) for rel in target_relations},
                          fact_level={'missing_facts': missing_facts,
                                      'evidence_mismatch': evidence_mismatch,
                                      'target_fact_n': len(fact_ids)},
                          candidate_rule='fact-level ABox backfill')
            return result

    # 7) ABox empty for required relation
    for rel in ('uses_station', 'station_has_type', 'applies_model', 'reports_variable', 'supported_by'):
        if rel in blob or rel in str(spec):
            required.append(rel)
            tbox_present.append(rel in relations)
            if abox.get(rel, 0) == 0:
                result.update(trigger_class='abox_repair', trigger_type='abox_incomplete',
                              required_elements=required, tbox_present=tbox_present,
                              abox_counts={rel: 0}, candidate_rule='backfill ABox')
                return result

    result['required_elements'] = required
    result['tbox_present'] = tbox_present
    result['abox_counts'] = {k: abox.get(k, 0) for k in required}
    if required and all(tbox_present):
        result['schema_coverage'] = 1.0
    elif required:
        result['schema_coverage'] = sum(1 for x in tbox_present if x) / len(required)
    return result
