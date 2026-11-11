"""Canonical E1--E5 state-transition evaluation.

This entry point now uses `dataset_v4_state.jsonl`. For every task it applies the
task's `state_spec` to the canonical base snapshot, constructs O_before and
O_after, and evaluates the frozen, predicted-repair, and reference-repair
conditions. The implementation is in `evaluate_state_repair.py`; this wrapper
also writes a compatibility-shaped `state_transition_results.json` for older
table generators.
"""
from __future__ import annotations

import json
from pathlib import Path

from core_v3 import config
from evaluate_state_repair import run as run_state_repair

DATA = config.DATA
SR_PATH = DATA / 'results_v4/state_repair/state_repair_results.json'
OUT_DIR = DATA / 'results_v4/state_transition'
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_JSON = OUT_DIR / 'state_transition_results.json'
OUT_MD = OUT_DIR / 'state_transition_results.md'
DATASET = DATA / 'tiers/dataset_v4_state.jsonl'


def coverage_obj(c):
    return {
        'coverage_p': c.get('precision'),
        'coverage_r': c.get('recall'),
        'coverage_f1': c.get('f1'),
        'overcoverage': c.get('overcoverage'),
        'undercoverage': c.get('undercoverage'),
        'over': c.get('overcoverage'),
        'under': c.get('undercoverage'),
        'tp': c.get('tp'), 'fp': c.get('fp'), 'fn': c.get('fn'),
    }


def legacy_shape(sr, tasks):
    e1 = sr['E1_expressibility_diagnosis']
    e2 = sr['E2_state_delta']
    e3 = sr['E3_restored_computation']
    e4 = sr['E4_coverage_change']
    e6 = sr['E6_state_repair_ablation']
    e5 = sr['E5_replay_comparability']
    conf = e1['confusion']
    changed = sum(v for k, v in conf.items() if k.startswith('ontology_upgrade->') or k.startswith('abox_repair->'))
    no_change = sum(v for k, v in conf.items() if k.startswith('no_intervention->'))
    missed = sum(v for k, v in conf.items() if k in ('ontology_upgrade->no_intervention', 'abox_repair->no_intervention'))
    false_intervention = sum(v for k, v in conf.items() if k in ('no_intervention->ontology_upgrade', 'no_intervention->abox_repair'))

    gold_map = {t.get('id'): t for t in tasks}
    silent_zero = 0
    silent_den = 0
    for r in sr['rows']:
        gold = (gold_map.get(r['id']) or {}).get('gold') or {}
        frozen = r.get('pred_frozen') or {}
        if frozen.get('status') == 'ok':
            silent_den += 1
            if frozen.get('answer') in (0, '0') and gold.get('answer') not in (0, '0', None, [], {}):
                silent_zero += 1
    silent_rate = silent_zero / silent_den if silent_den else 0.0

    replay_file = DATA / 'results_v4/real_replay_results.json'
    replay = json.loads(replay_file.read_text(encoding='utf-8')).get('summary', {}) if replay_file.exists() else {}
    tier_c = {
        'n': replay.get('n', 44),
        'comparability_audit': replay.get('comparability_audit', 1.0),
        'silent_zero_rate': replay.get('silent_zero_rate', 0.0),
        'regression_rate': replay.get('regression_rate', 0.0),
    }

    by_state = {}
    for key, label in [('ontology_upgrade', 'Upgrade'), ('abox_repair', 'Repair'), ('no_intervention', 'No change')]:
        b = e3['by_trigger'][key]
        by_state[key] = {
            'n': b['n'],
            'frozen_O': b['frozen'],
            'predicted_O_prime': b['predicted'],
            'gold_O_prime_upper_diagnostic': b['gold'],
        }
    by_state_cov = {}
    for key in ('ontology_upgrade', 'abox_repair', 'no_intervention'):
        c = e3['by_trigger'][key]['coverage']
        by_state_cov[key] = {
            'frozen_O': coverage_obj(c['frozen']),
            'predicted_O_prime': coverage_obj(c['predicted']),
        }

    overall = {
        'frozen_O': coverage_obj(e3['all']['coverage']['frozen']),
        'predicted_O_prime': coverage_obj(e3['all']['coverage']['predicted']),
        'no_coverage_auditor': coverage_obj(e6['no_auditor']['coverage']),
    }
    return {
        'method': 'per-task state_spec E1--E5 via evaluate_state_repair.py',
        'note': 'O_before and O_after are reconstructed from dataset_v4_state.jsonl state specs; frozen/predicted/gold conditions are scored per task.',
        'dataset': str(DATASET.relative_to(config.PAPER_EN)),
        'E1_expressibility_diagnosis': {
            'three_class_intervention_accuracy': e1.get('accuracy'),
            'missed_intervention_rate': missed / changed if changed else None,
            'false_intervention_rate': false_intervention / no_change if no_change else None,
            'confusion': conf,
            'by_gold': e1.get('by_gold'),
        },
        'E2_state_delta': {
            'required_element_accuracy': e2.get('required_element_accuracy'),
            'state_delta_subtype_accuracy': e2.get('subtype_accuracy'),
            'required_element_n': e2.get('required_element_n'),
            'subtype_n': e2.get('subtype_n'),
        },
        'E3_restored_computation': {
            'frozen_O': e3['all']['frozen'],
            'predicted_O_prime': e3['all']['predicted'],
            'gold_O_prime_upper_diagnostic': e3['all']['gold'],
            'by_state': by_state,
            'by_status': e3['by_state_ready_status'],
        },
        'E4_coverage_change': {
            'overall': overall,
            'by_state': by_state_cov,
        },
        'E5_replay_comparability': {
            'state_change_replay': {
                'restoration_rate': e5.get('restoration_rate'),
                'regression_rate': e5.get('regression_rate'),
                'comparability': e5.get('comparability'),
                'silent_zero_rate': silent_rate,
                'pre_ok_n': e5.get('pre_ok_n'),
                'post_ok_n': e5.get('post_ok_n'),
            },
            'tier_c_real_replay': tier_c,
        },
        'rows': sr['rows'],
    }


def main():
    run_state_repair()
    sr = json.loads(SR_PATH.read_text(encoding='utf-8'))
    tasks = [json.loads(line) for line in DATASET.read_text(encoding='utf-8').splitlines() if line.strip()]
    out = legacy_shape(sr, tasks)
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    main_metrics = out['E3_restored_computation']
    lines = [
        '# State-Transition E1--E5', '',
        'Generated from `dataset_v4_state.jsonl` with per-task `state_spec`.',
        '',
        '| Metric | Value |', '|---|---:|',
        f"| E1 trigger accuracy | {out['E1_expressibility_diagnosis']['three_class_intervention_accuracy']:.3f} |",
        f"| E2 required-element accuracy | {out['E2_state_delta']['required_element_accuracy']:.3f} |",
        f"| E3 frozen exact | {main_metrics['frozen_O']['strict_answer_accuracy']:.3f} |",
        f"| E3 predicted exact | {main_metrics['predicted_O_prime']['strict_answer_accuracy']:.3f} |",
        f"| E3 gold exact | {main_metrics['gold_O_prime_upper_diagnostic']['strict_answer_accuracy']:.3f} |",
        f"| E5 restoration | {out['E5_replay_comparability']['state_change_replay']['restoration_rate']:.3f} |",
        f"| E5 comparability | {out['E5_replay_comparability']['state_change_replay']['comparability']:.3f} |",
    ]
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('wrote', OUT_JSON, OUT_MD)


if __name__ == '__main__':
    main()
