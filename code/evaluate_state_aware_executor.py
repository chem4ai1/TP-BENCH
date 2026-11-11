"""Compare the conservative availability guard with a state-filtered executor.

The guard condition uses the current evaluate_state_repair result. The
state-aware condition filters annotation records and the object inventory by
the constructed O_before/O_after T/A before running the deterministic engine.
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from copy import deepcopy
from pathlib import Path

from core_v3 import data_loader, evidence_builder, object_inventory, population_engine, schema_checker, strict_metrics
from core_v3.state_builder import apply_state_spec

import evaluate_state_repair as esr

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
DATASET = DATA / 'tiers/dataset_v4_state.jsonl'
SR = json.loads((DATA / 'results_v4/state_repair/state_repair_results.json').read_text(encoding='utf-8'))
OUT_DIR = DATA / 'results_v4/state_aware'
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_JSON = OUT_DIR / 'state_aware_comparison.json'
OUT_MD = OUT_DIR / 'state_aware_comparison.md'
BASE = esr.BASE
INDS = {i.get('id'): i for i in BASE.get('individuals', [])}


def fact_sets(state):
    inds = {i.get('id'): i for i in state.get('individuals', [])}
    rels = {r.get('id') for r in state.get('relations', [])}
    stations = set()
    roles = set()
    models = set()
    model_roles = set()
    types = set()
    variables = set()
    for f in state.get('relation_instances', []):
        rel = f.get('relation')
        sub = str(f.get('subject') or '').replace('Paper_', '')
        obj = f.get('object')
        if rel == 'uses_station':
            name = (inds.get(obj, {}).get('attributes') or {}).get('name')
            if name: stations.add((sub, name))
        elif rel == 'hasStationRole':
            name = (inds.get(obj, {}).get('attributes') or {}).get('name')
            if name: roles.add((sub, name, f.get('role') or '未分类'))
        elif rel == 'applies_model':
            name = (inds.get(obj, {}).get('attributes') or {}).get('name')
            if name: models.add((sub, name))
        elif rel == 'hasModelRole':
            name = (inds.get(obj, {}).get('attributes') or {}).get('name')
            if name: model_roles.add((sub, name, f.get('role') or '未分类'))
        elif rel == 'station_has_type':
            st = next((i for i in state.get('individuals', []) if i.get('id') == f.get('subject')), {})
            typ = (inds.get(obj, {}).get('attributes') or {}).get('name')
            stname = (st.get('attributes') or {}).get('name')
            if stname and typ: types.add((stname, typ))
        elif rel == 'reports_variable':
            name = (inds.get(obj, {}).get('attributes') or {}).get('name')
            if name: variables.add((sub, name))
    return {'relations': rels, 'stations': stations, 'roles': roles, 'models': models,
            'model_roles': model_roles, 'types': types, 'variables': variables}


def filter_ann(ann, state):
    fs = fact_sets(state)
    out = {}
    for doc, x in ann.items():
        y = deepcopy(x)
        if 'uses_station' not in fs['relations']:
            y['stations'] = []
        else:
            keep = []
            for s in y.get('stations', []):
                name = s.get('name_norm')
                if (doc, name) not in fs['stations']:
                    continue
                role = next((r for (d, n, r) in fs['roles'] if d == doc and n == name), None)
                s['role'] = role or '未分类'
                s['relation'] = '使用' if role else '待定'
                typ = next((t for (n, t) in fs['types'] if n == name), None)
                s['type_norm'] = typ or ''
                keep.append(s)
            y['stations'] = keep
        if 'applies_model' not in fs['relations']:
            y['models'] = []
        else:
            keep = []
            for m in y.get('models', []):
                name = m.get('name_norm')
                if (doc, name) not in fs['models']:
                    continue
                role = next((r for (d, n, r) in fs['model_roles'] if d == doc and n == name), None)
                m['role'] = role or '未分类'
                m['relation'] = '使用' if role else '待定'
                keep.append(m)
            y['models'] = keep
        if 'reports_variable' not in fs['relations']:
            y['data_uses'] = []
        else:
            vars_ = {n for (d, n) in fs['variables'] if d == doc}
            y['data_uses'] = [u for u in y.get('data_uses', []) if (u.get('data_type_norm') in vars_ or u.get('theme') in vars_ or not vars_)]
        if 'paper.year' not in fs.get('properties', set()) and not any(p.get('id') == 'paper.year' for p in state.get('properties', [])):
            y['year'] = None
        out[doc] = y
    return out


def run_state_aware(tasks, ann, md):
    rows = []
    for t in tasks:
        x, y = data_loader.split_task(t)
        ev = evidence_builder.build_evidence(x, object_inventory.build_inventory(ann), ann, md)
        spec = t['state_spec']
        before_obj = apply_state_spec(BASE, esr.with_ops(spec, []))
        gold_obj = apply_state_spec(BASE, spec)
        before_ann = filter_ann(ann, before_obj)
        gold_ann = filter_ann(ann, gold_obj)
        before_inv = object_inventory.build_inventory(before_ann)
        gold_inv = object_inventory.build_inventory(gold_ann)
        before_state = schema_checker.schema_state(before_obj)
        gold_state = schema_checker.schema_state(gold_obj)
        stage_before = schema_checker.stage_a(x, ev, before_state, {})
        stage_gold = schema_checker.stage_a(x, ev, gold_state, {})
        pred_obj = apply_state_spec(BASE, esr.with_ops(spec, esr.predicted_operations(t, stage_before)))
        pred_ann = filter_ann(ann, pred_obj)
        pred_inv = object_inventory.build_inventory(pred_ann)
        pred_state = schema_checker.schema_state(pred_obj)
        stage_pred = schema_checker.stage_a(x, ev, pred_state, {})
        pred_before = population_engine.solve(x, ev, stage_before, before_ann, md, before_inv, {})
        pred_mid = population_engine.solve(x, ev, stage_pred, pred_ann, md, pred_inv, {})
        pred_gold = population_engine.solve(x, ev, stage_gold, gold_ann, md, gold_inv, {})
        ref = {'id': y['id'], 'group': y['group'],
               'gold': {'answer': y['answer'], 'members': list(y['members']),
                        'denominator': y['denominator'], 'denominator_members': y.get('denominator_members') or []},
               'evaluation': y.get('evaluation') or {'answer': True, 'members': True, 'denominator_count': False, 'reasons': []}}
        sb = strict_metrics.evaluate(ref, esr.pred_object(pred_before))
        sm = strict_metrics.evaluate(ref, esr.pred_object(pred_mid))
        sg = strict_metrics.evaluate(ref, esr.pred_object(pred_gold))
        rows.append({'id': y['id'], 'group': y['group'], 'trigger_gold': esr.normalize_trigger(y.get('trigger_class')),
                     'state_ready_status': t.get('state_ready_status'), 'frozen': sb, 'predicted': sm, 'gold': sg,
                     'members_frozen': sorted(pred_before.get('members') or []),
                     'members_predicted': sorted(pred_mid.get('members') or []),
                     'members_gold': sorted(pred_gold.get('members') or [])})
    return rows


def summarize(rows):
    return {'n': len(rows), 'frozen': strict_metrics.summarize([r['frozen'] for r in rows]),
            'predicted': strict_metrics.summarize([r['predicted'] for r in rows]),
            'gold': strict_metrics.summarize([r['gold'] for r in rows])}


def main():
    ann, md, _, _ = data_loader.load_resources()
    tasks = [json.loads(l) for l in DATASET.read_text(encoding='utf-8').splitlines() if l.strip()]
    guard_rows = SR['rows']
    aware_rows = run_state_aware(tasks, ann, md)
    guard_by = defaultdict(list); aware_by = defaultdict(list)
    for r in guard_rows:
        guard_by[r['trigger_gold']].append(r)
    for r in aware_rows:
        aware_by[r['trigger_gold']].append(r)
    result = {
        'method': 'state-aware executor comparison',
        'note': 'guard = target availability check plus annotation evidence; state-aware = T/A-filtered annotations and inventory. This is a state-filtered execution proxy, not a full OWL reasoner.',
        'guard': summarize(guard_rows),
        'state_aware': summarize(aware_rows),
        'by_trigger': {k: {'guard': summarize(guard_by[k]), 'state_aware': summarize(aware_by[k])} for k in ('ontology_upgrade', 'abox_repair', 'no_intervention')},
        'rows': aware_rows,
    }
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = ['# State-Aware Executor Comparison', '', result['note'], '',
             '| Condition | Exact | P Macro-F1 | Nonempty F1 | Abstain |', '|---|---:|---:|---:|---:|']
    for label, key in [('Guard', 'guard'), ('State-aware', 'state_aware')]:
        for cond, cname in [('frozen', 'frozen'), ('predicted', 'predicted'), ('gold', 'reference')]:
            a = result[key][cond]
            lines.append(f"| {label} {cname} | {a['strict_answer_accuracy']:.3f} | {a['population_macro_f1']:.3f} | {a['nonempty_population_f1']:.3f} | {a['abstain_rate']:.3f} |")
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'rows'}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
