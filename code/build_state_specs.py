"""Build compact per-task state specs for TP-Bench.

Outputs:
  data/tiers/dataset_v4_state.jsonl
  data/tiers/state_ready_manifest.json
  data/STATE_SPEC_AUDIT.md

The builder is deterministic. It turns trigger annotations into a base
snapshot + mask + gold delta, and adds ABox-repair tasks whose references are
derived from committed ontology facts. Tasks whose target cannot be recovered
are marked explicitly.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from core_v3.state_builder import apply_state_spec, state_hash, state_stats

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
SRC = DATA / 'tiers' / 'dataset_v3_corrected.jsonl'
BASE_PATH = DATA / 'canonical' / 'ontology_v2_backfilled.json'
OUT = DATA / 'tiers' / 'dataset_v4_state.jsonl'
MANIFEST = DATA / 'tiers' / 'state_ready_manifest.json'
AUDIT = DATA / 'STATE_SPEC_AUDIT.md'

BASE = json.loads(BASE_PATH.read_text(encoding='utf-8'))
TASKS = [json.loads(line) for line in SRC.read_text(encoding='utf-8').splitlines() if line.strip()]
REL_IDS = {r.get('id') for r in BASE.get('relations', [])}
REL_META = {r.get('id'): r for r in BASE.get('relations', [])}
CLASSES = {c.get('id'): c for c in BASE.get('classes', [])}
CLASS_BY_LABEL = {c.get('label'): c for c in BASE.get('classes', []) if c.get('label')}
PROP_IDS = {p.get('id') for p in BASE.get('properties', [])}
INDIVIDUALS = {i.get('id'): i for i in BASE.get('individuals', [])}
STATION_IDS = {
    i.get('attributes', {}).get('name'): i.get('id')
    for i in BASE.get('individuals', [])
    if i.get('class') == 'EcologicalStation'
}


def _abox_station_facts():
    inds = {i.get('id'): i for i in BASE.get('individuals', [])}
    uses = defaultdict(lambda: defaultdict(list))
    model_docs = set()
    for f in BASE.get('relation_instances', []):
        if f.get('relation') == 'uses_station':
            name = (inds.get(f.get('object'), {}).get('attributes') or {}).get('name')
            doc = str(f.get('subject') or '').replace('Paper_', '')
            if name and doc:
                uses[name][doc].append(f.get('evidence') or '')
        elif f.get('relation') == 'applies_model':
            model_docs.add(str(f.get('subject') or '').replace('Paper_', ''))
    return uses, model_docs


def generate_abox_repair_tasks():
    """Create additional fact-backed ABox-repair tasks from committed ontology facts.

    The tasks use the negative-absence template, where the gold population is
    the set of papers using a station minus papers with an applied model.  The
    state spec clears both `applies_model` and `hasModelRole` facts, so repair is
    required before the target population can be instantiated.
    """
    from core_v3 import data_loader, object_inventory
    ann, _, _, _ = data_loader.load_resources()
    inv = object_inventory.build_inventory(ann)
    uses, model_docs = _abox_station_facts()
    existing = {t.get('id') for t in TASKS}
    existing_questions = {t.get('question_zh') or t.get('question') for t in TASKS}

    nonempty = ['海北', '内蒙古', '策勒', '临泽', '长武']
    empty = ['长白山', '禹城', '千烟洲', '西双版纳', '鼎湖山', '北京森林',
             '拉萨', '会同', '哀牢山', '安塞', '常熟', '神农架', '当雄',
             '帽儿山', '尖峰岭', '阜康', '栾城', '大兴', '秦岭', '那曲']
    templates = [
        '使用{name}且未报告任何模型的论文共有多少篇？',
        '使用{name}的论文中，没有报告任何模型的共有多少篇？',
        '在涉及{name}的论文里，没有报告模型的共有多少篇？',
        '使用{name}且未采用任何模型的论文数量是多少？',
        '使用{name}的论文中，未采用模型的论文数量是多少？',
    ]
    seen = set(existing_questions)

    def pick_pairs(names, limit):
        result = []
        for name in names:
            for template in templates:
                question = template.format(name=name)
                if name not in uses or name not in inv['stations'] or question in seen:
                    continue
                seen.add(question)
                result.append((name, question))
                if len(result) == limit:
                    return result
        return result

    selected = pick_pairs(nonempty, 12) + pick_pairs(empty, 12)

    out = []
    for idx, (name, question) in enumerate(selected, start=len(TASKS) + 1):
        doc_facts = uses[name]
        use_docs = sorted(doc_facts)
        gold_members = sorted(set(use_docs) - model_docs)
        source_docs = gold_members or use_docs
        evidence = []
        for d in source_docs:
            quotes = [q for q in doc_facts.get(d, []) if q]
            evidence.append({'doc_id': d, 'quote': quotes[0] if quotes else ''})
        task_id = f'TP{idx:04d}'
        if task_id in existing:
            task_id = f'ABX{idx:04d}'
        t = {
            'id': task_id,
            'legacy_id': None,
            'source_row': idx,
            'tier': 'B' if gold_members else 'C',
            'group': 'negative_absence',
            'question_zh': question,
            'question': question,
            'population_spec': {
                'U_q': 'paper',
                'C_q_pop': f'Paper ⊓ ∃uses_station.Station("{name}") ⊓ ¬∃applies_model.Model',
                'N_q': f'papers using {name} without an applied model',
                'D_q': f'papers using {name}',
                'role_q': 'study_or_observation',
                'gran_q': name,
                'unit_q': 'paper',
                'evidence_q': 'sentence+page',
                'schema_version': 'v2.1.461-backfilled',
            },
            'source_docs': source_docs,
            'evidence': evidence,
            'gold': {
                'answer': len(gold_members),
                'denominator': len(use_docs),
                'members': gold_members,
                'numerator': len(gold_members),
                'status': 'ontology_fact_backed',
            },
            'statistical_process': {
                'numerator_rule': f'papers using {name} with no applied model',
                'denominator_rule': f'papers using {name}',
                'unit': 'paper',
                'aggregation': 'set_difference',
                'answer': len(gold_members),
                'members': gold_members,
                'numerator': len(gold_members),
                'denominator': len(use_docs),
                'accounting': 'sum(members)=numerator; denominator declared',
            },
            'metrics': {'type': 'count', 'unit': 'paper'},
            'evaluation': {
                'answer': True,
                'members': True,
                'denominator_count': False,
                'reasons': [],
            },
            'ontology_editing': {
                'trigger_class': 'abox_repair',
                'trigger_type': 'abox_incomplete',
                'required_element': 'applies_model',
                'proposal': {},
                'approval_required': False,
                'schema_version': 'v2.1.460',
                'abox_change': 'backfill model links; absence rule in spec',
                'why': 'applies_model and hasModelRole facts are cleared in the pre-state',
            },
            'source_status': 'canonical_ontology_facts',
            'reference_repaired': False,
            'annotation_round': 'abox_augmentation_v1',
            'independent_human_validation': {},
            'llm_polish': {},
            'agent_trace': {},
        }
        out.append(t)
    return out


TASKS.extend(generate_abox_repair_tasks())
TASKS_BY_ID = {t.get('id'): t for t in TASKS}


def sha8(text: str) -> str:
    return hashlib.sha256((text or '').encode('utf-8')).hexdigest()[:8]


def docs_of(t):
    docs = list(t.get('source_docs') or [])
    for e in t.get('evidence') or []:
        d = e.get('doc_id')
        if d and d not in docs:
            docs.append(d)
    for m in (t.get('gold') or {}).get('members') or []:
        if m not in docs:
            docs.append(m)
    return docs


def task_member_docs(t):
    return [m for m in (t.get('gold') or {}).get('members') or [] if m]


def paper_ids(docs):
    out = set()
    for d in docs or []:
        out.add(d)
        out.add('Paper_' + d)
    return out


def target_relation_from_text(text):
    text = str(text or '')
    # Prefer explicit relation ids from the current ontology.
    present = [rid for rid in REL_IDS if rid in text]
    if present:
        # dedup, keep longest first to prefer station_has_type over station
        return sorted(set(present), key=len, reverse=True)
    for key, rid in [
        ('reports_variable', 'reports_variable'),
        ('applies_model', 'applies_model'),
        ('uses_station', 'uses_station'),
        ('station_has_type', 'station_has_type'),
        ('mentions', 'mentions'),
        ('sameAs', 'sameAs'),
        ('hasStationRole', 'hasStationRole'),
        ('hasModelRole', 'hasModelRole'),
        ('supported_by', 'supported_by'),
    ]:
        if key in text:
            return [rid]
    return []


def alias_candidates(t):
    q = t.get('question_zh') or t.get('question') or ''
    quoted = re.findall(r'[“"]([^”"]{1,40})[”"]', q)
    gran = (t.get('population_spec') or {}).get('gran_q')
    target = None
    m = re.search(r'sameAs\(["“]([^"”]+)["”]\)', str((t.get('population_spec') or {}).get('C_q_pop') or ''))
    if m:
        target = m.group(1)
    target = target or gran
    if target in (None, '', 'masked'):
        for station in STATION_IDS:
            if station and station in q:
                target = station
                break
    aliases = []
    for a in quoted + ([target] if target else []):
        if not a or a == 'masked' or '论文' in a or len(a) > 20:
            continue
        if a not in aliases:
            aliases.append(a)
    return target, aliases


def class_target(t):
    q = t.get('question_zh') or t.get('question') or ''
    if 'AlpineMeadow' in q or '高寒草甸' in q:
        return CLASS_BY_LABEL.get('高寒草甸')
    # fallback: any class label appearing in question
    for label, c in CLASS_BY_LABEL.items():
        if label and label in q:
            return c
    return None


def abox_relations(t):
    oe = t.get('ontology_editing') or {}
    change = str(oe.get('abox_change') or '')
    req = oe.get('required_element') or ''
    rels = []
    if 'station links' in change:
        rels = ['uses_station', 'hasStationRole']
    elif 'model links' in change:
        rels = ['applies_model', 'hasModelRole']
    elif 'reports_variable' in change:
        rels = ['reports_variable']
    elif 'applies_model' in change:
        rels = ['applies_model']
    elif 'year+uses_station' in change:
        rels = ['uses_station']
    elif 'station_has_type' in change:
        rels = ['station_has_type']
    elif 'group-by fields' in change:
        q = t.get('question_zh') or t.get('question') or ''
        if ('网站' in q or '新旧网站' in q) and '站点类型' in q:
            return ['involves_service', 'station_has_type'], []
        if '年份' in q and '模型' in q:
            return ['hasModelRole'], []
        return [], ['grouping_relations_not_supported']
    elif req in REL_IDS:
        rels = [req]
    # keep only defined relations
    rels = [r for r in rels if r in REL_IDS]
    if req in REL_IDS and req not in rels:
        rels.append(req)
    return rels, []


def build_one(t):
    oe = t.get('ontology_editing') or {}
    trigger_class = oe.get('trigger_class') or 'none'
    trigger_type = oe.get('trigger_type') or ''
    req = oe.get('required_element') or ''
    prop_target = oe.get('proposal') or {}
    subtask = oe.get('ontology_subtask') or {}
    target_text = req or prop_target.get('target') or subtask.get('target') or ''
    subtask_type = subtask.get('type') or ''
    status = 'spec_only' if trigger_class == 'none' and req == 'denominator' else 'no_intervention'
    issues = []
    target_relations = []
    target_classes = []
    target_properties = []
    alias_links = []
    remove_relations = []
    remove_classes = []
    remove_class_parent = []
    remove_properties = []
    clear_abox = []
    operations = []
    closed_world = []

    if trigger_class == 'ontology_upgrade':
        if trigger_type == 'alias_gap' or subtask_type == 'add_sameas' or target_text == 'sameAs':
            target, aliases = alias_candidates(t)
            st = str(subtask.get('target') or '')
            if '=' in st:
                left, right = [x.strip() for x in st.split('=', 1)]
                target = right or target
                aliases = [x for x in [left, right] if x]
            if not target:
                issues.append('alias_target_missing')
            alias_links = [{'alias': a, 'target': target} for a in aliases]
            operations = [{'op': 'add_alias_link', 'alias': a, 'target': target} for a in aliases]
            if len(aliases) <= 1:
                issues.append('alias_candidates_only_target')
            closed_world = ['sameAs']
        elif target_text in REL_IDS:
            target_relations = [target_text]
            remove_relations = [target_text]
            operations = [
                {'op': 'restore_relation', 'id': target_text},
                {'op': 'restore_abox_relation', 'id': target_text},
            ]
            closed_world = [target_text]
        elif target_text == 'AlpineMeadow' or trigger_type == 'class_missing' or subtask_type == 'add_class':
            c = class_target(t)
            if c:
                target_classes = [c['id']]
                remove_classes = [c['id']]
                clear_abox = ['station_has_type']
                operations = [
                    {'op': 'restore_class', 'id': c['id']},
                    {'op': 'restore_abox_relation', 'id': 'station_has_type'},
                ]
                closed_world = ['station_has_type']
            else:
                issues.append('class_target_missing')
        elif trigger_type == 'definition_gap' or subtask_type == 'add_axiom':
            c = class_target(t)
            if c:
                target_classes = [c['id']]
                remove_class_parent = [c['id']]
                operations = [{'op': 'restore_class_parent', 'id': c['id']}]
                closed_world = ['station_has_type']
            else:
                issues.append('definition_gap_class_missing')
        elif target_text == 'grouping_relations' or trigger_type == 'grouping_relations':
            issues.append('grouping_relations_not_supported')
        elif trigger_type == 'proposal_gap' or subtask_type == 'validate_proposal':
            issues.append('proposal_validation_not_state_transition')
        elif target_text == 'supported_by':
            target_relations = ['supported_by']
            remove_relations = ['supported_by']
            operations = [
                {'op': 'restore_relation', 'id': 'supported_by'},
                {'op': 'restore_abox_relation', 'id': 'supported_by'},
            ]
            closed_world = ['supported_by']
        else:
            issues.append('unknown_upgrade_target')
    elif trigger_class == 'abox_repair':
        rels, more = abox_relations(t)
        if not rels:
            definition = str(subtask.get('definition') or '')
            rels = [r for r in REL_IDS if r in definition]
            rels = [r for r in rels if r not in ('station_located_in',)]
        issues.extend(more)
        target_relations = rels
        clear_abox = rels
        if 'year+uses_station' in str(oe.get('abox_change') or '') or ('年份' in (t.get('question_zh') or t.get('question') or '') and '模型' in (t.get('question_zh') or t.get('question') or '')):
            target_properties = ['paper.year']
            remove_properties = ['paper.year']
            operations.append({'op': 'restore_property', 'id': 'paper.year'})
            operations.append({'op': 'restore_individual_attribute', 'id': 'paper.year'})
        for r in rels:
            operations.append({'op': 'restore_abox_relation', 'id': r})
        closed_world = rels
        if not rels:
            issues.append('abox_target_missing')
    elif trigger_class in ('verified', 'none'):
        status = 'spec_only' if req == 'denominator' else 'no_intervention'
    else:
        issues.append('unknown_trigger_class')

    # Build the compact mask/delta.
    spec = {
        'schema_version': 'state_spec_v1',
        'base_snapshot': 'data/canonical/ontology_v2_backfilled.json',
        'mask': {
            'remove_relations': remove_relations,
            'remove_classes': remove_classes,
            'remove_class_parent': remove_class_parent,
            'remove_properties': remove_properties,
            'remove_alias_links': [],
            'clear_abox_relations': clear_abox,
        },
        'gold_delta': {
            'trigger_class': trigger_class,
            'trigger_type': trigger_type,
            'operations': operations,
            'required_elements': [x for x in [req] if x],
        },
        'closed_world_scope': closed_world,
        'target_relations': target_relations,
        'target_classes': target_classes,
        'target_properties': target_properties,
        'alias_links': alias_links,
    }

    target_ready = bool(
        trigger_class in ('verified', 'none')
        or target_relations
        or target_classes
        or target_properties
        or alias_links
    )
    if issues and not target_ready:
        spec['status'] = 'unsupported'
        spec['issues'] = issues
        return spec, spec['status'], []

    # Compute relevant fact IDs and evidence hashes.
    docs = set(docs_of(t))
    fact_ids = []
    evidence_hashes = {}
    for r in target_relations:
        for f in BASE.get('relation_instances', []):
            if f.get('relation') != r:
                continue
            subject = str(f.get('subject') or '')
            if r in ('station_has_type', 'station_located_in') or not docs:
                use = True
            else:
                use = subject in paper_ids(docs)
            if use:
                fid = f"{r}|{f.get('subject')}|{f.get('object')}|{f.get('role','')}"
                fact_ids.append(fid)
                evidence_hashes[fid] = sha8(f.get('evidence') or '')
    spec['fact_ids'] = fact_ids
    spec['evidence_hashes'] = evidence_hashes

    before = apply_state_spec(BASE, spec)
    after = apply_state_spec(BASE, spec)
    # The current builder applies mask + delta in one pass.  Recompute a true
    # O_before by applying the mask with an empty delta.
    before_spec = json.loads(json.dumps(spec, ensure_ascii=False))
    before_spec['gold_delta']['operations'] = []
    before = apply_state_spec(BASE, before_spec)
    base_stats = state_stats(BASE)
    before_stats = state_stats(before)
    after_stats = state_stats(after)
    spec['state_hashes'] = {
        'base': state_hash(BASE),
        'before': state_hash(before),
        'after': state_hash(after),
        'after_equals_base': state_hash(after) == state_hash(BASE),
    }
    spec['state_stats'] = {'before': before_stats, 'after': after_stats}
    spec['status'] = 'spec_ready' if target_ready else 'unsupported'
    spec['issues'] = issues
    return spec, spec['status'], fact_ids


def audit_counts(rows):
    by_status = Counter(r['state_ready_status'] for r in rows)
    by_spec_status = Counter(r['state_spec_status'] for r in rows)
    by_trigger = Counter((r.get('ontology_editing') or {}).get('trigger_class') for r in rows)
    by_group = Counter(r.get('group') for r in rows)
    by_tier = Counter(r.get('tier') for r in rows)
    return {'by_status': dict(by_status), 'by_spec_status': dict(by_spec_status), 'by_trigger': dict(by_trigger), 'by_group': dict(by_group), 'by_tier': dict(by_tier)}


def main():
    out_rows = []
    for t in TASKS:
        spec, spec_status, fact_ids = build_one(t)
        trigger_class = (t.get('ontology_editing') or {}).get('trigger_class') or 'none'
        orig_docs = list(t.get('source_docs') or [])
        orig_evidence = list(t.get('evidence') or [])
        derived_docs = list(dict.fromkeys(orig_docs + task_member_docs(t)))
        derived_evidence = orig_evidence
        if not derived_evidence and task_member_docs(t):
            derived_evidence = [
                {'doc_id': d, 'quote': '', 'source': 'derived_from_gold_members'}
                for d in task_member_docs(t)
            ]

        membership_eligible = bool((t.get('evaluation') or {}).get('members'))
        answer_eligible = bool((t.get('evaluation') or {}).get('answer'))
        has_original_evidence = bool(orig_docs and orig_evidence)
        has_derived_evidence = bool(derived_docs and derived_evidence)
        has_gold_ref = membership_eligible or answer_eligible
        target_ready = spec_status == 'spec_ready'
        has_nonempty_members = bool((t.get('gold') or {}).get('members') or [])
        if not target_ready:
            state_status = 'unsupported'
        elif trigger_class in ('verified', 'none'):
            state_status = 'spec_only' if spec.get('gold_delta', {}).get('required_elements') == ['denominator'] else 'no_intervention_ready'
        elif has_original_evidence and has_nonempty_members:
            state_status = 'strict_ready'
        elif has_original_evidence and has_gold_ref:
            state_status = 'empty_reference_ready'
        elif has_gold_ref and (t.get('gold') or {}).get('answer') == 0 and not has_nonempty_members:
            state_status = 'empty_result_ready'
        elif has_derived_evidence and has_gold_ref:
            state_status = 'derived_ready'
        elif has_gold_ref:
            state_status = 'needs_evidence'
        else:
            state_status = 'needs_membership_or_answer_gold'

        row = dict(t)
        row['state_spec'] = spec
        row['state_spec_status'] = spec_status
        row['state_ready_status'] = state_status
        row['state_ready'] = state_status in ('strict_ready', 'empty_reference_ready', 'empty_result_ready', 'derived_ready', 'no_intervention_ready')
        row['state_ready_strict'] = state_status == 'strict_ready'
        row['derived_source_docs'] = derived_docs
        row['derived_evidence'] = derived_evidence
        row['derived_fact_ids'] = fact_ids
        out_rows.append(row)

    # Rewrite atomically: remove previous file content before append.
    OUT.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in out_rows), encoding='utf-8')

    strict = [r['id'] for r in out_rows if r['state_ready_status'] == 'strict_ready']
    empty_reference = [r['id'] for r in out_rows if r['state_ready_status'] == 'empty_reference_ready']
    empty_result = [r['id'] for r in out_rows if r['state_ready_status'] == 'empty_result_ready']
    derived = [r['id'] for r in out_rows if r['state_ready_status'] == 'derived_ready']
    needs_gold = [r['id'] for r in out_rows if r['state_ready_status'] == 'needs_membership_or_answer_gold']
    state_change_ids = [
        r['id'] for r in out_rows
        if (r.get('ontology_editing') or {}).get('trigger_class') in ('ontology_upgrade', 'abox_repair')
    ]
    state_change_strict = [i for i in state_change_ids if i in set(strict)]
    gap_ids = [i for i in state_change_ids if i not in set(strict)]
    filled_gap = [i for i in gap_ids if i in set(empty_reference + empty_result + derived)]
    remaining_gap = [i for i in gap_ids if i not in set(filled_gap)]
    manifest = {
        'schema_version': 'state_spec_v1',
        'source_dataset': str(SRC.relative_to(ROOT)),
        'base_snapshot': str(BASE_PATH.relative_to(ROOT)),
        'output': str(OUT.relative_to(ROOT)),
        'n_tasks': len(out_rows),
        'strict_ready': strict,
        'empty_reference_ready': empty_reference,
        'empty_result_ready': empty_result,
        'derived_ready': derived,
        'needs_membership_or_answer_gold': needs_gold,
        'gap_ids': gap_ids,
        'filled_gap': filled_gap,
        'remaining_gap': remaining_gap,
        'state_change_strict': state_change_strict,
        'counts': audit_counts(out_rows),
        'status_examples': {},
    }
    by_status = defaultdict(list)
    for r in out_rows:
        by_status[r['state_ready_status']].append(r['id'])
    manifest['status_examples'] = {k: v[:8] for k, v in by_status.items()}
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    (DATA / 'tiers/state_ready_strict.json').write_text(json.dumps({
        'n': len(strict), 'ids': strict,
        'by_trigger': dict(Counter((TASKS_BY_ID[i].get('ontology_editing') or {}).get('trigger_class') for i in strict)),
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    (DATA / 'tiers/state_gap_manifest.json').write_text(json.dumps({
        'n': len(gap_ids), 'ids': gap_ids, 'filled_n': len(filled_gap), 'filled_ids': filled_gap,
        'remaining_n': len(remaining_gap), 'remaining_ids': remaining_gap,
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    (DATA / 'tiers/state_gap_remaining.json').write_text(json.dumps([
        {'id': i, 'group': (TASKS_BY_ID[i].get('group')), 'trigger_class': (TASKS_BY_ID[i].get('ontology_editing') or {}).get('trigger_class'),
         'state_ready_status': next(r['state_ready_status'] for r in out_rows if r['id'] == i)}
        for i in remaining_gap
    ], ensure_ascii=False, indent=2), encoding='utf-8')

    lines = [
        '# State Spec Audit',
        '',
        'Source: `data/tiers/dataset_v3_corrected.jsonl` plus deterministic ABox-repair augmentation from canonical ontology facts',
        'Base snapshot: `data/canonical/ontology_v2_backfilled.json`',
        f'Output: `{OUT.relative_to(ROOT)}`',
        '',
        '## Counts',
        '',
        '| status | n |',
        '|---|---:|',
    ]
    for k, v in sorted(Counter(r['state_ready_status'] for r in out_rows).items()):
        lines.append(f'| {k} | {v} |')
    lines += [
        '',
        f'- strict state-ready (nonempty membership gold): **{len(strict)}**',
        f'- state-change strict-ready: **{len(state_change_strict)}**',
        f'- empty-reference ready: **{len(empty_reference)}**',
        f'- empty-result ready: **{sum(1 for r in out_rows if r["state_ready_status"] == "empty_result_ready")}**',
        f'- derived-ready (evidence derived from gold members): **{len(derived)}**',
        f'- filled state-change gaps: **{len(filled_gap)}**',
        f'- remaining gap: **{len(remaining_gap)}**',
        f'- remaining IDs: {", ".join(remaining_gap) if remaining_gap else "none"}',
        f'- state_spec unsupported: **{sum(1 for r in out_rows if r["state_ready_status"] == "unsupported")}**',
        '',
        '## Counts by trigger',
        '',
        '| trigger | n | strict | derived | unsupported |',
        '|---|---:|---:|---:|---:|',
    ]
    for trig, n in sorted(Counter((r.get('ontology_editing') or {}).get('trigger_class') or 'none' for r in out_rows).items()):
        rs = [r for r in out_rows if ((r.get('ontology_editing') or {}).get('trigger_class') or 'none') == trig]
        lines.append(
            f'| {trig} | {n} | {sum(1 for r in rs if r["state_ready_status"] == "strict_ready")} | '
            f'{sum(1 for r in rs if r["state_ready_status"] in ("derived_ready", "empty_reference_ready"))} | '
            f'{sum(1 for r in rs if r["state_ready_status"] == "unsupported")} |'
        )
    lines += [
        '',
        '## Notes',
        '',
        '- `strict_ready`: original source/evidence + gold reference + recoverable state target.',
        '- `empty_reference_ready`: membership gold is an empty set; no positive member evidence is required.',
        '- `empty_result_ready`: exact answer is zero and membership gold is empty; state repair can be checked under declared closed-world scope, but this is not positive-member evidence.',
        '- `derived_ready`: missing source/evidence was derived from `gold.members`; still needs review before calling it gold.',
        '- `needs_membership_or_answer_gold`: state target is recoverable, but the task still lacks answer/membership gold.',
        '- `unsupported`: target relation/class could not be recovered from current annotations.',
        '- `gold_delta.operations` use `restore_*` operations against the full snapshot; this is a compact representation, not a hand-written full ontology per task.',
    ]
    AUDIT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({'tasks': len(out_rows), 'strict': len(strict), 'state_change_strict': len(state_change_strict), 'derived': len(derived), 'status': dict(Counter(r['state_ready_status'] for r in out_rows))}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
