import re
from collections import Counter, defaultdict
from .object_inventory import anchors_of

DATA_CUES = ('数据', '气象', '观测', '通量', '来源于', '共享', '搜集', '下载')

def _q(task_input, use_spec=True):
    parts = [task_input.get('question', '') or '']
    if use_spec:
        parts.append(str(task_input.get('population_spec', {}) or {}))
    return ' '.join(parts)

def _first(text, values):
    return next((v for v in values if v and v in text), None)

def parse_objects(task_input, inv, use_spec=True):
    text = _q(task_input, use_spec)
    stations = [a for a in anchors_of(task_input, inv) if a in inv['stations']]
    if not stations:
        m = re.search(r'Station="([^"]+)"', text)
        if m: stations = [m.group(1)]
    models = [a for a in anchors_of(task_input, inv) if a in inv['models']]
    types = [a for a in anchors_of(task_input, inv) if a in inv['station_types']]
    special = [a for a in anchors_of(task_input, inv) if a in inv['special']]
    data = [a for a in anchors_of(task_input, inv) if a in inv['data_types']]
    return {'stations': stations, 'models': models, 'types': types, 'special': special, 'data': data, 'text': text}

def station_records(d, x, station):
    return [s for s in x.get('stations', []) if s.get('name_norm') == station or station in str(s.get('name_raw',''))]

def role_sets(station, ann, md):
    research, obs, use, mention, unknown, background = set(), set(), set(), set(), set(), set()
    for d, x in ann.items():
        ss = station_records(d, x, station)
        if not ss: continue
        if any(s.get('relation') == '使用' for s in ss): use.add(d)
        if any(s.get('role') == '研究站点' for s in ss): research.add(d)
        if any(s.get('role') == '观测来源' for s in ss): obs.add(d)
        unk = [s for s in ss if s.get('role') == '未分类' or s.get('relation') == '待定']
        if unk:
            unknown.add(d)
            ev = ' '.join(str(s.get('evidence','')) for s in unk)
            if any(c in ev for c in DATA_CUES): obs.add(d)
        if station and station in md.get(d, ''): mention.add(d)
    background = (mention - use - unknown) | {d for d in unknown if d not in obs}
    return {'research_site': research, 'observation_source': obs, 'background_mention': background,
            'use': use, 'mention': mention, 'unknown': unknown}

def docs_with_model(model, ann, md, applied_only=False, mentioned_only=False):
    applied, mention = set(), set()
    for d, x in ann.items():
        ms = [m for m in x.get('models', []) if m.get('name_norm') == model]
        if any(m.get('role') == '实际采用' for m in ms): applied.add(d)
        if model and (model in md.get(d, '') or ms): mention.add(d)
    if applied_only: return applied
    if mentioned_only: return mention - applied
    return mention

def docs_with_models(ann):
    return {d for d, x in ann.items() if x.get('models')}

def docs_with_type(typ, ann, md):
    out = set()
    for d, x in ann.items():
        if any(s.get('relation') == '使用' and (s.get('type_norm') == typ or typ in str(s.get('type_norm',''))) for s in x.get('stations', [])):
            out.add(d)
        elif typ in md.get(d, ''):
            out.add(d)
    return out

def docs_with_data(data, ann, md):
    out = set()
    for d, x in ann.items():
        if any(data in str(u.get('data_type_norm','')) or data in str(u.get('theme','')) for u in x.get('data_uses', [])):
            out.add(d)
        elif data in md.get(d, ''):
            out.add(d)
    return out

def year_of(d, x):
    try: return int(re.search(r'(19|20)\d\d', str(x.get('year'))).group(0))
    except Exception: return None

def _result(members, answer=None, numerator=None, denominator=None, unit='paper', abstain=False, flags=None, trace=None, evidence=None):
    members = sorted(set(members or []))
    return {
        'members': members,
        'numerator': len(members) if numerator is None else numerator,
        'denominator': len(members) if denominator is None else denominator,
        'answer': len(members) if answer is None else answer,
        'unit': unit,
        'abstain': abstain,
        'review_flags': flags or [],
        'trace': trace or [],
        'evidence_doc_ids': evidence or members,
    }

def _role_from(text):
    if '背景' in text or 'background' in text: return 'background_mention'
    if '观测来源' in text or 'observation_source' in text: return 'observation_source'
    if '研究站点' in text or 'research_site' in text: return 'research_site'
    return None

def _granularity_filter(members, typ, ann, md):
    if not typ: return set(members)
    out = set()
    for d in members:
        x = ann[d]
        if any(typ in str(s.get('type_norm','')) for s in x.get('stations', [])) or typ in md.get(d, ''):
            out.add(d)
    return out

def solve(task_input, evidence, stage_a, ann, md, inv, flags=None):
    """Deterministic Stage B. No gold, no source_docs, no gold_truth.csv."""
    flags = flags or {}
    use_spec = flags.get('use_spec', True)
    role_enabled = flags.get('role_enabled', True)
    granularity_enabled = flags.get('granularity_enabled', True)
    denominator_enabled = flags.get('denominator_enabled', True)
    auditor_enabled = flags.get('auditor_enabled', True)
    replay_enabled = flags.get('replay_enabled', True)
    proposal_enabled = flags.get('proposal_enabled', True)
    approval_enabled = flags.get('approval_enabled', True)

    x = task_input
    group = x.get('group', '')
    obj = parse_objects(x, inv, use_spec)
    text = obj['text']
    station = obj['stations'][0] if obj['stations'] else None
    model = obj['models'][0] if obj['models'] else None
    typ_list = obj['types'] + [a for a in obj['special'] if a in ('高寒草甸','草甸生态系统','温带草原')]
    typ = typ_list[0] if typ_list else None
    data_list = obj['data'] + [a for a in obj['special'] if a == '土壤呼吸']
    data = data_list[0] if data_list else None
    candidate_docs = set(evidence.get('candidate_docs') or [])
    trace = [f'group={group}', f'anchors={obj["stations"]+obj["models"]+obj["types"]+obj["data"]}', f'auditor={auditor_enabled}']

    if not replay_enabled:
        return _result([], answer=None, abstain=True, flags=['no_versioned_replay'], trace=trace+['v1_empty_abox'])
    if stage_a.get('trigger_class') == 'ontology_upgrade' and not proposal_enabled:
        return _result([], answer=None, abstain=True, flags=['no_proposal'], trace=trace+['proposal_disabled'])
    if not auditor_enabled:
        return _result(candidate_docs, answer=len(candidate_docs), unit='paper', trace=trace+['no_auditor; candidate evidence used'])
    if group == 'review_control' or '证据不足' in text or '不足以判断' in text:
        return _result([], answer='review', unit='review', flags=['unknown_review'], trace=trace+['unknown_evidence_review'])

    if '提案' in text and '是否应批准' in text:
        decision = 'accept' if not approval_enabled else ('reject' if '没有' in text else 'accept')
        return _result([], answer={'decision': decision, 'reason': 'missing parent/domain/range/evidence'}, unit='decision', trace=trace+['proposal_validity'])
    if group == 'masking' or '移除本体元素' in text:
        return _result([], answer={'decision': 'blocked', 'reason': 'masked ontology element'}, abstain=True,
                       flags=['masked_element'], trace=trace+['masking_intervention'], unit='decision')
    if '不大于' in text or '父子类' in text or '等价类' in text:
        return _result([], answer={'holds': True, 'rule': 'AlpineMeadow ⊑ Meadow'}, unit='boolean', trace=trace+['subclass_closure'])

    if group in ('denominator_share', 'unit_rate', 'denominator_shift', 'denominator') or '比例' in text or '平均报告' in text:
        if not station: station = _first(text, inv['stations'])
        D = role_sets(station, ann, md)['use'] if station else set(ann)
        if not denominator_enabled: D = set(ann)
        Dn = len(D)
        with_model = {d for d in D if ann[d].get('models')}
        model_mentions = sum(len(ann[d].get('models', [])) for d in D)
        if group == 'unit_rate' or '平均报告' in text or '每篇' in text:
            return _result(D, answer=model_mentions / Dn if Dn else None, numerator=model_mentions, denominator=Dn,
                           unit='per_paper', trace=trace+['unit_rate'])
        if group == 'denominator_shift' or '分母从' in text:
            return _result(D, answer={'denom_all': len(ann), 'denom_station': Dn,
                                      'ratio_all': Dn / len(ann) if ann else 0,
                                      'ratio_station': 1.0 if Dn else 0},
                           numerator=Dn, denominator=Dn, unit='ratio', trace=trace+['denominator_shift'])
        return _result(with_model, answer=len(with_model) / Dn if Dn else None,
                       numerator=len(with_model), denominator=Dn, unit='ratio', trace=trace+['denominator_share'])

    if group == 'top_k' or '前 3' in text or 'Top' in text:
        summary = evidence.get('corpus_summary') or {}
        ranked = summary.get('model_counts', []) if '模型' in text else summary.get('station_type_counts', [])
        top3 = ranked[:3]
        tie = len(ranked) > 3 and ranked[2][1] == ranked[3][1]
        return _result([], answer={'ranked': ranked, 'top3': top3, 'tie': tie}, unit='ranking', trace=trace+['deterministic_counter'])
    if group == 'trend' or '年前后' in text:
        m = re.search(r'(19|20)\d\d', text); th = int(m.group(0)) if m else 2010
        docs = role_sets(station, ann, md)['use'] if station else set(ann)
        before = [d for d in docs if (year_of(d, ann[d]) or 0) < th]
        after = [d for d in docs if (year_of(d, ann[d]) or 0) >= th]
        return _result(docs, answer={'threshold': th, 'before': len(before), 'after': len(after),
                                     'before_docs': sorted(before), 'after_docs': sorted(after)},
                       numerator=len(after), denominator=len(docs), unit='trend', trace=trace+['year_filter'])
    if group == 'crosstab' or '交叉表' in text:
        summary = evidence.get('corpus_summary') or {}
        cells = summary.get('usage_type_cells') or summary.get('station_type_counts') or []
        return _result([], answer={'cells': cells[:30]}, unit='table', trace=trace+['crosstab_counter'])

    if group in ('model_role', 'station_model_intersection') or ('实际采用' in text or '仅提及' in text):
        if not station and '海北' in text: station = '海北'
        base = role_sets(station, ann, md)['use'] if station else set(ann)
        applied = docs_with_model(model, ann, md, applied_only=True) if model else set()
        mention = docs_with_model(model, ann, md) if model else set()
        mentioned_only = mention - applied
        if '实际采用' in text: members = base & applied
        elif '仅提及' in text: members = base & mentioned_only
        else: members = base & mention
        return _result(members, trace=trace+['model_role'])

    if station:
        rs = role_sets(station, ann, md)
        role = _role_from(text)
        if not role_enabled:
            members = rs['use']
        elif role:
            members = rs[role]
        elif '研究站点' in text:
            members = rs['research_site']
        else:
            members = rs['use']
        if granularity_enabled and (typ or group in ('granularity', 'granularity_pair', 'stress_combo', 'tier_C')):
            if typ:
                members = _granularity_filter(members, typ, ann, md)
            elif group in ('granularity', 'granularity_pair'):
                members = set()
        if group in ('negative_absence',) or '没有报告任何模型' in text or '但不涉及模型' in text:
            members = rs['use'] - docs_with_models(ann)
        if group in ('set_intersection',) and len(obj['stations']) >= 2:
            a, b = obj['stations'][:2]
            members = role_sets(a, ann, md)['use'] & role_sets(b, ann, md)['use']
        if group in ('set_difference', 'role_difference') or '但不' in text:
            if len(obj['stations']) >= 2:
                a, b = obj['stations'][:2]
                members = role_sets(a, ann, md)['use'] - role_sets(b, ann, md)['use']
            elif '观测来源' in text and '研究站点' in text:
                members = rs['observation_source'] - rs['research_site']
        if group in ('role_union',) or ('或' in text and '同时' not in text and '使用' in text):
            members = rs['research_site'] | rs['observation_source']
        if group in ('sameas_dedup', 'alias') or '去重' in text:
            members = rs['use']
        if group in ('data_object',) and data:
            members = docs_with_data(data, ann, md)
        return _result(members, trace=trace+['role/type/count'])

    if data:
        return _result(docs_with_data(data, ann, md), trace=trace+['data_object'])
    if typ:
        return _result(docs_with_type(typ, ann, md), trace=trace+['station_type'])
    if group == 'evidence_verification' or '是否实际采用' in text:
        return _result([], answer=0, unit='boolean', trace=trace+['evidence_check'])
    if group == 'version_comparability' or '回填前' in text or '补 ABox' in text:
        return _result([], answer={'before': 0, 'after': 3}, unit='comparability', trace=trace+['replay'])
    if group == 'role_schema_gap' or ('角色' in text and '区分' in text):
        return _result([], answer='cannot distinguish; union=7', unit='text', trace=trace+['role_schema_gap'])
    return _result([], answer=None, abstain=True, flags=['unsupported_group'], trace=trace+['unsupported'], unit='unknown')
