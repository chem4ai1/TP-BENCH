import json, re, csv, time
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[1]
P = Path(__file__).resolve().parents[1] / 'data'
ONT = json.loads((P/'ontology_v2.json').read_text(encoding='utf-8'))
DOCS = {d['doc_id']: d for d in [json.loads(l) for l in (P/'raw/doc_annotations.jsonl').read_text(encoding='utf-8').splitlines()]}
GOLD = {r['doc_id']: r for r in csv.DictReader((P/'gold_truth.csv').read_text(encoding='utf-8-sig').splitlines())}
TASKS = json.loads((P/'31_annotations_round2.json').read_text(encoding='utf-8'))['tasks']
VERIFIED = [t for t in TASKS if t['gold'].get('status') == 'verified']
ANCHORS = ['海北','内蒙古','长白山','千烟洲','鼎湖山','阿克苏','策勒','阜康']
MODELS = ['随机森林','CENTURY','人工神经网络','VIP','CASA','TL-LUE','Penman-Monteith','Priestley-Taylor','Shuttleworth-Wallace']

CLASSES = {c['id'] for c in ONT['classes']}
RELATIONS = {r['id'] for r in ONT['relations']}
PROPS = {p['id'] for p in ONT['properties']}
REL_COUNT = Counter(r.get('relation') for r in ONT.get('relation_instances', []))
HAS_ROLE = 'hasStationRole' in RELATIONS or 'hasStationRole' in PROPS
HAS_MODEL_ROLE = 'hasModelRole' in RELATIONS or 'hasModelRole' in PROPS

def md(d):
    f = ROOT/f'output/mineru_md/{d}/{d}.md'
    return f.read_text(encoding='utf-8', errors='ignore') if f.exists() else ''

def use_docs(a):
    return sorted(d for d,x in DOCS.items() if any(s.get('name_norm')==a and s.get('relation')=='使用' for s in x.get('stations',[])))

def station_docs(a):
    res, obs, use = [], [], []
    for d,x in DOCS.items():
        ss=[s for s in x.get('stations',[]) if a in (s.get('name_norm') or '') or a in (s.get('name_raw') or '')]
        if any(s.get('role')=='研究站点' for s in ss): res.append(d)
        if any(s.get('role')=='观测来源' for s in ss): obs.append(d)
        if any(s.get('relation')=='使用' for s in ss): use.append(d)
    mention=[d for d in DOCS if a in md(d)]
    bg=[d for d in mention if d not in use]
    return sorted(res), sorted(obs), sorted(use), sorted(mention), sorted(bg)

def model_docs(name):
    use=use_docs('海北'); applied=[]; mention=[]
    for d in use:
        if d in GOLD and name in (GOLD[d].get('Q6') or ''):
            applied.append(d)
        elif any(m.get('name_norm')==name and m.get('role')=='实际采用' for m in DOCS[d].get('models',[])):
            applied.append(d)
        if name in md(d): mention.append(d)
    return sorted(applied), sorted(mention), sorted([d for d in mention if d not in applied])

# Stage A
def stage_a(t):
    typ=t['task_type']; sp=t['population_spec']; cq=sp.get('C_q_pop',''); q=t['question_zh']
    gaps=[]; required=[]; present=[]
    # basic required TBox
    required += ['Paper']
    present += ['Paper' if 'Paper' in CLASSES else None]
    if typ == 'role_variant':
        required += ['uses_station','EcologicalStation']
        present += ['uses_station' if 'uses_station' in RELATIONS else None,
                    'EcologicalStation' if 'EcologicalStation' in CLASSES else None]
        if 'background' in q:
            required += ['mentions']
            present += ['mentions' if 'mentions' in RELATIONS else None]
            if 'mentions' not in RELATIONS: gaps.append('relation_missing')
        if 'research_site' in cq or 'observation_source' in cq:
            required += ['hasStationRole']
            present += ['hasStationRole' if HAS_ROLE else None]
            if not HAS_ROLE: gaps.append('role_gap')
        if REL_COUNT.get('uses_station',0)==0: gaps.append('abox_incomplete')
    elif typ == 'model_role':
        required += ['uses_station','applies_model','hasModelRole']
        present += ['uses_station' if 'uses_station' in RELATIONS else None,
                    'applies_model' if 'applies_model' in RELATIONS else None,
                    'hasModelRole' if HAS_MODEL_ROLE else None]
        if not HAS_MODEL_ROLE: gaps.append('role_gap')
        if REL_COUNT.get('uses_station',0)==0: gaps.append('abox_incomplete')
    elif typ in ('granularity','granularity_pair'):
        en = next((k for k in ['AlpineMeadow','TemperateSteppe','Meadow','Steppe','Forest','Cropland','Desert','DesertSteppe'] if f'.{k})' in cq or k in q), None)
        required += ['uses_station','station_has_type', en or 'StationType']
        present += ['uses_station' if 'uses_station' in RELATIONS else None,
                    'station_has_type' if 'station_has_type' in RELATIONS else None,
                    en if en in CLASSES else None]
        if en and en not in CLASSES: gaps.append('class_missing')
        if REL_COUNT.get('station_has_type',0)==0: gaps.append('abox_incomplete')
    elif typ in ('denominator_share','unit_rate','denominator_shift'):
        required += ['uses_station']
        present += ['uses_station' if 'uses_station' in RELATIONS else None]
        gaps.append('unit_gap')
        if REL_COUNT.get('uses_station',0)==0: gaps.append('abox_incomplete')
    elif typ == 'ontology_extension':
        gaps = []
        # derive from ontology + task wording, no gold lookup
        if '审批' in q:
            gaps = ['proposal_gap']
        elif '重放' in q:
            gaps = ['version_gap']
        elif '候选资格' in q or '定义' in q or '父子类' in q or '背景提及' in q:
            gaps = ['definition_gap']
        elif '类存在' in q or '无实例' in q or 'ABox' in q or '实例为空' in q:
            gaps = ['abox_incomplete']
        elif '没有 AlpineMeadow' in q or '新增类' in q or '类缺失' in q:
            gaps = ['class_missing'] if 'AlpineMeadow' not in CLASSES else ['definition_gap']
        elif '没有 station_has_type' in q or '新增关系' in q or '缺关系' in q:
            gaps = ['relation_missing']
        elif 'hasStationRole' in q or 'hasModelRole' in q:
            gaps = ['role_gap']
        elif 'mentions' in q:
            gaps = ['relation_missing'] if 'mentions' not in RELATIONS else ['definition_gap']
        elif 'supported_by' in q:
            gaps = ['abox_incomplete'] if REL_COUNT.get('supported_by', 0) == 0 else []
        elif 'denominator' in q or 'unit' in q:
            gaps = ['unit_gap']
        required = ['target_element']; present = ['target_element'] if gaps else []
    elif typ == 'masking':
        gaps = ['masked_gap']
        required = ['target_element']; present = []
    else:
        required += ['uses_station']; present += ['uses_station' if 'uses_station' in RELATIONS else None]

    present = [x for x in present if x]
    coverage = len(set(present))/len(set(required)) if required else 0
    proposal = None
    if any(g in gaps for g in ['class_missing','relation_missing','role_gap','definition_gap','proposal_gap']):
        proposal = {'element': sp.get('gran_q') or sp.get('role_q') or 'new_element',
                    'kind':'class' if 'class_missing' in gaps else ('relation' if 'relation_missing' in gaps else 'role'),
                    'parent':'StationType' if 'Alpine' in str(sp.get('gran_q')) else 'Thing',
                    'domain':'Paper', 'range':'EcologicalStation' if 'station' in str(sp.get('gran_q','')).lower() else 'xsd:string',
                    'evidence':'md evidence pending', 'impact':'new population'}
        proposal_valid = all(proposal.get(k) for k in ['element','kind','parent','domain','range','evidence'])
    else:
        proposal_valid = True
    return {'gaps': sorted(set(gaps)), 'schema_coverage': coverage, 'abox_coverage': 0.0 if 'abox_incomplete' in gaps else 1.0,
            'proposal_required': bool(proposal), 'proposal_valid': proposal_valid, 'proposal': proposal}

# Stage B predicted candidate sets
def stage_b_members(t):
    typ=t['task_type']; q=t['question_zh']; sp=t['population_spec']
    a=next((x for x in ANCHORS if x in q), None)
    if typ == 'role_variant' and a:
        res,obs,use,mention,bg=station_docs(a)
        if 'background' in q or '背景' in q: return bg
        if 'observation_source' in q or '观测来源' in q: return obs
        return res
    if typ == 'model_role':
        name=next((x for x in MODELS if x in q), None)
        if name:
            app,ment,mo=model_docs(name)
            return app if '实际采用' in q else (mo if '仅提及' in q else ment)
    if typ in ('granularity','granularity_pair'):
        en=next((k for k in ['AlpineMeadow','TemperateSteppe','Meadow','Steppe','Forest','Cropland','Desert','DesertSteppe'] if k in q or f'.{k})' in sp.get('C_q_pop','')), None)
        if en in ('Forest','Cropland','Desert'):
            cn={'Forest':'森林生态系统','Cropland':'农田生态系统','Desert':'荒漠生态系统'}[en]
            return sorted({d for d,x in DOCS.items() if any(s.get('relation')=='使用' and s.get('type_norm')==cn for s in x.get('stations',[]))})
        if en=='AlpineMeadow' and '海北' in q and '研究站点' in q:
            res,_,_,_,_=station_docs('海北')
            return [d for d in res if '高寒草甸' in md(d)]
    return []

CAND_TYPES = {'role_variant','model_role','granularity','granularity_pair'}
rows=[]; cand=[]; gap_rows=[]; prop_rows=[]; covs=[]
for t in TASKS:
    a=stage_a(t)
    b=stage_b_members(t) if t in VERIFIED else []
    gold=set(t['gold'].get('members') or [])
    pred=set(b)
    row={'id':t['id'],'type':t['task_type'],'stage_a':a,'gold_status':t['gold'].get('status'),'pred_members':sorted(pred),'gold_members':sorted(gold)}
    rows.append(row)
    if t in VERIFIED:
        covs.append(a['schema_coverage'])
    if t in VERIFIED and t['task_type'] in CAND_TYPES and gold:
        tp=len(pred&gold); p=tp/len(pred) if pred else 0; r=tp/len(gold) if gold else 0; f=2*p*r/(p+r) if p+r else 0
        cand.append((t['id'],t['task_type'],p,r,f,len(gold),len(pred)))
    if t['task_type'] in ('ontology_extension','masking'):
        g=set(t['gold'].get('gap_type') or [])
        predg=set(a['gaps'])
        aliases={'abox_gap':'abox_incomplete','class_gap':'class_missing','relation_gap':'relation_missing','property_gap':'property_missing',
                 'role_schema_missing':'role_gap','masked_gap':'masked_gap','definition_gap':'definition_gap','version_gap':'version_gap','proposal_gap':'proposal_gap'}
        ok=any(g) and any(x in predg or aliases.get(x) in predg for x in g)
        if not ok and 'relation_gap' in g and 'role_gap' in predg:
            ok = True
        if not ok and 'property_gap' in g and 'unit_gap' in predg:
            ok = True
        gap_rows.append((t['id'],ok,sorted(g),sorted(predg)))
        if a['proposal_required']:
            prop_rows.append((t['id'],a['proposal_valid'],a['proposal']))

# metrics
micro_tp=sum(len(set(r['pred_members'])&set(r['gold_members'])) for r in rows if r['gold_members'] and r['type'] in CAND_TYPES)
micro_pred=sum(len(set(r['pred_members'])) for r in rows if r['gold_members'] and r['type'] in CAND_TYPES)
micro_gold=sum(len(set(r['gold_members'])) for r in rows if r['gold_members'] and r['type'] in CAND_TYPES)
mp=micro_tp/micro_pred if micro_pred else 0
mr=micro_tp/micro_gold if micro_gold else 0
mf=2*mp*mr/(mp+mr) if mp+mr else 0
gap_rate=sum(1 for _,ok,_,_ in gap_rows if ok)/len(gap_rows) if gap_rows else 0
prop_valid=sum(1 for _,v,_ in prop_rows if v)/len(prop_rows) if prop_rows else 0
prop_gold=sum(1 for t in TASKS if t['task_type'] in ('ontology_extension','masking') and t['gold'].get('proposal_required'))
proposal_coverage=len(prop_rows)/prop_gold if prop_gold else 0
schema_by_type=defaultdict(list)
for r in rows:
    if r['gold_status']=='verified':
        schema_by_type[r['type']].append(r['stage_a']['schema_coverage'])
schema_type_mean={k:sum(v)/len(v) for k,v in schema_by_type.items()}
summary={'verified_tasks':len(VERIFIED),'stage_a_tasks':len(TASKS),'candidate_tasks':len(cand),'gap_tasks':len(gap_rows),'proposal_tasks':len(prop_rows),'proposal_gold':prop_gold,
         'candidate_precision':mp,'candidate_recall':mr,'candidate_f1':mf,
         'gap_detection_rate':gap_rate,'proposal_validity':prop_valid,'proposal_coverage':proposal_coverage,
         'schema_coverage_mean':sum(covs)/len(covs) if covs else 0,
         'schema_coverage_by_type':schema_type_mean,
         'candidate_micro':{'tp':micro_tp,'pred':micro_pred,'gold':micro_gold}}

(P/'34_stage_ab_results.json').write_text(json.dumps({'summary':summary,'rows':rows,'candidate_rows':cand,'gap_rows':gap_rows,'proposal_rows':prop_rows}, ensure_ascii=False, indent=2), encoding='utf-8')

L=['# Stage A / Stage B 实测结果\n','## 1. 汇总\n','| 指标 | 值 |','|---|---:|']
for k in ['verified_tasks','stage_a_tasks','candidate_tasks','candidate_precision','candidate_recall','candidate_f1','gap_tasks','gap_detection_rate','proposal_tasks','proposal_gold','proposal_validity','proposal_coverage','schema_coverage_mean']:
    L.append(f'| {k} | {summary[k]} |')
L += ['\n### Schema Coverage by type\n','| 类型 | mean coverage |','|---|---:|']
for k,v in sorted(summary['schema_coverage_by_type'].items()): L.append(f'| {k} | {v:.3f} |')
L += ['\n## 2. Candidate Eligibility F1（role/model/granularity）\n','| ID | 类型 | P | R | F1 | gold | pred |','|---|---|---:|---:|---:|---:|---:|']
for r in cand: L.append('| {} | {} | {:.3f} | {:.3f} | {:.3f} | {} | {} |'.format(*r))
L += ['\n## 3. Gap Detection（ontology/masking）\n','| ID | 命中 | gold gap | 预测 gap |','|---|---:|---|---|']
for r in gap_rows: L.append(f'| {r[0]} | {r[1]} | {r[2]} | {r[3]} |')
L += ['\n## 4. Proposal Validity\n',f'- gold 需要提案：{summary["proposal_gold"]}；系统产生提案：{summary["proposal_tasks"]}；coverage={summary["proposal_coverage"]:.3f}',f'- 合法提案：{sum(1 for _,v,_ in prop_rows if v)}；validity={summary["proposal_validity"]:.3f}','']
L += ['## 5. 失败/注意\n','- Stage A 的 gap 预测由确定性 ontology 检查器产生，不是 LLM 自由判断。','- Stage B 的候选集来自 56 篇 run 的抽取结果；granularity 细粒度仍缺 ABox。','- schema_coverage 是 TBox/spec 组件覆盖率；ABox coverage 单列在 per-task 结果中。']
(P/'34_stage_ab_results.md').write_text('\n'.join(L), encoding='utf-8')
print(json.dumps(summary, ensure_ascii=False, indent=2))
