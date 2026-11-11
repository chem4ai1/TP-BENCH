"""Per-task state-repair evaluation on TP-Bench v4 state specs.

This script is deliberately explicit about the three conditions:
  frozen_O      : the task-specific O_before, with the repair blocked
  predicted_O   : O_before plus the repair inferred from Stage A
  gold_O        : O_after reconstructed from the task's state_spec

The current deterministic Stage B still consumes annotation records; the state
availability guard prevents a task from being scored when its required relation,
class, property, or alias link is absent.  This is the first state-aware pass and
exposes exactly where a future full logical executor is needed.
"""
from __future__ import annotations

import json
import os
import re
from collections import Counter, defaultdict
from copy import deepcopy
from pathlib import Path

from core_v3 import config, data_loader, object_inventory, evidence_builder, schema_checker, population_engine, strict_metrics
from core_v3.state_builder import apply_state_spec

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
DATASET = DATA / 'tiers/dataset_v4_state.jsonl'
BASE_PATH = DATA / 'canonical/ontology_v2_backfilled.json'
OUT_DIR = DATA / 'results_v4/state_repair'
OUT_JSON = OUT_DIR / 'state_repair_results.json'
OUT_MD = OUT_DIR / 'state_repair_results.md'
OUT_DIR.mkdir(parents=True, exist_ok=True)

BASE = json.loads(BASE_PATH.read_text(encoding='utf-8'))
REL_IDS = {r.get('id') for r in BASE.get('relations', [])}
CLASSES = {c.get('id'): c for c in BASE.get('classes', [])}
CLASS_BY_LABEL = {c.get('label'): c for c in BASE.get('classes', []) if c.get('label')}
PROPS = {p.get('id') for p in BASE.get('properties', [])}

FACT_LEVEL_ABOX = os.environ.get('FACT_LEVEL_ABOX', '0') == '1'

VARIANT_FLAGS = {
    'full': {},
    'no_auditor': {'auditor_enabled': False},
    'no_role': {'role_enabled': False},
    'no_granularity': {'granularity_enabled': False},
    'no_denominator': {'denominator_enabled': False},
    'no_replay': {'replay_enabled': False},
}


def normalize_trigger(value):
    v = value or 'none'
    if v in ('verified', 'none', 'spec_only'):
        return 'no_intervention'
    return v


def state_available(state, spec):
    """Conservative availability check for the task's repaired target."""
    for rid in spec.get('target_relations') or []:
        if rid not in {r.get('id') for r in state.get('relations', [])}:
            return False, f'missing_relation:{rid}'
        if not any(x.get('relation') == rid for x in state.get('relation_instances', [])):
            return False, f'empty_abox:{rid}'
    for cid in spec.get('target_classes') or []:
        if cid not in {c.get('id') for c in state.get('classes', [])}:
            return False, f'missing_class:{cid}'
    for pid in spec.get('target_properties') or []:
        if pid not in {p.get('id') for p in state.get('properties', [])}:
            return False, f'missing_property:{pid}'
    for cid in (spec.get('mask') or {}).get('remove_class_parent') or []:
        c = next((x for x in state.get('classes', []) if x.get('id') == cid), None)
        if c is not None and not c.get('parent'):
            return False, f'missing_class_parent:{cid}'
    if spec.get('alias_links') and not state.get('same_as'):
        return False, 'missing_alias_link'
    return True, 'available'


def class_for_req(req, task):
    txt = str(req or '')
    if txt in CLASSES:
        return CLASSES[txt]
    if txt in CLASS_BY_LABEL:
        return CLASS_BY_LABEL[txt]
    if 'AlpineMeadow' in txt or '高寒草甸' in txt:
        return CLASS_BY_LABEL.get('高寒草甸')
    for c in CLASSES.values():
        if c.get('label') and c['label'] in txt:
            return c
    return None


def relation_targets_for_repair(task, reqs):
    group = task.get('group') or ''
    q = (task.get('question_zh') or task.get('question') or '') + ' ' + str(task.get('population_spec') or {})
    rels = []
    for r in reqs:
        if r in REL_IDS and r not in rels:
            rels.append(r)
    # ABox repair often names one anchor but requires a linked role relation too.
    if group in ('model_role', 'negative_absence') or '模型' in q:
        for r in ('applies_model', 'hasModelRole'):
            if r not in rels:
                rels.append(r)
    if group in ('station_role', 'stress_combo', 'role_union', 'set_operation', 'top_k', 'trend') or '站点' in q:
        for r in ('uses_station', 'hasStationRole'):
            if r not in rels:
                rels.append(r)
    if group == 'data_object' or '变量' in q:
        if 'reports_variable' not in rels:
            rels.append('reports_variable')
    if '站点类型' in q or group in ('granularity', 'crosstab'):
        if 'station_has_type' not in rels:
            rels.append('station_has_type')
    return [r for r in rels if r in REL_IDS]


def predicted_operations(task, stage_a):
    trigger = (stage_a or {}).get('trigger_class') or 'none'
    reqs = (stage_a or {}).get('required_elements') or []
    if trigger in ('none', 'verified', 'spec_only'):
        return []
    ops = []
    rels = []
    if trigger == 'ontology_upgrade':
        for req in reqs:
            if req == 'sameAs':
                continue
            c = class_for_req(req, task)
            if c:
                ops.append({'op': 'restore_class', 'id': c['id']})
                rels.append('station_has_type')
            elif req in REL_IDS:
                rels.append(req)
        if 'grouping_relations' in reqs:
            q = (task.get('question_zh') or task.get('question') or '')
            if '网站' in q:
                rels.extend(['involves_service', 'station_has_type'])
            if '年份' in q:
                ops.append({'op': 'restore_property', 'id': 'paper.year'})
                ops.append({'op': 'restore_individual_attribute', 'id': 'paper.year'})
                rels.append('hasModelRole')
        for r in rels:
            ops.append({'op': 'restore_relation', 'id': r})
            ops.append({'op': 'restore_abox_relation', 'id': r})
    elif trigger == 'abox_repair':
        rels = relation_targets_for_repair(task, reqs)
        for r in rels:
            ops.append({'op': 'restore_abox_relation', 'id': r})
        if task.get('group') in ('trend',) or 'year' in str((task.get('population_spec') or {}).get('C_q_pop', '')):
            ops.append({'op': 'restore_property', 'id': 'paper.year'})
            ops.append({'op': 'restore_individual_attribute', 'id': 'paper.year'})
    # remove duplicate ops
    seen = set()
    out = []
    for op in ops:
        key = json.dumps(op, ensure_ascii=False, sort_keys=True)
        if key not in seen:
            seen.add(key)
            out.append(op)
    return out


def with_ops(spec, ops):
    s = deepcopy(spec)
    s['gold_delta']['operations'] = ops
    return s


def pred_object(pred):
    return {
        'status': 'abstain' if (pred.get('abstain') or pred.get('status') == 'abstain') else 'ok',
        'answer': pred.get('answer'),
        'members': pred.get('members') or [],
        'denominator_count': pred.get('denominator'),
        'denominator_members': [],
    }


def abstain_obj(reason):
    return {'status': 'abstain', 'answer': None, 'members': [], 'denominator_count': None,
            'denominator_members': [], 'abstain_reason': reason}


def coverage_metrics(gold, pred):
    g, p = set(gold or []), set(pred or [])
    tp, fp, fn = len(g & p), len(p - g), len(g - p)
    prec = tp / len(p) if p else (1.0 if not g else 0.0)
    rec = tp / len(g) if g else (1.0 if not p else 0.0)
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
    over = fp / len(p) if p else 0.0
    under = fn / len(g) if g else 0.0
    return {'precision': prec, 'recall': rec, 'f1': f1, 'overcoverage': over, 'undercoverage': under,
            'tp': tp, 'fp': fp, 'fn': fn}


def summarize(rows, key):
    rr = [r[key] for r in rows if r.get(key)]
    return strict_metrics.summarize(rr) if rr else {}


def run():
    ann, md, _, _ = data_loader.load_resources()
    inv = object_inventory.build_inventory(ann)
    tasks = [json.loads(l) for l in DATASET.read_text(encoding='utf-8').splitlines() if l.strip()]
    rows = []
    for t in tasks:
        x, y = data_loader.split_task(t)
        ev = evidence_builder.build_evidence(x, inv, ann, md)
        spec = t['state_spec']
        before = apply_state_spec(BASE, with_ops(spec, []))
        gold_after = apply_state_spec(BASE, spec)
        before_state = schema_checker.schema_state(before)
        gold_state = schema_checker.schema_state(gold_after)
        stage_before = schema_checker.stage_a(x, ev, before_state, {}, state_spec=spec if FACT_LEVEL_ABOX else None)
        stage_gold = schema_checker.stage_a(x, ev, gold_state, {}, state_spec=spec if FACT_LEVEL_ABOX else None)
        pred_ops = predicted_operations(t, stage_before)
        pred_after = apply_state_spec(BASE, with_ops(spec, pred_ops))
        pred_state = schema_checker.schema_state(pred_after)
        stage_pred = schema_checker.stage_a(x, ev, pred_state, {}, state_spec=spec if FACT_LEVEL_ABOX else None)

        ok_before, why_before = state_available(before, spec)
        ok_gold, why_gold = state_available(gold_after, spec)
        ok_pred, why_pred = state_available(pred_after, spec)

        def run_condition(state, ok, stage, flags=None):
            if not ok:
                return abstain_obj('state_unavailable')
            return population_engine.solve(x, ev, stage, ann, md, inv, flags or {})

        raw_frozen = run_condition(before, ok_before, stage_before)
        raw_pred = run_condition(pred_after, ok_pred, stage_pred)
        raw_gold = run_condition(gold_after, ok_gold, stage_gold)
        pred_frozen = pred_object(raw_frozen)
        pred_pred = pred_object(raw_pred)
        pred_gold = pred_object(raw_gold)
        ref = {'id': y['id'], 'group': y['group'],
               'gold': {'answer': y['answer'], 'members': list(y['members']),
                        'denominator': y['denominator'], 'denominator_members': y.get('denominator_members') or []},
               'evaluation': y.get('evaluation') or {'answer': True, 'members': True, 'denominator_count': False, 'reasons': []}}
        ablation = {}
        ablation_coverage = {}
        for vname, vflags in VARIANT_FLAGS.items():
            raw_v = run_condition(pred_after, ok_pred, stage_pred, vflags)
            pv = pred_object(raw_v)
            ablation[vname] = strict_metrics.evaluate(ref, pv)
            ablation_coverage[vname] = coverage_metrics(y['members'], pv.get('members'))
        sr_frozen = strict_metrics.evaluate(ref, pred_frozen)
        sr_pred = strict_metrics.evaluate(ref, pred_pred)
        sr_gold = strict_metrics.evaluate(ref, pred_gold)
        row = {
            'id': y['id'], 'group': y['group'], 'tier': y.get('tier'),
            'trigger_gold': normalize_trigger(y.get('trigger_class')),
            'trigger_pred': normalize_trigger(stage_before.get('trigger_class')),
            'trigger_type_gold': y.get('trigger_type'),
            'trigger_type_pred': stage_before.get('trigger_type'),
            'required_element_gold': (t.get('ontology_editing') or {}).get('required_element') or '',
            'required_elements_pred': stage_before.get('required_elements') or [],
            'state_ready_status': t.get('state_ready_status'),
            'state_spec_status': t.get('state_spec_status'),
            'state_available_before': ok_before, 'state_available_pred': ok_pred, 'state_available_gold': ok_gold,
            'state_unavailable_reason_before': why_before, 'state_unavailable_reason_pred': why_pred,
            'state_unavailable_reason_gold': why_gold,
            'predicted_operations': pred_ops,
            'frozen': sr_frozen, 'predicted': sr_pred, 'gold': sr_gold,
            'pred_frozen': pred_frozen, 'pred_predicted': pred_pred, 'pred_gold': pred_gold,
            'coverage_frozen': coverage_metrics(y['members'], pred_frozen.get('members')),
            'coverage_predicted': coverage_metrics(y['members'], pred_pred.get('members')),
            'coverage_gold': coverage_metrics(y['members'], pred_gold.get('members')),
            'ablation': ablation,
            'ablation_coverage': ablation_coverage,
        }
        rows.append(row)

    all_rows = rows
    by_state = {}
    for key in ('ontology_upgrade', 'abox_repair', 'no_intervention'):
        by_state[key] = [r for r in rows if r['trigger_gold'] == key]
    by_status = defaultdict(list)
    for r in rows:
        by_status[r['state_ready_status']].append(r)

    def block(rs):
        return {'n': len(rs), 'frozen': summarize(rs, 'frozen'), 'predicted': summarize(rs, 'predicted'), 'gold': summarize(rs, 'gold'),
                'coverage': {
                    'frozen': {k: sum(r['coverage_frozen'][k] for r in rs) / len(rs) for k in ('precision', 'recall', 'f1', 'overcoverage', 'undercoverage')} if rs else {},
                    'predicted': {k: sum(r['coverage_predicted'][k] for r in rs) / len(rs) for k in ('precision', 'recall', 'f1', 'overcoverage', 'undercoverage')} if rs else {},
                    'gold': {k: sum(r['coverage_gold'][k] for r in rs) / len(rs) for k in ('precision', 'recall', 'f1', 'overcoverage', 'undercoverage')} if rs else {},
                }}

    # E1: trigger diagnosis; E2: required-element / subtype diagnostics.
    trig_rows = [r for r in rows if r['trigger_gold'] in ('ontology_upgrade', 'abox_repair', 'no_intervention')]
    trig_acc = sum(1 for r in trig_rows if r['trigger_gold'] == r['trigger_pred']) / len(trig_rows) if trig_rows else None
    cm = Counter((r['trigger_gold'], r['trigger_pred']) for r in trig_rows)
    gold_req = [r for r in rows if r.get('trigger_type_gold')]
    subtype_ok = sum(1 for r in gold_req if r.get('trigger_type_gold') and r.get('trigger_type_gold') == r.get('trigger_type_pred'))
    req_ok = 0
    req_n = 0
    for r in rows:
        req = r.get('required_element_gold') or ''
        if not req:
            continue
        req_n += 1
        pred_reqs = [str(x) for x in (r.get('required_elements_pred') or [])]
        if req in pred_reqs:
            req_ok += 1
    # E5 paired stability: predicted repair vs frozen execution.
    pre_ok = [int(bool(r['frozen'].get('strict_answer'))) for r in rows]
    post_ok = [int(bool(r['predicted'].get('strict_answer'))) for r in rows]
    restore = sum(1 for a, b in zip(pre_ok, post_ok) if not a and b)
    regress = sum(1 for a, b in zip(pre_ok, post_ok) if a and not b)
    comparable = sum(1 for a, b in zip(pre_ok, post_ok) if not (a and not b))

    result = {
        'method': 'per-task state_repair on dataset_v4_state.jsonl',
        'note': 'frozen=O_before with repair blocked; predicted=repair inferred from Stage A required elements; gold=state_spec O_after. State availability is a conservative guard, not full logical entailment.',
        'counts': {
            'n_tasks': len(rows),
            'state_spec_ready': sum(1 for r in rows if r['state_spec_status'] == 'spec_ready'),
            'state_ready_status': dict(Counter(r['state_ready_status'] for r in rows)),
            'trigger_gold': dict(Counter(r['trigger_gold'] for r in rows)),
            'trigger_pred': dict(Counter(r['trigger_pred'] for r in rows)),
        },
        'E1_expressibility_diagnosis': {
            'n': len(trig_rows), 'accuracy': trig_acc,
            'confusion': {f'{g}->{p}': n for (g, p), n in cm.items()},
            'by_gold': {g: {'n': sum(1 for r in trig_rows if r['trigger_gold'] == g),
                            'accuracy': (sum(1 for r in trig_rows if r['trigger_gold'] == g and r['trigger_pred'] == g) /
                                         max(1, sum(1 for r in trig_rows if r['trigger_gold'] == g)))}
                        for g in ('ontology_upgrade', 'abox_repair', 'no_intervention')},
        },
        'E2_state_delta': {
            'required_element_accuracy': req_ok / req_n if req_n else None,
            'required_element_n': req_n,
            'subtype_accuracy': subtype_ok / len(gold_req) if gold_req else None,
            'subtype_n': len(gold_req),
        },
        'E3_restored_computation': {
            'all': block(all_rows),
            'by_trigger': {k: block(v) for k, v in by_state.items()},
            'by_state_ready_status': {k: block(v) for k, v in by_status.items()},
        },
        'E4_coverage_change': {
            'by_trigger': {k: block(v)['coverage'] for k, v in by_state.items()},
        },
        'E6_state_repair_ablation': {
            name: {
                'n': len(rows),
                'metrics': strict_metrics.summarize([r['ablation'][name] for r in rows]),
                'coverage': {k: sum(r['ablation_coverage'][name][k] for r in rows) / len(rows) for k in ('precision', 'recall', 'f1', 'overcoverage', 'undercoverage')},
            }
            for name in VARIANT_FLAGS
        },
        'E5_replay_comparability': {
            'restoration_rate': restore / len(rows) if rows else None,
            'regression_rate': regress / len(rows) if rows else None,
            'comparability': comparable / len(rows) if rows else None,
            'pre_ok_n': sum(pre_ok), 'post_ok_n': sum(post_ok),
        },
        'rows': rows,
    }
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')

    lines = [
        '# State Repair Evaluation', '',
        'Conditions: `frozen_O` = task O_before with repair blocked; `predicted_O` = Stage A repair; `gold_O` = state_spec O_after.',
        '',
        '## Counts', '',
        f"- tasks: {len(rows)}",
        f"- state_ready_status: {dict(Counter(r['state_ready_status'] for r in rows))}",
        f"- trigger gold: {dict(Counter(r['trigger_gold'] for r in rows))}",
        f"- trigger pred: {dict(Counter(r['trigger_pred'] for r in rows))}",
        '',
        '## E1 / E2', '',
        f"- E1 trigger accuracy: {trig_acc:.3f}" if trig_acc is not None else '- E1 trigger accuracy: n/a',
        f"- E2 required-element accuracy: {req_ok / req_n:.3f}" if req_n else '- E2 required-element accuracy: n/a',
        f"- E2 subtype accuracy: {subtype_ok / len(gold_req):.3f}" if gold_req else '- E2 subtype accuracy: n/a',
        '',
        '## E3 restored computation', '',
        '| condition | exact | P macro F1 | nonempty F1 | abstain |',
        '|---|---:|---:|---:|---:|',
    ]
    for name in ('frozen', 'predicted', 'gold'):
        a = result['E3_restored_computation']['all'][name]
        lines.append(f"| {name} | {a.get('strict_answer_accuracy'):.3f} | {a.get('population_macro_f1'):.3f} | {a.get('nonempty_population_f1'):.3f} | {a.get('abstain_rate'):.3f} |")
    lines += ['', '## E4 coverage', '',
              '| condition | P | R | F1 | over | under |', '|---|---:|---:|---:|---:|---:|']
    for name in ('frozen', 'predicted', 'gold'):
        c = result['E3_restored_computation']['all']['coverage'][name]
        lines.append(f"| {name} | {c['precision']:.3f} | {c['recall']:.3f} | {c['f1']:.3f} | {c['overcoverage']:.3f} | {c['undercoverage']:.3f} |")
    lines += ['', '## E5 paired stability', '',
              f"- restoration: {result['E5_replay_comparability']['restoration_rate']:.3f}",
              f"- regression: {result['E5_replay_comparability']['regression_rate']:.3f}",
              f"- comparability: {result['E5_replay_comparability']['comparability']:.3f}"]
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'rows'}, ensure_ascii=False, indent=2)[:6000])
    print('wrote', OUT_JSON, OUT_MD)


if __name__ == '__main__':
    run()
