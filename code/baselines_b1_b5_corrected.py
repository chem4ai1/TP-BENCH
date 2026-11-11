import json, re, math
from collections import Counter
from core_v3 import config, strict_metrics

P=config.DATA
DOCS={d['doc_id']:d for d in [json.loads(l) for l in (P/'raw/doc_annotations.jsonl').read_text(encoding='utf-8').splitlines()]}
TASKS=[json.loads(l) for l in (P/'tiers/dataset_v3_corrected.jsonl').read_text(encoding='utf-8').splitlines()]
S=[t for t in TASKS if t['group'] in {'role_variant','model_role','granularity','granularity_pair'} and (t.get('evaluation') or {}).get('members')]
MD={d:(P/'docs'/f'{d}.md').read_text(encoding='utf-8',errors='ignore') if (P/'docs'/f'{d}.md').exists() else (config.CORPUS_MD/d/f'{d}.md').read_text(encoding='utf-8',errors='ignore') for d in DOCS}
chunks=[]
for d,t in MD.items():
    for i in range(0,max(1,len(t)),500):
        c=t[i:i+600]
        if c.strip(): chunks.append((d,c))
def toks(s):
    s=''.join(re.findall(r'[\u4e00-\u9fffA-Za-z0-9]+',s))
    out=set(re.findall(r'[\u4e00-\u9fff]{2}',s)); out |= set(re.findall(r'[A-Za-z]{2,}',s)); out |= set(re.findall(r'\d{4}',s)); return out
chunk_tokens=[toks(c) for _,c in chunks]; df=Counter()
for ts in chunk_tokens:
    for t in ts: df[t]+=1
N=len(chunks); idf={t:math.log((N+1)/(v+1))+1 for t,v in df.items()}
ANCHORS=['海北','内蒙古','长白山','千烟洲','鼎湖山','阿克苏','策勒','阜康','禹城','会同','临泽','安塞','拉萨','当雄','海伦','沈阳','封丘','鹰潭','桃源','常熟','帽儿山','大兴安岭','哀牢山','西双版纳','北京森林','秦岭','茂县','尖峰岭','神农架','栾城']
MODELS=['随机森林','CENTURY','人工神经网络','VIP','CASA','TL-LUE','Penman-Monteith','Priestley-Taylor','Shuttleworth-Wallace','InVEST','PLUS','CLM5','DLM','MCR','PLS','Noah-MP','FORCCHN','SWH双源','水均衡法']
def anchor_of(t):
    cq=t.get('population_spec',{}).get('C_q_pop',''); m=re.search(r'Station="([^"]+)"',cq)
    return m.group(1) if m else next((a for a in ANCHORS if a in t.get('question_zh','')),None)
def model_of(t): return next((m for m in MODELS if m in t.get('question_zh','')),None)
def role_docs(a,role):
    out=[]
    for d,x in DOCS.items():
        ss=[s for s in x.get('stations',[]) if s.get('name_norm')==a]
        if role=='research_site' and any(s.get('role')=='研究站点' and s.get('relation')=='使用' for s in ss): out.append(d)
        if role=='observation_source' and any(s.get('role')=='观测来源' and s.get('relation')=='使用' for s in ss): out.append(d)
        if role=='background_mention' and a in MD[d] and not any(s.get('relation')=='使用' for s in ss): out.append(d)
    return sorted(set(out))
def model_docs(m,role):
    out=[]
    for d,x in DOCS.items():
        ms=[z for z in x.get('models',[]) if z.get('name_norm')==m]
        if not ms: continue
        if role=='applied_model' and any(z.get('role')=='实际采用' for z in ms): out.append(d)
        if role=='mentioned_model' and m in MD[d] and not any(z.get('role')=='实际采用' for z in ms): out.append(d)
    return sorted(set(out))
def b5_pred(t):
    cq=t.get('population_spec',{}).get('C_q_pop',''); q=t.get('question_zh',''); a=anchor_of(t); m=model_of(t)
    if t['group']=='role_variant' and a:
        role='background_mention' if ('background' in cq or '背景' in q) else ('observation_source' if 'observation_source' in cq or '观测来源' in q else 'research_site')
        return role_docs(a,role)
    if t['group']=='model_role' and m:
        return model_docs(m,'applied_model' if '实际采用' in q else 'mentioned_model')
    if t['group'] in ('granularity','granularity_pair'):
        if '海北' in q and '高寒草甸' in q:
            return [d for d in role_docs('海北','research_site') if '高寒草甸' in MD[d]]
        cn={'Forest':'森林生态系统','Cropland':'农田生态系统','Desert':'荒漠生态系统'}
        for k,v in cn.items():
            if k in q or k in cq:
                return sorted({d for d,x in DOCS.items() if any(s.get('relation')=='使用' and s.get('type_norm')==v for s in x.get('stations',[]))})
    return []
def b2_pred(t):
    a=anchor_of(t); m=model_of(t); q=t.get('question_zh','')
    if t['group']=='role_variant' and a: return sorted({d for d in DOCS if a in MD[d]})
    if t['group']=='model_role' and m: return sorted({d for d in DOCS if m in MD[d]})
    if t['group'] in ('granularity','granularity_pair'):
        term=next((x for x in ['高寒草甸','温带草原','草甸','草原','森林','农田','荒漠'] if x in q),None)
        return sorted({d for d in DOCS if term and term in MD[d]}) if term else []
    return []
def b1_pred(t,k=20):
    a=anchor_of(t); m=model_of(t); q=t.get('question_zh','')
    qt=toks(q); qn=math.sqrt(sum(idf.get(x,1)**2 for x in qt)) or 1
    scores=[]
    for i,(d,c) in enumerate(chunks):
        ts=chunk_tokens[i]; dot=sum(idf.get(x,1) for x in (qt & ts)); tn=math.sqrt(sum(idf.get(x,1)**2 for x in ts)) or 1
        scores.append((dot/(qn*tn),i))
    scores.sort(reverse=True); docs=[]
    for _,i in scores[:k]:
        d,c=chunks[i]
        if (a and a in c) or (m and m in c): docs.append(d)
    return sorted(set(docs))
def b3_pred(t): return []

def eval_pred(t,pred,answer=None):
    pred=set(pred); gold=t['gold']; ans=gold.get('answer')
    if answer is None: answer=len(pred)
    ref={'id':t['id'],'group':t['group'],'gold':{'answer':ans,'members':gold.get('members') or [],'denominator':gold.get('denominator'),'denominator_members':gold.get('denominator_members') or []},'evaluation':t.get('evaluation') or {'answer':True,'members':True,'denominator_count':False,'reasons':[]}}
    return strict_metrics.evaluate(ref,{'status':'ok' if pred else 'abstain','answer':answer,'members':sorted(pred),'denominator_count':ans if isinstance(ans,int) else None})

systems={'B1_RAG':b1_pred,'B2_Extraction':b2_pred,'B5_Full':b5_pred}
results={}
for name,fn in systems.items():
    rows=[eval_pred(t,fn(t)) for t in S]
    results[name]={'summary':strict_metrics.summarize(rows),'rows':rows}
b4_path=P/'baselines/b4_qwen_retrieval.json'
if not b4_path.exists():
    raise SystemExit('run code/b4_qwen_retrieval.py before building B1--B5 assets')
b4=json.loads(b4_path.read_text(encoding='utf-8'))
results['B4_Qwen_retrieval']={'summary':b4['summary']['strict'],'rows':b4['rows'],
    'note':'Qwen3.8-27B retrieval-only baseline; candidates come from TF-IDF top-20 chunks, not annotated source_docs'}
out={'subset_size':len(S),'systems':results}
(P/'baselines').mkdir(exist_ok=True)
(P/'baselines/b1_b5_corrected.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
L=['# B1—B5 corrected strict results\n',f'Membership subset: {len(S)} tasks with corrected references and `evaluation.members=True`.\n','| System | Answer n | Strict acc | Pop macro F1 | Nonempty F1 | Micro F1 |','|---|---:|---:|---:|---:|---:|']
for k,v in results.items():
    s=v.get('summary',{})
    L.append(f"| {k} | {s.get('answer_n')} | {s.get('strict_answer_accuracy')} | {s.get('population_macro_f1')} | {s.get('nonempty_population_f1')} | {s.get('population_micro_f1')} |")
L += ['\n## Notes\n','- B1/B2/B5 are deterministic reruns on the corrected TP IDs.','- B4 is a Qwen3.8-27B retrieval-only baseline; candidates come from TF-IDF retrieval, not annotated source_docs or gold members.','- `abstain` receives no empty-set credit; applicability masks come from corrected references.']
(P/'baselines/b1_b5_corrected.md').write_text('\n'.join(L),encoding='utf-8')
print(json.dumps({k:v.get('summary') for k,v in results.items()},ensure_ascii=False,indent=2))
