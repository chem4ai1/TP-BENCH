"""Qwen3.8-27B test: with ontology state vs without ontology definitions.

The same local model and task set are used in both conditions. Gold fields are
not included in either prompt. The no-ontology condition receives only the
question and evidence; the with-ontology condition additionally receives the
population specification, pre-state relation summary, and relation registry.
"""
from __future__ import annotations

import argparse
import json
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from threading import Lock

from core_v3.llm_client import call_qwen, extract_json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
ANN = DATA / 'annotation'
OUT = DATA / 'results_v4/qwen_ontology_ablation_v5'
OUT.mkdir(parents=True, exist_ok=True)
DATASET = DATA / 'tiers/dataset_v4_state.jsonl'
D = {t['id']: t for t in [json.loads(l) for l in DATASET.read_text(encoding='utf-8').splitlines() if l.strip()]}
MODEL = 'Qwen3.8-27B'
TRIGGERS = {'ontology_upgrade', 'abox_repair', 'no_intervention'}
SCHEMA = {
    'trigger_class': 'ontology_upgrade | abox_repair | no_intervention',
    'trigger_type': 'role_schema_missing | relation_missing | abox_incomplete | alias_gap | class_missing | definition_gap | proposal_gap | none',
    'required_elements': ['only missing or fact-backfilled element names'],
    'repair_operations': [{'op': 'add_relation|add_abox_relation|add_class|add_alias_link|none',
                           'id': 'relation/class id', 'subject': 'optional', 'object': 'optional'}],
    'closed_world_scope': ['relations needed by the predicate'],
    'rationale': 'short explanation',
}
SYSTEM = (
    '你是独立语义标注员。给定问题、证据，以及可选的当前本体状态，判断目标总体在当前状态下是否可表达，'
    '并给出最小状态修复。只输出一个 JSON 对象，不要 markdown。\n'
    'trigger_class 只能取：no_intervention, abox_repair, ontology_upgrade。\n'
    '判定规则：\n'
    '1. no_intervention：问题所需关系/类在当前状态可用且相关 ABox 事实为正。\n'
    '2. abox_repair：关系/类可用，但相关 ABox 事实为零或缺失；回填事实即可。\n'
    '3. ontology_upgrade：所需关系/类/角色关系不在当前状态，或问题要求角色区分而角色关系缺失。\n'
    '4. 角色词“研究站点/观测来源/背景提及/实际采用/仅提及”需要对应角色关系；角色关系缺失时判 ontology_upgrade。\n'
    '5. 论文-变量使用优先用 reports_variable；存在近义关系时不要发明 uses_variable。\n'
    '6. required_elements 只列需要补充或回填的元素；no_intervention 必须返回 []。\n'
    '7. “实际采用”且有 applies_model 正事实时，不需要额外角色关系；“背景提及/仅提及”且 lacks hasModelRole 时需要 ontology_upgrade。\n'
    '8. 若提供 missing_relations / zero_abox_relations，只对与问题成员谓词相关的关系使用它们：相关关系在 missing_relations 中判 ontology_upgrade，在 zero_abox_relations 中判 abox_repair，二者都不相关才判 no_intervention。\n'
    '9. 不要假设 gold answer 或 gold members；它们不会提供。\n'
    'SCHEMA:\n' + json.dumps(SCHEMA, ensure_ascii=False)
)
LOCK = Lock()
ROWS = OUT / 'qwen_ontology_ablation_rows.jsonl'
ERRORS = OUT / 'qwen_ontology_ablation_errors.jsonl'


def valid(x):
    return isinstance(x, dict) and x.get('trigger_class') in TRIGGERS


def norm_gold(v):
    return 'no_intervention' if v in ('verified', 'none', None) else v


def required_set(x):
    return set(str(v) for v in (x.get('required_elements') or [])) if valid(x) else set()


def call_once(item, condition, attempt):
    if condition == 'with_ontology':
        payload = {k: v for k, v in item.items() if k not in ('status', 'model')}
        payload = json.loads(json.dumps(payload, ensure_ascii=False))
        pre = payload.get('pre_state') or {}
        registry = {r.get('id') for r in (payload.get('ontology_relation_registry') or []) if r.get('id')}
        available = set(pre.get('available_relations') or [])
        counts = pre.get('abox_counts') or {}
        pre['missing_relations'] = sorted(registry - available)
        pre['zero_abox_relations'] = sorted([r for r in available if counts.get(r, 0) == 0])
        payload['pre_state'] = pre
        prefix = 'CONDITION=WITH_ONTOLOGY. pre_state.missing_relations 和 pre_state.zero_abox_relations 已由当前状态计算，可直接用于判定相关关系。\n'
    else:
        payload = {k: item[k] for k in ('task_id', 'question', 'source_docs', 'evidence') if k in item}
        prefix = 'CONDITION=WITHOUT_ONTOLOGY. 当前不提供本体状态、关系注册表或 population_spec；只根据问题与证据判断。\n'
    messages = [{'role': 'system', 'content': SYSTEM},
                {'role': 'user', 'content': prefix + 'TASK:\n' + json.dumps(payload, ensure_ascii=False)}]
    status, text = call_qwen(messages, model=MODEL, max_tokens=900, temperature=0.0, enable_thinking=False)
    content = ''
    usage = {}
    parsed = None
    try:
        p = json.loads(text)
        ch = (p.get('choices') or [{}])[0]
        content = ((ch.get('message') or {}).get('content') or '')
        usage = p.get('usage') or {}
        parsed = extract_json(content)
    except Exception:
        pass
    return {'condition': condition, 'http_status': status, 'content': content, 'parsed': parsed,
            'usage': usage, 'attempt': attempt + 1}


def run_task(item, condition):
    last = None
    for attempt in range(2):
        last = call_once(item, condition, attempt)
        if valid(last.get('parsed')):
            return last
        time.sleep(1)
    return last


def process(item):
    return {'task_id': item['task_id'],
            'with_ontology': run_task(item, 'with_ontology'),
            'without_ontology': run_task(item, 'without_ontology')}


def score(rows, condition):
    n = len(rows)
    preds = [r[condition].get('parsed') if valid(r[condition].get('parsed')) else None for r in rows]
    correct = 0
    gold_req_n = 0
    gold_req_ok = 0
    by = defaultdict(list)
    for t, p in zip(rows, preds):
        gold = (D[t['task_id']].get('ontology_editing') or {}).get('trigger_class') or 'none'
        gold_norm = norm_gold(gold)
        ok = p is not None and p.get('trigger_class') == gold_norm
        correct += int(ok)
        by[gold_norm].append(int(ok))
        req = (D[t['task_id']].get('ontology_editing') or {}).get('required_element') or ''
        if req:
            gold_req_n += 1
            gold_req_ok += int(p is not None and req in required_set(p))
    return {
        'n': n,
        'parse_rate': sum(1 for p in preds if p is not None) / n if n else None,
        'trigger_accuracy': correct / n if n else None,
        'gold_required_match': gold_req_ok / gold_req_n if gold_req_n else None,
        'by_gold': {k: {'n': len(v), 'trigger_accuracy': sum(v) / len(v)} for k, v in by.items()},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--workers', type=int, default=4)
    args = ap.parse_args()
    q = [json.loads(l) for l in (ANN / 'llm_a_queue.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
    done, rows = set(), []
    if ROWS.exists():
        for line in ROWS.read_text(encoding='utf-8').splitlines():
            if line.strip():
                r = json.loads(line)
                if r.get('with_ontology') and r.get('without_ontology'):
                    rows.append(r); done.add(r['task_id'])
    pending = [x for x in q if x['task_id'] not in done]
    print(f'total={len(q)} done={len(done)} pending={len(pending)} model={MODEL}', flush=True)
    start = time.time()
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as ex:
        futs = {ex.submit(process, item): item for item in pending}
        for i, fut in enumerate(as_completed(futs), 1):
            item = futs[fut]
            try:
                r = fut.result()
                with LOCK:
                    with ROWS.open('a', encoding='utf-8') as f:
                        f.write(json.dumps(r, ensure_ascii=False) + '\n')
                    rows.append(r); done.add(r['task_id'])
                print(f'[{i}/{len(pending)}] {r["task_id"]} with={valid(r["with_ontology"].get("parsed"))} without={valid(r["without_ontology"].get("parsed"))}', flush=True)
            except Exception as e:
                with LOCK:
                    with ERRORS.open('a', encoding='utf-8') as f:
                        f.write(json.dumps({'task_id': item['task_id'], 'error': repr(e)}, ensure_ascii=False) + '\n')
                print('ERROR', item['task_id'], repr(e), flush=True)
    order = {tid: i for i, tid in enumerate(D)}
    rows.sort(key=lambda r: order.get(r['task_id'], 9999))
    summary = {
        'model': MODEL,
        'n_tasks': len(rows),
        'n_calls': len(rows) * 2,
        'elapsed_s': round(time.time() - start, 1),
        'with_ontology': score(rows, 'with_ontology'),
        'without_ontology': score(rows, 'without_ontology'),
        'wins': {},
    }
    for a, b in [('with_ontology', 'without_ontology')]:
        wins = 0; losses = 0; both = 0; neither = 0
        for r in rows:
            t = D[r['task_id']]
            gold = norm_gold((t.get('ontology_editing') or {}).get('trigger_class') or 'none')
            pa = r[a].get('parsed') if valid(r[a].get('parsed')) else None
            pb = r[b].get('parsed') if valid(r[b].get('parsed')) else None
            ca = pa is not None and pa.get('trigger_class') == gold
            cb = pb is not None and pb.get('trigger_class') == gold
            if ca and cb: both += 1
            elif ca: wins += 1
            elif cb: losses += 1
            else: neither += 1
        summary['wins'][a + '_vs_' + b] = {'with_only': wins, 'without_only': losses, 'both': both, 'neither': neither}
    (OUT / 'qwen_ontology_ablation.json').write_text(json.dumps({'summary': summary, 'rows': rows}, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = ['# Qwen3.8-27B: With vs Without Ontology', '',
             f"Model: `{MODEL}`; tasks: {summary['n_tasks']}; calls: {summary['n_calls']}; elapsed: {summary['elapsed_s']}s.", '',
             '| Condition | parse rate | trigger accuracy | gold required match |', '|---|---:|---:|---:|']
    for c in ('with_ontology', 'without_ontology'):
        s = summary[c]
        lines.append(f"| {c} | {s['parse_rate']:.3f} | {s['trigger_accuracy']:.3f} | {s['gold_required_match']:.3f} |")
    lines += ['', '| Gold trigger | n | with ontology | without ontology |', '|---|---:|---:|---:|']
    keys = sorted(set(summary['with_ontology']['by_gold']) | set(summary['without_ontology']['by_gold']))
    for k in keys:
        a = summary['with_ontology']['by_gold'].get(k, {'trigger_accuracy': 0})
        b = summary['without_ontology']['by_gold'].get(k, {'trigger_accuracy': 0})
        lines.append(f"| {k} | {a.get('n', b.get('n', 0))} | {a['trigger_accuracy']:.3f} | {b['trigger_accuracy']:.3f} |")
    (OUT / 'qwen_ontology_ablation.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print('wrote', OUT / 'qwen_ontology_ablation.json')


if __name__ == '__main__':
    main()
