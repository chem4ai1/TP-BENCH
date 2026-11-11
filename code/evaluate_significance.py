"""Bootstrap confidence intervals and paired McNemar tests for state repair."""
from __future__ import annotations

import json
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
SRC = DATA / 'results_v4/state_repair/state_repair_results.json'
OUT = DATA / 'results_v4/state_repair/significance.json'
OUT_MD = DATA / 'results_v4/state_repair/significance.md'
RNG = random.Random(17)


def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def bootstrap_mean(values, n=3000):
    vals = [v for v in values if v is not None]
    if not vals:
        return {'mean': None, 'lo': None, 'hi': None, 'n': 0}
    means = []
    for _ in range(n):
        sample = [vals[RNG.randrange(len(vals))] for _ in vals]
        means.append(sum(sample) / len(sample))
    means.sort()
    return {'mean': sum(vals) / len(vals), 'lo': means[int(0.025 * n)], 'hi': means[int(0.975 * n) - 1], 'n': len(vals)}


def exact_ci(rows, key):
    vals = []
    for r in rows:
        v = r.get(key, {}).get('strict_answer')
        if v is not None:
            vals.append(v)
    return bootstrap_mean(vals)


def f1_ci(rows, key):
    vals = []
    for r in rows:
        x = r.get(key, {}).get('population')
        vals.append(x.get('f1') if x else None)
    return bootstrap_mean(vals)


def coverage_ci(rows, key):
    vals = [r.get(key, {}).get('f1') for r in rows]
    return bootstrap_mean(vals)


def mcnemar(rows, a_key, b_key):
    b = c = 0
    n = 0
    for r in rows:
        a = r.get(a_key, {}).get('strict_answer')
        z = r.get(b_key, {}).get('strict_answer')
        if a is None or z is None:
            continue
        n += 1
        a, z = int(bool(a)), int(bool(z))
        if a and not z:
            b += 1
        elif not a and z:
            c += 1
    if b + c == 0:
        return {'n': n, 'a_correct_b_wrong': b, 'a_wrong_b_correct': c, 'p_value': 1.0}
    k = min(b, c)
    tail = sum(math.comb(b + c, i) for i in range(k + 1)) / (2 ** (b + c))
    p = min(1.0, 2 * tail)
    return {'n': n, 'a_correct_b_wrong': b, 'a_wrong_b_correct': c, 'p_value': p}


def main():
    sr = json.loads(SRC.read_text(encoding='utf-8'))
    rows = sr['rows']
    out = {
        'n_tasks': len(rows),
        'exact': {}, 'population_macro_f1': {}, 'coverage_f1': {},
        'mcnemar': {},
    }
    for key in ('frozen', 'predicted', 'gold'):
        out['exact'][key] = exact_ci(rows, key)
        out['population_macro_f1'][key] = f1_ci(rows, key)
        out['coverage_f1'][key] = coverage_ci(rows, f'coverage_{key}')
    for a, b in [('frozen', 'predicted'), ('frozen', 'gold'), ('gold', 'predicted')]:
        out['mcnemar'][f'{a}_vs_{b}'] = mcnemar(rows, a, b)
    for name in ('no_auditor', 'no_role', 'no_granularity', 'no_denominator', 'no_replay'):
        out['mcnemar'][f'full_vs_{name}'] = mcnemar(rows, 'predicted', f'ablation:{name}')
        # The ablation rows use a nested key; compute directly.
    # Recompute ablation comparisons against the nested ablation rows.
    for name in ('no_auditor', 'no_role', 'no_granularity', 'no_denominator', 'no_replay'):
        bb = cc = nn = 0
        for r in rows:
            a = r['predicted'].get('strict_answer')
            z = r['ablation'][name].get('strict_answer')
            if a is None or z is None:
                continue
            nn += 1
            a, z = int(bool(a)), int(bool(z))
            if a and not z:
                bb += 1
            elif not a and z:
                cc += 1
        if bb + cc == 0:
            p = 1.0
        else:
            k = min(bb, cc)
            p = min(1.0, 2 * sum(math.comb(bb + cc, i) for i in range(k + 1)) / (2 ** (bb + cc)))
        out['mcnemar'][f'full_vs_{name}'] = {'n': nn, 'a_correct_b_wrong': bb, 'a_wrong_b_correct': cc, 'p_value': p}

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = ['# State Repair Significance', '', 'Bootstrap 95% CI (3000 resamples) and paired McNemar exact tests.', '',
             '| metric | mean | 95% CI | n |', '|---|---:|---|---:|']
    for group in ('exact', 'population_macro_f1', 'coverage_f1'):
        for key in ('frozen', 'predicted', 'gold'):
            v = out[group][key]
            lines.append(f"| {group} / {key} | {v['mean']:.3f} | [{v['lo']:.3f}, {v['hi']:.3f}] | {v['n']} |")
    lines += ['', '## McNemar', '', '| comparison | n | A correct / B wrong | A wrong / B correct | p |', '|---|---:|---:|---:|---:|']
    for k, v in out['mcnemar'].items():
        lines.append(f"| {k} | {v['n']} | {v['a_correct_b_wrong']} | {v['a_wrong_b_correct']} | {v['p_value']:.4g} |")
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
