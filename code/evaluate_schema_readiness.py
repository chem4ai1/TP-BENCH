"""Compare question-only, rule+spec, and state-blind readiness checkers."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from core_v3 import data_loader, evidence_builder, object_inventory, schema_checker
from core_v3.state_builder import apply_state_spec

import evaluate_state_repair as esr

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
OUT = DATA / 'results_v4/schema_readiness'
OUT.mkdir(parents=True, exist_ok=True)
BASE = esr.BASE
DATASET = DATA / 'tiers/dataset_v4_state.jsonl'


def norm(v):
    return esr.normalize_trigger(v)


def eval_preds(tasks, ann, md, sortie):
    rows = []
    for t in tasks:
        x, y = data_loader.split_task(t)
        ev = evidence_builder.build_evidence(x, object_inventory.build_inventory(ann), ann, md)
        spec = t['state_spec']
        before = schema_checker.schema_state(apply_state_spec(BASE, esr.with_ops(spec, [])))
        if sortie == 'question_only':
            xx = dict(x); xx['population_spec'] = {}
            stage = schema_checker.stage_a(xx, ev, before, {})
        elif sortie == 'rule_plus_spec':
            stage = schema_checker.stage_a(x, ev, before, {})
        elif sortie == 'state_blind':
            stage = schema_checker.stage_a(x, ev, schema_checker.schema_state(BASE), {})
        elif sortie == 'no_audit':
            stage = schema_checker.stage_a(x, ev, before, {'schema_audit_enabled': False})
        else:
            raise ValueError(sortie)
        gold = norm(y.get('trigger_class'))
        pred = norm(stage.get('trigger_class'))
        reqs = stage.get('required_elements') or []
        req = (t.get('ontology_editing') or {}).get('required_element') or ''
        rows.append({'id': y['id'], 'gold': gold, 'pred': pred, 'gold_type': y.get('trigger_type') or '',
                     'pred_type': stage.get('trigger_type') or '', 'req': req, 'reqs': reqs})
    return rows


def score(rows):
    tp = sum(1 for r in rows if r['gold'] == 'abox_repair' and r['pred'] == 'abox_repair')
    fp = sum(1 for r in rows if r['gold'] != 'abox_repair' and r['pred'] == 'abox_repair')
    fn = sum(1 for r in rows if r['gold'] == 'abox_repair' and r['pred'] != 'abox_repair')
    nochange = [r for r in rows if r['gold'] == 'no_intervention']
    false_intervention = sum(1 for r in nochange if r['pred'] != 'no_intervention')
    req_n = [r for r in rows if r['req']]
    sub_n = [r for r in rows if r['gold_type']]
    return {
        'n': len(rows),
        'accuracy': sum(1 for r in rows if r['gold'] == r['pred']) / len(rows),
        'abox_precision': tp / (tp + fp) if tp + fp else None,
        'abox_recall': tp / (tp + fn) if tp + fn else None,
        'abox_tp': tp, 'abox_fp': fp, 'abox_fn': fn,
        'false_intervention_rate': false_intervention / len(nochange) if nochange else None,
        'required_element_accuracy': sum(1 for r in req_n if r['req'] in r['reqs']) / len(req_n) if req_n else None,
        'subtype_accuracy': sum(1 for r in sub_n if r['gold_type'] == r['pred_type']) / len(sub_n) if sub_n else None,
        'confusion': {f'{g}->{p}': n for (g, p), n in Counter((r['gold'], r['pred']) for r in rows).items()},
    }


def main():
    ann, md, _, _ = data_loader.load_resources()
    tasks = [json.loads(l) for l in DATASET.read_text(encoding='utf-8').splitlines() if l.strip()]
    result = {'n_tasks': len(tasks), 'variants': {}}
    for variant in ('question_only', 'rule_plus_spec', 'state_blind', 'no_audit'):
        result['variants'][variant] = score(eval_preds(tasks, ann, md, variant))
    (OUT / 'schema_readiness_results.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = ['# Schema Readiness Mechanism Comparison', '',
             '| Checker | exact | abox P | abox R | false intervention | required element | subtype |',
             '|---|---:|---:|---:|---:|---:|---:|']
    for k, v in result['variants'].items():
        def f(x):
            return '--' if x is None else f'{x:.3f}'
        lines.append(f"| {k} | {f(v['accuracy'])} | {f(v['abox_precision'])} | {f(v['abox_recall'])} | {f(v['false_intervention_rate'])} | {f(v['required_element_accuracy'])} | {f(v['subtype_accuracy'])} |")
    (OUT / 'schema_readiness_results.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
