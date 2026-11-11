"""Compare relation-level and fact-level ABox repair decisions."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from core_v3 import data_loader, evidence_builder, object_inventory, population_engine, schema_checker, strict_metrics
from core_v3.state_builder import apply_state_spec

import evaluate_state_repair as esr

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
OUT = DATA / 'results_v4/fact_level_abox'
OUT.mkdir(parents=True, exist_ok=True)
TRIGGERS = ('ontology_upgrade', 'abox_repair', 'no_intervention')


def norm(v):
    return 'no_intervention' if v in ('verified', 'none', None) else v


def pred_obj(pred):
    return esr.pred_object(pred)


def evaluate_condition(t, x, y, ev, spec, stage, ann, md, inv):
    ops = esr.predicted_operations(t, stage)
    after = apply_state_spec(esr.BASE, esr.with_ops(spec, ops))
    ok, why = esr.state_available(after, spec)
    if not ok:
        raw = esr.abstain_obj('state_unavailable')
    else:
        stage_after = schema_checker.stage_a(x, ev, schema_checker.schema_state(after), {}, state_spec=spec)
        raw = population_engine.solve(x, ev, stage_after, ann, md, inv, {})
    ref = {'id': y['id'], 'group': y['group'],
           'gold': {'answer': y['answer'], 'members': list(y['members']),
                    'denominator': y.get('denominator'),
                    'denominator_members': y.get('denominator_members') or []},
           'evaluation': t.get('evaluation') or {'answer': True, 'members': True,
                                                 'denominator_count': False, 'reasons': []}}
    return strict_metrics.evaluate(ref, pred_obj(raw)), ops, why


def main():
    ann, md, _, _ = data_loader.load_resources()
    inv = object_inventory.build_inventory(ann)
    tasks = [json.loads(l) for l in esr.DATASET.read_text(encoding='utf-8').splitlines() if l.strip()]
    rows = []
    for t in tasks:
        x, y = data_loader.split_task(t)
        ev = evidence_builder.build_evidence(x, inv, ann, md)
        spec = t.get('state_spec') or {}
        before = apply_state_spec(esr.BASE, esr.with_ops(spec, []))
        before_state = schema_checker.schema_state(before)
        stage_relation = schema_checker.stage_a(x, ev, before_state, {})
        stage_fact = schema_checker.stage_a(x, ev, before_state, {}, state_spec=spec)
        gold = norm((t.get('ontology_editing') or {}).get('trigger_class'))
        req_gold = (t.get('ontology_editing') or {}).get('required_element') or ''
        rec = {'id': t['id'], 'group': t.get('group'), 'trigger_gold': gold,
               'required_element_gold': req_gold,
               'trigger_relation': norm(stage_relation.get('trigger_class')),
               'trigger_fact': norm(stage_fact.get('trigger_class')),
               'required_relation': stage_relation.get('required_elements') or [],
               'required_fact': stage_fact.get('required_elements') or [],
               'fact_level': stage_fact.get('fact_level') or {}}
        for label, stage in [('relation', stage_relation), ('fact', stage_fact)]:
            strict, ops, why = evaluate_condition(t, x, y, ev, spec, stage, ann, md, inv)
            rec[label] = {'strict': strict, 'ops': ops, 'why': why}
        rows.append(rec)

    def acc(rs, key):
        return sum(1 for r in rs if r['trigger_' + key] == r['trigger_gold']) / len(rs) if rs else 0.0

    def req_acc(rs, key):
        rr = [r for r in rs if r['required_element_gold']]
        return sum(1 for r in rr if r['required_element_gold'] in r['required_' + key]) / len(rr) if rr else 0.0

    def exact(rs, key, group=None):
        rr = [r for r in rs if group is None or r['group'] == group]
        return sum(1 for r in rr if r[key]['strict'].get('strict_answer')) / len(rr) if rr else 0.0

    by_gold = {}
    for g in TRIGGERS:
        rs = [r for r in rows if r['trigger_gold'] == g]
        by_gold[g] = {
            'n': len(rs),
            'relation_acc': acc(rs, 'relation'),
            'fact_acc': acc(rs, 'fact'),
            'relation_exact': exact(rs, 'relation'),
            'fact_exact': exact(rs, 'fact'),
        }
    result = {
        'method': 'relation-level vs fact-level ABox recovery; state_spec fact_ids/evidence_hashes',
        'n': len(rows),
        'overall': {
            'relation_trigger_acc': acc(rows, 'relation'),
            'fact_trigger_acc': acc(rows, 'fact'),
            'relation_required_acc': req_acc(rows, 'relation'),
            'fact_required_acc': req_acc(rows, 'fact'),
            'relation_exact': exact(rows, 'relation'),
            'fact_exact': exact(rows, 'fact'),
        },
        'by_gold': by_gold,
        'abox_fact_level': {
            'n_with_missing': sum(1 for r in rows if (r['fact_level'].get('missing_facts') or [])),
            'n_with_evidence_mismatch': sum(1 for r in rows if (r['fact_level'].get('evidence_mismatch') or [])),
        },
        'rows': rows,
    }
    (OUT / 'fact_level_abox.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = ['# Fact-level ABox recovery', '',
             result['method'], '',
             '| Metric | Relation-level | Fact-level |', '|---|---:|---:|',
             f"| trigger accuracy | {result['overall']['relation_trigger_acc']:.3f} | {result['overall']['fact_trigger_acc']:.3f} |",
             f"| required-element accuracy | {result['overall']['relation_required_acc']:.3f} | {result['overall']['fact_required_acc']:.3f} |",
             f"| predicted exact | {result['overall']['relation_exact']:.3f} | {result['overall']['fact_exact']:.3f} |",
             '', '## By gold trigger', '',
             '| Gold | n | relation trigger | fact trigger | relation exact | fact exact |',
             '|---|---:|---:|---:|---:|---:|']
    for g, v in by_gold.items():
        lines.append(f"| {g} | {v['n']} | {v['relation_acc']:.3f} | {v['fact_acc']:.3f} | {v['relation_exact']:.3f} | {v['fact_exact']:.3f} |")
    lines += ['', f"Missing-fact tasks: {result['abox_fact_level']['n_with_missing']}",
              f"Evidence-mismatch tasks: {result['abox_fact_level']['n_with_evidence_mismatch']}"]
    (OUT / 'fact_level_abox.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(result['overall'], ensure_ascii=False, indent=2))
    print(json.dumps(result['by_gold'], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
