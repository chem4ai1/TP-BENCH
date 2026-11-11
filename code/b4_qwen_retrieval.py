"""Qwen3.8-27B retrieval-only B4 baseline on the 85-task membership subset.

Candidate documents come from TF-IDF retrieval over the corpus, not from
annotated source_docs or gold members. No ontology state is supplied.
"""
from __future__ import annotations

import json
import math
import re
import time
from collections import Counter
from pathlib import Path

from core_v3 import config, strict_metrics
from core_v3.llm_client import call_qwen

P = Path(__file__).resolve().parents[1] / 'data'
MODEL = 'Qwen3.8-27B'
OUT_JSON = P / 'baselines/b4_qwen_retrieval.json'
OUT_MD = P / 'baselines/b4_qwen_retrieval.md'

DOCS = {d['doc_id']: d for d in [json.loads(l) for l in (P / 'raw/doc_annotations.jsonl').read_text(encoding='utf-8').splitlines()]}
TASKS = [json.loads(l) for l in (P / 'tiers/dataset_v3_corrected.jsonl').read_text(encoding='utf-8').splitlines()]
S = [t for t in TASKS if t.get('group') in {'role_variant', 'model_role', 'granularity', 'granularity_pair'}
     and (t.get('evaluation') or {}).get('members')]
MD = {d: (P / 'docs' / f'{d}.md').read_text(encoding='utf-8', errors='ignore')
      if (P / 'docs' / f'{d}.md').exists()
      else (config.CORPUS_MD / d / f'{d}.md').read_text(encoding='utf-8', errors='ignore')
      for d in DOCS}


def toks(s):
    s = ''.join(re.findall(r'[\u4e00-\u9fffA-Za-z0-9]+', s))
    out = set(re.findall(r'[\u4e00-\u9fff]{2}', s))
    out |= set(re.findall(r'[A-Za-z]{2,}', s))
    out |= set(re.findall(r'\d{4}', s))
    return out


chunks = []
for d, t in MD.items():
    for i in range(0, max(1, len(t)), 500):
        c = t[i:i + 600]
        if c.strip():
            chunks.append((d, c))
chunk_tokens = [toks(c) for _, c in chunks]
df = Counter()
for ts in chunk_tokens:
    for t in ts:
        df[t] += 1
N = len(chunks)
idf = {t: math.log((N + 1) / (v + 1)) + 1 for t, v in df.items()}


def retrieve(t, k=20):
    q = t.get('question_zh') or t.get('question') or ''
    qt = toks(q)
    qn = math.sqrt(sum(idf.get(x, 1) ** 2 for x in qt)) or 1
    scores = []
    for i, (d, c) in enumerate(chunks):
        ts = chunk_tokens[i]
        dot = sum(idf.get(x, 1) for x in (qt & ts))
        tn = math.sqrt(sum(idf.get(x, 1) ** 2 for x in ts)) or 1
        scores.append((dot / (qn * tn), i))
    scores.sort(reverse=True)
    docs = [chunks[i][0] for _, i in scores[:k]]
    return sorted(set(docs))


def parse(raw):
    if not raw:
        return {}
    raw = raw.strip()
    for st in [0, raw.find('{')]:
        try:
            return json.JSONDecoder().raw_decode(raw[st:])[0]
        except Exception:
            pass
    return {}


def call(batch, candidate_map):
    items = []
    for t in batch:
        items.append({'id': t['id'], 'question': t.get('question_zh') or t.get('question'),
                      'role': (t.get('population_spec') or {}).get('role_q'),
                      'spec': (t.get('population_spec') or {}).get('C_q_pop'),
                      'unit': (t.get('population_spec') or {}).get('unit_q'),
                      'candidate_docs': candidate_map[t['id']]})
    prompt = ('你是统计型问答候选资格标注器。对每个问题，从 candidate_docs 中选出满足 PopulationSpec 的正例论文；'
              '不要选仅背景提及、仅提及模型或粗粒度类型；不能编造 ID；每题至少选一个，若确实没有才返回空；'
              '只输出 JSON：{"items":[{"id":"...","positive_docs":["..."]}]}。任务：' + json.dumps(items, ensure_ascii=False))
    status, text = call_qwen([{'role': 'system', 'content': '只输出合法 JSON。'},
                              {'role': 'user', 'content': prompt}],
                             model=MODEL, max_tokens=1800, temperature=0.0, enable_thinking=False)
    print('status', status, flush=True)
    if status != 200:
        return {}
    try:
        raw = json.loads(text)['choices'][0]['message'].get('content') or ''
    except Exception:
        return {}
    obj = parse(raw)
    return {str(x.get('id')): x for x in obj.get('items', []) if isinstance(x, dict) and x.get('id')}


def main():
    cand = {t['id']: retrieve(t, 20) for t in S}
    preds = {}
    for i in range(0, len(S), 10):
        preds.update(call(S[i:i + 10], cand))
        print('batch', i // 10 + 1, len(preds), flush=True)
        time.sleep(0.5)
    rows = []
    for t in S:
        allowed = set(cand[t['id']])
        p = set(preds.get(t['id'], {}).get('positive_docs') or []) & allowed
        g = set((t.get('gold') or {}).get('members') or [])
        tp = len(p & g)
        pr = tp / len(p) if p else 0.0
        rc = tp / len(g) if g else 0.0
        f1 = 2 * pr * rc / (pr + rc) if pr + rc else 0.0
        ref = {'id': t['id'], 'group': t['group'],
               'gold': {'answer': (t.get('gold') or {}).get('answer'), 'members': sorted(g),
                        'denominator': (t.get('gold') or {}).get('denominator'),
                        'denominator_members': (t.get('gold') or {}).get('denominator_members') or []},
               'evaluation': t.get('evaluation') or {'answer': True, 'members': True,
                                                     'denominator_count': False, 'reasons': []}}
        strict = strict_metrics.evaluate(ref, {'status': 'ok' if p else 'abstain', 'answer': len(p),
                                               'members': sorted(p), 'denominator_count': len(p)})
        rows.append({'id': t['id'], 'type': t['group'], 'p': pr, 'r': rc, 'f1': f1,
                     'candidate_docs': sorted(allowed), 'pred': sorted(p), 'gold': sorted(g), 'strict': strict})
    tp = sum(len(set(r['pred']) & set(r['gold'])) for r in rows)
    pp = sum(len(r['pred']) for r in rows)
    gg = sum(len(r['gold']) for r in rows)
    pr = tp / pp if pp else 0
    rc = tp / gg if gg else 0
    f1 = 2 * pr * rc / (pr + rc) if pr + rc else 0
    summary = {'model': MODEL, 'tasks': len(S), 'candidate_source': 'TF-IDF top-20 chunks',
               'precision': pr, 'recall': rc, 'f1': f1,
               'strict': strict_metrics.summarize([r['strict'] for r in rows])}
    OUT_JSON.write_text(json.dumps({'summary': summary, 'rows': rows}, ensure_ascii=False, indent=2), encoding='utf-8')
    lines = ['# B4 Qwen retrieval-only on 85 membership tasks', '',
             f"P={pr:.3f}, R={rc:.3f}, F1={f1:.3f}; exact={summary['strict']['strict_answer_accuracy']:.3f}, "
             f"macro-F1={summary['strict']['population_macro_f1']:.3f}.", '',
             '| ID | type | P | R | F1 | candidates | pred | gold |', '|---|---|---:|---:|---:|---:|---:|---:|']
    for r in rows:
        lines.append(f"| {r['id']} | {r['type']} | {r['p']:.2f} | {r['r']:.2f} | {r['f1']:.2f} | "
                     f"{len(r['candidate_docs'])} | {len(r['pred'])} | {len(r['gold'])} |")
    OUT_MD.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print('wrote', OUT_JSON, OUT_MD)


if __name__ == '__main__':
    main()
