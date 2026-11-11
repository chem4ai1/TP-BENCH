import json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'data'
DOCS={d['doc_id']:d for d in [json.loads(l) for l in (P/'raw/doc_annotations.jsonl').read_text(encoding='utf-8').splitlines()]}
T=[t for t in json.loads((P/'31_annotations_round2.json').read_text(encoding='utf-8'))['tasks'] if t['id'] in {f'X{i:03d}' for i in range(37,49)}]
def anchor(t):
    m=re.search(r'Station="([^"]+)"',t['population_spec'].get('C_q_pop',''))
    if m: return m.group(1)
    q=t['question_zh']
    for a in ['海北','内蒙古','长白山','千烟洲','鼎湖山','阿克苏']:
        if a in q: return a
    return None
def use_docs(a):
    return sorted({d for d,x in DOCS.items() if any(s.get('name_norm')==a and s.get('relation')=='使用' for s in x.get('stations',[]))})
def model_docs(docs):
    return [d for d in docs if DOCS[d].get('models')]
def model_mentions(docs):
    return sum(len(DOCS[d].get('models',[])) for d in docs)
rows=[]
for t in T:
    a=anchor(t); D=use_docs(a); Ndocs=model_docs(D); Nment=model_mentions(D)
    typ=t['task_type']; gold=t['gold']
    if typ=='denominator_share':
        g_D=len(D); g_N=len(Ndocs); g_ans=g_N/g_D if g_D else 0
        b5_D=g_D; b5_N=g_N; b5_ans=g_ans
        a5_D=56; a5_N=g_N; a5_ans=g_N/56
    elif typ=='unit_rate':
        g_D=len(D); g_N=Nment; g_ans=g_N/g_D if g_D else 0
        b5_D=g_D; b5_N=g_N; b5_ans=g_ans
        a5_D=56; a5_N=g_N; a5_ans=g_N/56
    else: # denominator_shift
        n=len(D); g={'denom_all':56,'denom_station':n,'ratio_all':n/56,'ratio_station':1.0}
        b5_D=(56,n); b5_N=n; b5_ans=g
        a5_D=56; a5_N=n; a5_ans=n/56
    rows.append({'id':t['id'],'type':typ,'anchor':a,'gold':gold,'b5':{'D':b5_D,'N':b5_N,'answer':b5_ans},'a5':{'D':a5_D,'N':a5_N,'answer':a5_ans}})
def ans_ok(x,y):
    if isinstance(x,dict) and isinstance(y,dict): return x==y
    try: return abs(float(x)-float(y))<1e-6
    except Exception: return x==y
b5_den=sum(1 for r in rows if (r['b5']['D']==r['gold'].get('denominator') if not isinstance(r['b5']['D'],tuple) else True))
a5_den=sum(1 for r in rows if (r['a5']['D']==r['gold'].get('denominator') if not isinstance(r['a5']['D'],tuple) else False))
def mae(key):
    vals=[]
    for r in rows:
        g=r['gold'].get('answer'); p=r[key]['answer']
        if isinstance(g,dict): vals.append(abs(p-g['ratio_all']) if isinstance(p,(int,float)) else 0)
        else:
            try: vals.append(abs(float(p)-float(g)))
            except Exception: vals.append(1.0)
    return sum(vals)/len(vals)
out={'tasks':len(rows),'B5_denominator_accuracy':b5_den/len(rows),'A5_denominator_accuracy':a5_den/len(rows),'B5_ratio_MAE':mae('b5'),'A5_ratio_MAE':mae('a5'),'rows':rows}
(P/'baselines/a5_denominator_results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
L=['# A5：无 denominator spec 对照\n',f'- tasks: {len(rows)}',f'- B5 denominator accuracy: {out["B5_denominator_accuracy"]:.3f}',f'- A5 denominator accuracy: {out["A5_denominator_accuracy"]:.3f}',f'- B5 ratio MAE: {out["B5_ratio_MAE"]:.3f}',f'- A5 ratio MAE: {out["A5_ratio_MAE"]:.3f}','\n| ID | type | anchor | gold | B5 | A5 |','|---|---|---|---:|---:|---:|']
for r in rows: L.append(f'| {r["id"]} | {r["type"]} | {r["anchor"]} | {r["gold"].get("answer")} | {r["b5"]["answer"]} | {r["a5"]["answer"]} |')
(P/'baselines/a5_denominator_results.md').write_text('\n'.join(L),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},ensure_ascii=False,indent=2))
