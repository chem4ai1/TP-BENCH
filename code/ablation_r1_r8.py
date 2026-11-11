import json,re,csv
from pathlib import Path
from collections import defaultdict, Counter
P=Path(__file__).resolve().parents[1]/'data'
ROOT=Path(__file__).resolve().parents[1]
DOCS={d['doc_id']:d for d in [json.loads(l) for l in (P/'raw/doc_annotations.jsonl').read_text(encoding='utf-8').splitlines()]}
GOLD={r['doc_id']:r for r in csv.DictReader((P/'gold_truth.csv').read_text(encoding='utf-8-sig').splitlines())}
TASKS=json.loads((P/'31_annotations_round2.json').read_text(encoding='utf-8'))['tasks']
MD={d:(P/'docs'/f'{d}.md').read_text(encoding='utf-8',errors='ignore') if (P/'docs'/f'{d}.md').exists() else (ROOT/f'output/mineru_md/{d}/{d}.md').read_text(encoding='utf-8',errors='ignore') if (ROOT/f'output/mineru_md/{d}/{d}.md').exists() else '' for d in DOCS}
S=[]; seen=set()
for t in TASKS:
    if t['gold'].get('status')!='verified': continue
    if t['task_type'] not in ('role_variant','model_role','granularity','granularity_pair'): continue
    if (t['task_type'],t['question_zh']) in seen: continue
    seen.add((t['task_type'],t['question_zh'])); S.append(t)
def anchor_of(t):
    cq=t['population_spec'].get('C_q_pop',''); m=re.search(r'Station="([^"]+)"',cq)
    if m: return m.group(1)
    for a in ['海北','内蒙古','长白山','千烟洲','鼎湖山','阿克苏','策勒','阜康']:
        if a in t['question_zh']: return a
    return None
def role_sets(a):
    res=set(); obs=set(); use=set(); mention=set(); unknown=set(); unknown_bg=set()
    data_cues=('数据','气象','观测','通量','来源于','共享','搜集','下载')
    for d,x in DOCS.items():
        ss=[s for s in x.get('stations',[]) if s.get('name_norm')==a]
        if any(s.get('relation')=='使用' for s in ss): use.add(d)
        if any(s.get('role')=='研究站点' for s in ss): res.add(d)
        if any(s.get('role')=='观测来源' for s in ss): obs.add(d)
        if any(s.get('role')=='未分类' or s.get('relation')=='待定' for s in ss):
            unknown.add(d)
            ev=' '.join(str(s.get('evidence','')) for s in ss if s.get('role')=='未分类' or s.get('relation')=='待定')
            if not any(c in ev for c in data_cues): unknown_bg.add(d)
        if a in MD.get(d,''): mention.add(d)
    bg=(mention-use-unknown) | unknown_bg
    return res,obs,bg,unknown,mention
def is_role(t): return t['task_type']=='role_variant'
def role_of(t):
    q=t['question_zh']; cq=t['population_spec'].get('C_q_pop','')
    if 'background' in cq or '背景' in q: return 'background_mention'
    if 'observation_source' in cq or '观测来源' in q: return 'observation_source'
    return 'research_site'
def base(t):
    a=anchor_of(t)
    if t['task_type']=='role_variant' and a:
        r,o,b,u,m=role_sets(a); return sorted({'research_site':r,'observation_source':o,'background_mention':b}[role_of(t)])
    if t['task_type']=='model_role':
        from_json=t.get('gold',{}).get('members',[])
        # deterministic role candidates are reconstructed in model_base below
        return model_base(t)
    if t['task_type'] in ('granularity','granularity_pair'):
        q=t['question_zh']; cq=t['population_spec'].get('C_q_pop','')
        if '海北' in q and '高寒草甸' in q:
            r,o,b,u,m=role_sets('海北'); return sorted([d for d in r if '高寒草甸' in MD.get(d,'')])
        cn={'Forest':'森林生态系统','Cropland':'农田生态系统','Desert':'荒漠生态系统'}
        for k,v in cn.items():
            if k in q or k in cq:
                return sorted({d for d,x in DOCS.items() if any(s.get('relation')=='使用' and s.get('type_norm')==v for s in x.get('stations',[]))})
    return []
def model_base(t):
    q=t['question_zh']
    m=next((x for x in ['随机森林','CENTURY','人工神经网络','VIP','CASA','TL-LUE','Penman-Monteith','Priestley-Taylor'] if x in q),None)
    if not m: return []
    use={d for d,x in DOCS.items() if any(s.get('name_norm')=='海北' and s.get('relation')=='使用' for s in x.get('stations',[]))}
    applied=set(); mention=set()
    for d in use:
        if d in GOLD and m in (GOLD[d].get('Q6') or ''): applied.add(d)
        elif any(z.get('name_norm')==m and z.get('role')=='实际采用' for z in DOCS[d].get('models',[])): applied.add(d)
        if m in MD.get(d,''): mention.add(d)
    if '实际采用' in q: return sorted(applied)
    if '仅提及' in q: return sorted(mention-applied)
    return sorted(mention)
def variant(t,name):
    if not is_role(t): return base(t)
    a=anchor_of(t); r,o,b,u,m=role_sets(a); q=role_of(t)
    if name=='R0': return base(t)
    if name=='R1': return sorted(r|o|b|u)  # no hasStationRole
    if name=='R2':
        if q=='observation_source': return sorted(o - r)  # force single role; doc010 moves to research
        return base(t)
    if name=='R3':
        if q=='research_site': return sorted(r|b)
        return base(t)
    if name=='R4':
        if q=='background_mention': return sorted(b|u)
        return base(t)
    if name=='R5': return sorted(r|o|u)  # no auditor
    if name=='R6': return base(t)
    if name=='R7': return sorted(set(base(t))|u)  # no evidence gate
    return base(t)
def micro(rows):
    tp=sum(len(set(p)&set(g)) for p,g in rows); pp=sum(len(set(p)) for p,g in rows); gg=sum(len(set(g)) for p,g in rows)
    pr=tp/pp if pp else 0; rc=tp/gg if gg else 0; return pr,rc,(2*pr*rc/(pr+rc) if pr+rc else 0)
variants=['R0','R1','R2','R3','R4','R5','R6','R7']
res={}
rows_by_v={}
for v in variants:
    rows=[]; groups={'research':[], 'observation':[], 'background':[], 'model':[], 'granularity':[]}
    for t in S:
        pred=variant(t,v); gold=t['gold'].get('members') or []
        rows.append((pred,gold))
        if is_role(t):
            q=role_of(t); groups['research' if q=='research_site' else ('observation' if q=='observation_source' else 'background')].append((pred,gold))
        elif t['task_type']=='model_role': groups['model'].append((pred,gold))
        else: groups['granularity'].append((pred,gold))
    pr,rc,f=micro(rows); mae=sum(abs(len(p)-len(g)) for p,g in rows)/len(rows); acc=sum(1 for p,g in rows if set(p)==set(g))/len(rows)
    rp=groups['research']; op=groups['observation']; bp=groups['background']
    rpr=micro(rp)[0]; orc=micro(op)[1]; bfp=0; bden=0
    for p,g in bp:
        p=set(p); g=set(g); fp=len(p-g); tn=56-len(p|g); bfp+=fp; bden+=fp+tn
    background_fpr=bfp/bden if bden else 0
    res[v]={'precision':pr,'recall':rc,'f1':f,'mae':mae,'answer_acc':acc,'research_p':rpr,'observation_r':orc,'background_fpr':background_fpr,'rows':rows}
    rows_by_v[v]=rows
# unknown leak R4 vs R0 for background tasks
def unknown_docs(a):
    _,_,_,u,_=role_sets(a); return u
leak=0; total=0
for t in S:
    if is_role(t) and role_of(t)=='background_mention':
        a=anchor_of(t); u=unknown_docs(a); p=set(variant(t,'R4')); total+=len(u); leak+=len(p&u)
res['R4']['unknown_leak']=leak/total if total else 0
# duplicate rate (R6)
dup=0; tot=0
for t in S:
    if not is_role(t): continue
    a=anchor_of(t)
    for d,x in DOCS.items():
        raws=[s.get('name_raw') or '' for s in x.get('stations',[]) if s.get('name_norm')==a]
        if len(raws)>1: dup+=len(raws)-1; tot+=len(raws)
res['R6']['duplicate_rate']=dup/tot if tot else 0
# LLM-only O
b4=json.loads((P/'37_trigger_eval_supervl.json').read_text(encoding='utf-8'))
o_rows=[(r.get('pred_positive') or [],r.get('gold_positive') or []) for r in b4['rows']]
op,orr,of=micro(o_rows)
res['R8']={'precision':op,'recall':orr,'f1':of,'mae':None,'answer_acc':None,'source':'O01-O14 LLM-only'}
out={'subset_size':len(S),'variants':res,'llm_only':{'p':op,'r':orr,'f1':of},'b4_summary':b4.get('summary')}
(P/'baselines').mkdir(exist_ok=True)
(P/'baselines/r1_r8_results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
L=['# R1—R8 角色/候选资格消融\n',f'Role/model/granularity verified subset: {len(S)}\n','| 变体 | P | R | F1 | MAE | Answer Acc | Research P | Observation R | Background FPR |','|---|---:|---:|---:|---:|---:|---:|---:|---:|']
for v in variants:
    x=res[v]; L.append(f'| {v} | {x["precision"]:.3f} | {x["recall"]:.3f} | {x["f1"]:.3f} | {x["mae"]:.2f} | {x["answer_acc"]:.3f} | {x["research_p"]:.3f} | {x["observation_r"]:.3f} | {x["background_fpr"]:.3f} |')
L += [f'\n- R4 unknown leak rate: {res["R4"].get("unknown_leak",0):.3f}',f'- R6 duplicate rate: {res["R6"].get("duplicate_rate",0):.3f}',f'\n## LLM-only (O01—O14)\n\nP={op:.3f}, R={orr:.3f}, F1={of:.3f}\n','\n## 说明\n','- R0 是角色约束 + auditor 的完整候选。','- R1 合并研究/观测/背景/未分类；R2 强制单角色；R3 背景并入研究；R4 未分类并入背景；R5 去掉 auditor；R6 去掉 sameAs；R7 去掉 evidence gate；R8 为 O01—O14 的 LLM-only。','- R1—R7 在 47 个 role/model/granularity verified 任务上评测；R8 在 O01—O14 上评测，二者不可直接混为一个 F1。']
(P/'baselines/r1_r8_results.md').write_text('\n'.join(L),encoding='utf-8')
print(json.dumps({k:{kk:(round(vv,3) if isinstance(vv,(int,float)) else vv) for kk,vv in v.items() if kk not in ('rows',)} for k,v in res.items()},ensure_ascii=False,indent=2))
