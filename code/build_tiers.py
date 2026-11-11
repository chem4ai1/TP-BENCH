import json, re, csv, hashlib, random
from collections import defaultdict, Counter
from pathlib import Path
P = Path(__file__).resolve().parents[1] / 'data'
R = random.Random(42)
DOCS = {d['doc_id']: d for d in [json.loads(l) for l in (P/'raw/doc_annotations.jsonl').read_text(encoding='utf-8').splitlines()]}
ONTO = json.loads((P/'ontology_v2.json').read_text(encoding='utf-8'))
A_TASKS = json.loads((P/'31_annotations_round2.json').read_text(encoding='utf-8'))['tasks']
O_TASKS = json.loads((P/'35_ontology_tasks_v2.json').read_text(encoding='utf-8'))['tasks']
STATION_ID = {i.get('attributes',{}).get('name'): i['id'] for i in ONTO.get('individuals',[]) if i.get('class')=='EcologicalStation'}
def md(d):
    f = P/'docs'/f'{d}.md'
    return f.read_text(encoding='utf-8', errors='ignore') if f.exists() else ''
def short(s, n=180):
    s = re.sub(r'\s+', ' ', s or '').strip()
    return s[:n]
def eid(prefix, name):
    return prefix + '_' + hashlib.md5(name.encode('utf-8')).hexdigest()[:10]
def doc_year(d):
    y = DOCS[d].get('year')
    try: return int(re.search(r'(19|20)\d\d', str(y)).group(0))
    except Exception: return None
def station_records():
    rec = defaultdict(list)
    valid_types = {'森林生态系统','农田生态系统','草地生态系统','荒漠生态系统','草甸生态系统','草原生态系统'}
    bad = ('网','数据中心','平台','数据库','共享服务')
    for d, x in DOCS.items():
        for s in x.get('stations', []):
            name = s.get('name_norm') or ''
            if s.get('relation') != '使用' or not name: continue
            if s.get('type_norm') not in valid_types: continue
            if any(b in name for b in bad): continue
            rec[(name, s.get('role') or '未分类')].append({'doc_id':d,'evidence':s.get('evidence',''),'section':s.get('section',''),'page':s.get('page'),'type_norm':s.get('type_norm',''),'confidence':s.get('confidence',0.8),'name_raw':s.get('name_raw','')})
    return rec
def model_records():
    rec = defaultdict(list)
    for d, x in DOCS.items():
        for m in x.get('models', []):
            if not m.get('name_norm'): continue
            rec[(m['name_norm'], m.get('role') or '未分类')].append({'doc_id':d,'evidence':m.get('evidence',''),'section':m.get('section',''),'page':m.get('page'),'model_type':m.get('model_type_norm',''),'confidence':m.get('confidence',0.6)})
    return rec
def data_records():
    rec = defaultdict(list)
    for d, x in DOCS.items():
        for u in x.get('data_uses', []):
            if not u.get('data_type_norm'): continue
            rec[(u.get('theme') or '其他', u['data_type_norm'], u.get('relation') or '未分类')].append({'doc_id':d,'evidence':u.get('evidence',''),'section':u.get('section',''),'page':u.get('page'),'confidence':u.get('confidence',0.6)})
    return rec
ST = station_records(); MR = model_records(); DR = data_records()
def evidence_list(recs, maxn=4):
    return [{'doc_id':r['doc_id'],'section':r.get('section',''),'page':r.get('page'),'quote':short(r.get('evidence',''))} for r in recs[:maxn]]
def spec(cq, nq, dq, role, gran, unit='paper'):
    return {'U_q':unit,'C_q_pop':cq,'N_q':nq,'D_q':dq,'role_q':role,'gran_q':gran,'unit_q':unit,'evidence_q':'sentence+page'}
def trace(planner, checker, schema, grounder, instance, reasoner, auditor):
    return {'stage_a':{'planner':planner,'ontology_checker':checker,'schema_agent':schema,'approval':'human approval when ontology_upgrade'},'stage_b':{'grounder':grounder,'instance_agent':instance,'reasoner':reasoner,'auditor':auditor}}
def make_grounding(name, recs, cls='EcologicalStation', relation='uses_station', role='research_site', gran=''):
    return {'mentions':[{'text':r.get('name_raw') or name,'doc_id':r['doc_id'],'entity_id':STATION_ID.get(name) or eid('Station',name),'class':cls,'relation':relation,'role':role,'granularity':gran,'confidence':r.get('confidence',0.8),'evidence':short(r.get('evidence',''),120)} for r in recs[:4]],'grounding_status':'resolved' if STATION_ID.get(name) else 'new_entity_candidate'}
def make_ontology(trigger_class, trigger_type, target, parent='', domain='', range_='', definition='', abox=''):
    proposal = {} if trigger_class != 'ontology_upgrade' else {'target':target,'parent':parent,'domain':domain,'range':range_,'definition':definition,'evidence':'paper evidence','impact':'changes population membership'}
    return {'trigger_class':trigger_class,'trigger_type':trigger_type,'required_element':target,'proposal':proposal,'approval_required':trigger_class=='ontology_upgrade','schema_version':'v2.1.460','abox_change':abox}
def make_stat(nrule, drule, unit, agg, answer, members, numerator=None, denominator=None):
    return {'numerator_rule':nrule,'denominator_rule':drule,'unit':unit,'aggregation':agg,'answer':answer,'members':sorted(set(members)),'numerator':numerator if numerator is not None else len(members),'denominator':denominator if denominator is not None else len(members),'accounting':'sum(members)=numerator; denominator declared'}
def task(tier, group, q, src, spec_, gold, grounding, ontology, statistical, trace_, status='evidence-backed'):
    return {'id':'','tier':tier,'group':group,'question_zh':q,'source_docs':sorted(set(src)),'evidence':[],'population_spec':spec_,'grounding':grounding,'ontology_editing':ontology,'statistical_process':statistical,'agent_trace':trace_,'gold':{'status':status, **gold},'llm_polish':{'model':'','original':q,'polished':'','status':'pending'},'metrics':['Population F1','Denominator Accuracy','Count MAE','Evidence Recall','Trigger F1','Proposal Validity']}
print('loaded', len(DOCS), len(ST), len(MR), len(DR))
# Tier A: 80 verified + O01-O14
A=[]
for t in A_TASKS:
    if t['gold'].get('status') != 'verified': continue
    A.append({'id':t['id'],'tier':'A','group':t['task_type'],'question_zh':t['question_zh'],'source_docs':t.get('source_docs',[]),'evidence':[{'doc_id':d,'quote':''} for d in t.get('source_docs',[])[:3]],'population_spec':t['population_spec'],'grounding':{'mentions':[],'grounding_status':'from_verified_task'},'ontology_editing':{'trigger_class':'verified','trigger_type':'','required_element':'','proposal':{},'approval_required':False,'schema_version':'v2.1.460'},'statistical_process':{'numerator_rule':t['population_spec'].get('N_q'),'denominator_rule':t['population_spec'].get('D_q'),'unit':t['population_spec'].get('unit_q'),'aggregation':t['task_type'],'answer':t['gold'].get('answer'),'members':t['gold'].get('members',[]),'numerator':t['gold'].get('numerator'),'denominator':t['gold'].get('denominator'),'accounting':'verified against run'},'agent_trace':trace('loaded verified task','verified','n/a','n/a','n/a','n/a','verified'),'gold':t['gold'],'llm_polish':{'model':'','original':t['question_zh'],'polished':'','status':'curated'},'metrics':['Population F1','Denominator Accuracy','Count MAE']})
for o in O_TASKS:
    A.append({'id':o['id'],'tier':'A','group':'ontology_nested','question_zh':o['main_question'],'source_docs':[],'evidence':[],'population_spec':o['population_spec'],'grounding':{'mentions':[],'grounding_status':'from_ontology_task'},'ontology_editing':o['trigger_annotation'] | {'ontology_subtask':o['ontology_subtask']},'statistical_process':{'numerator_rule':o['population_spec'].get('N_q'),'denominator_rule':o['population_spec'].get('D_q'),'unit':o['population_spec'].get('unit_q'),'aggregation':'nested ontology task','answer':o['statistical_gold'].get('answer'),'members':o['statistical_gold'].get('members',[]),'numerator':None,'denominator':None,'accounting':'post-repair answer'},'agent_trace':trace('main question -> PopulationSpec','checker classifies trigger','proposal from O task','n/a','n/a','post-repair aggregation','auditor checks trigger/candidates'),'gold':{'status':'expert_design','members':o['statistical_gold'].get('members',[]),'numerator':None,'denominator':None,'answer':o['statistical_gold'].get('answer')},'llm_polish':{'model':'','original':o['main_question'],'polished':'','status':'curated'},'metrics':['Trigger F1','Proposal Validity','Candidate F1','Post-repair Answer']})
print('A',len(A))
B=[]
role_cn={'研究站点':'研究站点','观测来源':'观测来源','未分类':'未分类'}
# B1 station-role: sample 70 of 100
items=sorted(ST.items(), key=lambda kv:-len(kv[1]))[:70]
for (name,role),recs in items:
    docs=[r['doc_id'] for r in recs]; members=sorted(set(docs)); g=role if role!='未分类' else 'study_or_observation'
    q=f'把{name}作为{role_cn.get(role,role)}的论文有多少篇？'
    onto=make_ontology('ontology_upgrade','role_schema_missing','hasStationRole','Thing','Paper','StationRole','角色关系：研究站点/观测来源/背景提及')
    if role=='未分类': onto=make_ontology('abox_repair','abox_incomplete','uses_station',abox='backfill uses_station')
    t=task('B','station_role',q,docs,spec(f'Paper ⊓ ∃uses_station.(Station="{name}" ⊓ role={g})',f'{role} papers',f'{role} papers',g,recs[0].get('type_norm',''),'paper'),{'members':members,'numerator':len(members),'denominator':len(members),'answer':len(members)},make_grounding(name,recs,role=g,gran=recs[0].get('type_norm','')),onto,make_stat(f'{role} role',f'{name} papers','paper','count',len(members),members),trace('parse anchor/role','check uses_station + hasStationRole','propose hasStationRole','ground station mention/role','link paper->station','count paper members','check role and dedup'))
    t['evidence']=evidence_list(recs); B.append(t)
# B2 model-role: 37
for (name,role),recs in sorted(MR.items(), key=lambda kv:-len(kv[1]))[:37]:
    members=sorted({r['doc_id'] for r in recs}); role_cn2={'实际采用':'实际采用','仅提及':'仅提及','未分类':'提及或使用'}.get(role,role)
    q=f'论文中{role_cn2}{name}的论文有多少篇？'
    onto=make_ontology('ontology_upgrade','role_schema_missing','hasModelRole','Thing','Paper','ModelRole','模型角色：实际采用/对比基线/仅提及')
    if role=='未分类': onto=make_ontology('abox_repair','abox_incomplete','applies_model',abox='backfill applies_model')
    t=task('B','model_role',q,members,spec(f'Paper ⊓ {role}({name})',f'{role_cn2} {name} papers',f'{role_cn2} {name} papers',role,'model','paper'),{'members':members,'numerator':len(members),'denominator':len(members),'answer':len(members)},make_grounding(name,recs,cls='AlgorithmModel',relation='applies_model',role=role,gran=recs[0].get('model_type','')),onto,make_stat(f'model role={role}',f'{name} papers','paper','count',len(members),members),trace('parse model/role','check applies_model + hasModelRole','propose hasModelRole','ground model mention','link paper->model','count paper members','exclude mention-only when applied'))
    t['evidence']=evidence_list(recs); B.append(t)
# B3 data object: 60
for (theme,dtype,rel),recs in sorted(DR.items(), key=lambda kv:-len(kv[1]))[:60]:
    members=sorted({r['doc_id'] for r in recs}); rel_cn={'使用':'使用','提及':'提及','待定':'涉及'}.get(rel,rel)
    q=f'{rel_cn}{dtype}的论文有多少篇？'
    onto=make_ontology('abox_repair','abox_incomplete','reports_variable',abox='backfill reports_variable') if rel=='使用' else make_ontology('ontology_upgrade','relation_missing','mentions','Thing','Paper','Variable','区分提及与报告变量')
    t=task('B','data_object',q,members,spec(f'Paper ⊓ {rel}_variable({dtype})',f'{rel_cn} {dtype} papers',f'{rel_cn} {dtype} papers',rel,theme,'paper'),{'members':members,'numerator':len(members),'denominator':len(members),'answer':len(members)},{'mentions':[{'text':dtype,'doc_id':r['doc_id'],'entity_id':eid('Var',dtype),'class':'Variable','relation':'reports_variable' if rel=='使用' else 'mentions','role':rel,'granularity':theme,'evidence':short(r.get('evidence',''),120)} for r in recs[:4]],'grounding_status':'new_entity_candidate'},onto,make_stat(f'{rel} {dtype}','paper set','paper','count',len(members),members),trace('parse data object/relation','check Variable/reports_variable/mentions','propose mentions if needed','ground variable mention','link paper->variable','count papers','separate mention from report'))
    t['evidence']=evidence_list(recs); B.append(t)
# B4 station type/granularity: 31
TYPE = defaultdict(list)
for (name, role), recs in ST.items():
    for r in recs:
        if r.get('type_norm'):
            TYPE[(name, r['type_norm'])].append(r)
for (name,typ),recs in list(TYPE.items())[:31]:
    members=sorted({r['doc_id'] for r in recs}); q=f'研究站点类型为{typ}的论文有多少篇？'
    onto=make_ontology('abox_repair','abox_incomplete','station_has_type',abox='backfill station_has_type')
    t=task('B','granularity',q,members,spec(f'Paper ⊓ ∃uses_station.(Station="{name}" ⊓ ∃station_has_type.{eid("SType",typ)})',f'{typ} papers',f'{typ} papers','study_site',typ,'paper'),{'members':members,'numerator':len(members),'denominator':len(members),'answer':len(members)},make_grounding(name,recs,gran=typ),onto,make_stat(f'station type={typ}','papers using station','paper','count',len(members),members),trace('parse station/type','check station_has_type','no class proposal; backfill ABox','ground station/type','assert station_has_type','count papers','check type consistency'))
    t['evidence']=evidence_list(recs); B.append(t)
print('B part1',len(B))
# B5 denominator/unit: 40 station names
stations=sorted({k[0] for k in ST})
for name in stations[:40]:
    recs=[r for (n,r) in ST.items() if n==name for r in ST[(n,r)]]
    use=sorted({r['doc_id'] for r in recs}); with_model=[d for d in use if DOCS[d].get('models')]
    q=f'使用{name}的论文中，报告模型的比例是多少？'
    t=task('B','denominator',q,use,spec(f'Paper ⊓ ∃uses_station.Station("{name}")','papers reporting a model',f'papers using {name}','study_or_observation','model','ratio'),{'members':use,'numerator':len(with_model),'denominator':len(use),'answer':len(with_model)/len(use) if use else None},make_grounding(name,recs),make_ontology('none','spec_only','denominator',definition='D(q)=papers using station; unit=paper'),make_stat(f'papers reporting model','papers using {name}','ratio','ratio',len(with_model)/len(use) if use else None,use,len(with_model),len(use)),trace('parse N/D/unit','spec-only no ontology upgrade','none','ground papers','collect models','ratio','check N subset D'))
    t['evidence']=evidence_list(recs); B.append(t)
# B6 alias/dedup: 30 stations with at least two surface forms
alias_names=[]
for name in stations:
    recs=[r for (n,r) in ST.items() if n==name for r in ST[(n,r)]]
    variants=sorted({r.get('name_raw') or name for r in recs})
    if len(variants)>=2: alias_names.append((name,recs,variants))
    if len(alias_names)>=30: break
for name,recs,variants in alias_names:
    members=sorted({r['doc_id'] for r in recs}); q=f'把{name}及其常见写法（如{variants[:2]}）去重后，对应多少篇使用该站点的论文？'
    t=task('B','alias',q,members,spec(f'Paper ⊓ ∃uses_station.(Station ⊓ sameAs("{name}"))','deduplicated station papers','station mentions','study_or_observation',name,'paper'),{'members':members,'numerator':len(members),'denominator':len(members),'answer':len(members)},make_grounding(name,recs,role='study_or_observation'),make_ontology('ontology_upgrade','alias_gap','sameAs','Thing','EcologicalStation','EcologicalStation','站点别名归一'),make_stat('sameAs dedup','station papers','paper','dedup_count',len(members),members),trace('parse alias','check sameAs','propose sameAs','ground alias/entity','link sameAs','dedup count','check duplicate'))
    t['evidence']=evidence_list(recs); B.append(t)
# B7 set operations: 30 station pairs
import itertools
pairs=list(itertools.combinations(stations[:20],2))[:30]
for a,b in pairs:
    da=set(r['doc_id'] for (n,r) in ST.items() if n==a for r in ST[(n,r)]); db=set(r['doc_id'] for (n,r) in ST.items() if n==b for r in ST[(n,r)])
    members=sorted(da&db); q=f'同时使用{a}和{b}的论文有多少篇？'
    t=task('B','set_operation',q,list(da|db),spec(f'Paper ⊓ ∃uses_station.Station("{a}") ⊓ ∃uses_station.Station("{b}")',f'{a}∩{b}','papers using either station','set_operation','mixed','paper'),{'members':members,'numerator':len(members),'denominator':len(members),'answer':len(members)},{'mentions':[{'text':a,'entity_id':STATION_ID.get(a) or eid('Station',a),'class':'EcologicalStation','relation':'uses_station','evidence':'grounded from paper'},{'text':b,'entity_id':STATION_ID.get(b) or eid('Station',b),'class':'EcologicalStation','relation':'uses_station','evidence':'grounded from paper'}],'grounding_status':'resolved'},make_ontology('abox_repair','abox_incomplete','uses_station',abox='backfill both station links'),make_stat(f'papers with {a} AND {b}','papers with either','paper','set_intersection',len(members),members),trace('parse two stations','check uses_station ABox','no proposal; backfill','ground both','link both','intersection','check duplicate'))
    t['evidence']=[{'doc_id':d,'quote':short(DOCS[d].get('title',''))} for d in members[:4]]; B.append(t)
# B8 top-k/trend/crosstab: 20
for i,name in enumerate(stations[:10]):
    recs=[r for (n,r) in ST.items() if n==name for r in ST[(n,r)]]; docs=sorted({r['doc_id'] for r in recs})
    q=f'使用{name}的论文中，出现次数最多的前 3 个模型是哪些？'
    t=task('B','top_k',q,docs,spec(f'Paper ⊓ ∃uses_station.Station("{name}")','model frequency','papers using station','study_site','model','paper'),{'members':docs,'numerator':None,'denominator':None,'answer':'rank model mentions; ties must be reported'},make_grounding(name,recs),make_ontology('abox_repair','abox_incomplete','applies_model',abox='backfill model links'),make_stat('model mentions','papers using station','rank','top_k','tie/rank',docs),trace('parse group/metric','check model links','none','ground models','link papers','rank','tie handling'))
    t['evidence']=evidence_list(recs); B.append(t)
for i,name in enumerate(stations[:5]):
    recs=[r for (n,r) in ST.items() if n==name for r in ST[(n,r)]]; docs=sorted({r['doc_id'] for r in recs})
    for y in [2018,2022]:
        q=f'{y}年前后{name}相关论文数量如何变化？'
        t=task('B','trend',q,docs,spec(f'Paper ⊓ ∃uses_station.Station("{name}") ⊓ year<=> {y}',f'papers before/after {y}','papers using station','study_site','temporal','paper'),{'members':docs,'numerator':None,'denominator':None,'answer':f'count before <{y} vs after >={y}'},make_grounding(name,recs),make_ontology('abox_repair','abox_incomplete','uses_station',abox='backfill year+uses_station'),make_stat(f'year < {y}','year >= {y}','paper','trend','count pair',docs),trace('parse year/station','check year/uses_station','none','ground year','link year','trend','check year coverage'))
        t['evidence']=evidence_list(recs); B.append(t)
for i in range(5):
    q=['网站与站点类型的交叉表中，各组合的论文数是多少？','数据主题与模型类型的交叉表中，各组合的论文数是多少？','年份与模型类型的交叉表中，各组合的论文数是多少？','数据用途与站点类型的交叉表中，各组合的论文数是多少？','新旧网站在站点类型上的差异如何？'][i]
    all_docs=list(DOCS)
    t=task('B','crosstab',q,all_docs,spec('Paper','crosstab cells','all papers','mixed','mixed','paper'),{'members':all_docs,'numerator':None,'denominator':None,'answer':'matrix of non-zero cells'},{'mentions':[],'grounding_status':'grounding_required'},make_ontology('abox_repair','abox_incomplete','grouping_relations',abox='backfill group-by fields'),make_stat('group keys','all papers','paper','crosstab','matrix',all_docs),trace('parse group-by','check grouping fields','none','ground grouping entities','link fields','crosstab','sum cells'))
    t['evidence']=[{'doc_id':d,'quote':short(DOCS[d].get('title',''))} for d in all_docs[:3]]; B.append(t)
print('B part2',len(B))
# B9 ontology masking: 20 nested tasks
mask_targets=[('AlpineMeadow','class','研究站点类型为高寒草甸的论文有多少篇？'),('station_has_type','relation','区分草地与高寒草甸的论文统计'),('uses_station','relation','海北研究站点论文数'),('applies_model','relation','实际采用随机森林的论文数'),('hasStationRole','role','研究站点/观测来源论文数'),('hasModelRole','role','实际采用/仅提及论文数'),('sameAs','relation','海北别名去重论文数'),('supported_by','relation','有证据支持的统计结论'),('reports_variable','relation','报告土壤呼吸的论文数'),('mentions','relation','提到土壤呼吸的论文数')]
for i,(target,kind,main) in enumerate(mask_targets*2):
    if i>=20: break
    q=f'如果移除本体元素 {target}，系统还能正确回答“{main}”吗？'
    onto=make_ontology('ontology_upgrade',{'class':'class_missing','relation':'relation_missing','role':'role_schema_missing'}[kind],target,parent='StationType' if target in ('AlpineMeadow','station_has_type') else 'Thing',domain='Paper',range_='EcologicalStation' if 'station' in target else 'xsd:string',definition=f'恢复/新增 {target}')
    t=task('B','masking',q,['doc002','doc010','ndoc006'],spec('Paper','masked question target','masked denominator','masked','masked','paper'),{'members':[],'numerator':None,'denominator':None,'answer':'cannot answer without restoration'},{'mentions':[],'grounding_status':'intervention'},onto,make_stat('masked','masked','paper','unanswerable',None,[]),trace('parse main question','detect masked element','propose restore/add','n/a','n/a','cannot compute','must block silent fallback'),'expert_design')
    t['evidence']=[{'doc_id':d,'quote':short(DOCS[d].get('title',''))} for d in t['source_docs']]; B.append(t)
# B10 negative/absence: 30 stations without model
for name in stations[:30]:
    recs=[r for (n,r) in ST.items() if n==name for r in ST[(n,r)]]
    use=sorted({r['doc_id'] for r in recs}); no_model=[d for d in use if not DOCS[d].get('models')]
    q=f'使用{name}但没有报告任何模型的论文有多少篇？'
    t=task('B','negative_absence',q,use,spec(f'Paper ⊓ ∃uses_station.Station("{name}") ⊓ ¬∃applies_model.AlgorithmModel','papers without a model',f'papers using {name}','study_or_observation','Grassland','paper'),{'members':no_model,'numerator':len(no_model),'denominator':len(use),'answer':len(no_model)},make_grounding(name,recs),make_ontology('abox_repair','abox_incomplete','applies_model',abox='backfill model links; absence rule in spec'),make_stat('papers without model',f'papers using {name}','paper','absence_count',len(no_model),no_model,len(no_model),len(use)),trace('parse station/absence','check uses_station/applies_model','absence rule in spec','ground station','link papers','filter no-model','avoid false absence'))
    t['evidence']=evidence_list(recs); B.append(t)
# B11 station-model intersection: 25 evidence-backed pairs
model_names=[m for (m,r) in MR if r=='实际采用']
added=0
for name in stations[:10]:
    recs=[r for (n,r) in ST.items() if n==name for r in ST[(n,r)]]; use=sorted({r['doc_id'] for r in recs})
    for model in model_names[:5]:
        md_docs=sorted({r['doc_id'] for (m,r),rs in MR.items() if m==model for r in rs})
        members=sorted(set(use)&set(md_docs))
        if not members: continue
        q=f'同时使用{name}且实际采用{model}的论文有多少篇？'
        t=task('B','station_model_intersection',q,members,spec(f'Paper ⊓ ∃uses_station.Station("{name}") ⊓ ∃applies_model.{model}','station ∩ applied model',f'papers using {name}','study_site','model','paper'),{'members':members,'numerator':len(members),'denominator':len(use),'answer':len(members)},{'mentions':[{'text':name,'entity_id':STATION_ID.get(name) or eid('Station',name),'class':'EcologicalStation','relation':'uses_station','evidence':'station evidence'},{'text':model,'entity_id':eid('Model',model),'class':'AlgorithmModel','relation':'applies_model','evidence':'model evidence'}],'grounding_status':'resolved'},make_ontology('abox_repair','abox_incomplete','uses_station/applies_model',abox='backfill station and model links'),make_stat(f'{name} AND {model}',f'papers using {name}','paper','set_intersection',len(members),members),trace('parse station/model','check links','none','ground both','link both','intersection','dedup'))
        t['evidence']=[{'doc_id':d,'quote':short(DOCS[d].get('title',''))} for d in members[:3]]; B.append(t); added+=1
        if added>=25: break
    if added>=25: break
print('B part3',len(B))

# B12 station-specific type: 30
for name in stations[:30]:
    recs=[r for (n,r) in ST.items() if n==name for r in ST[(n,r)]]
    if not recs: continue
    typ=recs[0].get('type_norm') or '未知'
    members=sorted({r['doc_id'] for r in recs})
    q=f'研究站点{name}的生态系统类型为{typ}的论文有多少篇？'
    t=task('B','station_type',q,members,spec(f'Paper ⊓ ∃uses_station.(Station="{name}" ⊓ ∃station_has_type.{typ})',f'{name} {typ} papers',f'{name} papers','study_site',typ,'paper'),{'members':members,'numerator':len(members),'denominator':len(members),'answer':len(members)},make_grounding(name,recs,gran=typ),make_ontology('abox_repair','abox_incomplete','station_has_type',abox='backfill station_has_type'),make_stat(f'station={name},type={typ}',f'{name} papers','paper','count',len(members),members),trace('parse station/type','check station_has_type ABox','no class proposal; backfill','ground station/type','assert type','count','check type consistency'))
    t['evidence']=evidence_list(recs); B.append(t)
# B13 station role union/difference: 15
for a,b in pairs[:15]:
    da=set(r['doc_id'] for (n,r) in ST.items() if n==a for r in ST[(n,r)]); db=set(r['doc_id'] for (n,r) in ST.items() if n==b for r in ST[(n,r)])
    members=sorted(da|db); q=f'使用{a}或{b}的论文共有多少篇？'
    t=task('B','role_union',q,members,spec(f'Paper ⊓ (∃uses_station.Station("{a}") ∨ ∃uses_station.Station("{b}"))',f'{a}∪{b}',f'{a} or {b} papers','role_union','mixed','paper'),{'members':members,'numerator':len(members),'denominator':len(members),'answer':len(members)},{'mentions':[{'text':a,'entity_id':STATION_ID.get(a) or eid('Station',a),'class':'EcologicalStation','relation':'uses_station','evidence':'station evidence'},{'text':b,'entity_id':STATION_ID.get(b) or eid('Station',b),'class':'EcologicalStation','relation':'uses_station','evidence':'station evidence'}],'grounding_status':'resolved'},make_ontology('abox_repair','abox_incomplete','uses_station',abox='backfill both station links'),make_stat(f'{a} OR {b}',f'{a} or {b} papers','paper','set_union',len(members),members),trace('parse two stations','check uses_station','none','ground both','link both','union','dedup'))
    t['evidence']=[{'doc_id':d,'quote':short(DOCS[d].get('title',''))} for d in members[:3]]; B.append(t)
print('B part4',len(B))

# B14 station-model intersection: 20 direct pairs
actual_models=defaultdict(set)
for d,x in DOCS.items():
    for m in x.get('models',[]):
        if m.get('name_norm') and m.get('role')=='实际采用':
            actual_models[m['name_norm']].add(d)
added=0
for name in stations[:20]:
    recs=[r for (n,r) in ST.items() if n==name for r in ST[(n,r)]]
    if not recs: continue
    use=sorted({r['doc_id'] for r in recs})
    for model,mdocs in actual_models.items():
        members=sorted(set(use)&mdocs)
        if not members: continue
        q=f'使用{name}且实际采用{model}的论文有多少篇？'
        t=task('B','station_model_intersection',q,members,spec(f'Paper ⊓ ∃uses_station.Station("{name}") ⊓ ∃applies_model.{model}','station ∩ applied model',f'papers using {name}','study_site','model','paper'),{'members':members,'numerator':len(members),'denominator':len(use),'answer':len(members)},{'mentions':[{'text':name,'entity_id':STATION_ID.get(name) or eid('Station',name),'class':'EcologicalStation','relation':'uses_station','evidence':'station evidence'},{'text':model,'entity_id':eid('Model',model),'class':'AlgorithmModel','relation':'applies_model','evidence':'model evidence'}],'grounding_status':'resolved'},make_ontology('abox_repair','abox_incomplete','uses_station/applies_model',abox='backfill station/model links'),make_stat(f'{name} AND {model}',f'papers using {name}','paper','set_intersection',len(members),members),trace('parse station/model','check both links','none','ground both','link both','intersection','dedup'))
        t['evidence']=[{'doc_id':d,'quote':short(DOCS[d].get('title',''))} for d in members[:3]]; B.append(t); added+=1
        if added>=20: break
    if added>=20: break
print('B part5',len(B))

# B15 station role difference: 20
added=0
for a,b in pairs:
    da=set(r['doc_id'] for (n,r) in ST.items() if n==a for r in ST[(n,r)]); db=set(r['doc_id'] for (n,r) in ST.items() if n==b for r in ST[(n,r)])
    members=sorted(da-db)
    if not members: continue
    q=f'使用{a}但不使用{b}的论文有多少篇？'
    t=task('B','role_difference',q,members,spec(f'Paper ⊓ ∃uses_station.Station("{a}") ⊓ ¬∃uses_station.Station("{b}")',f'{a}\\{b}',f'{a} papers','role_difference','mixed','paper'),{'members':members,'numerator':len(members),'denominator':len(da),'answer':len(members)},{'mentions':[{'text':a,'entity_id':STATION_ID.get(a) or eid('Station',a),'class':'EcologicalStation','relation':'uses_station','evidence':'station evidence'},{'text':b,'entity_id':STATION_ID.get(b) or eid('Station',b),'class':'EcologicalStation','relation':'uses_station','evidence':'station evidence'}],'grounding_status':'resolved'},make_ontology('abox_repair','abox_incomplete','uses_station',abox='backfill both station links'),make_stat(f'{a} AND NOT {b}',f'{a} papers','paper','set_difference',len(members),members),trace('parse two stations','check uses_station','none','ground both','link both','difference','negative check'))
    t['evidence']=[{'doc_id':d,'quote':short(DOCS[d].get('title',''))} for d in members[:3]]; B.append(t); added+=1
    if added>=20: break
print('B part6',len(B))

# B16 alias fallback: 20
for name in stations[:20]:
    recs=[r for (n,r) in ST.items() if n==name for r in ST[(n,r)]]
    if not recs: continue
    members=sorted({r['doc_id'] for r in recs})
    q=f'把{name}及其常见别名去重后，对应多少篇使用该站点的论文？'
    t=task('B','alias',q,members,spec(f'Paper ⊓ ∃uses_station.(Station ⊓ sameAs("{name}"))','deduplicated station papers','station mentions','study_or_observation',name,'paper'),{'members':members,'numerator':len(members),'denominator':len(members),'answer':len(members)},make_grounding(name,recs,role='study_or_observation'),make_ontology('ontology_upgrade','alias_gap','sameAs','Thing','EcologicalStation','EcologicalStation','站点别名归一'),make_stat('sameAs dedup','station papers','paper','dedup_count',len(members),members),trace('parse alias','check sameAs','propose sameAs','ground alias/entity','link sameAs','dedup count','check duplicate'))
    t['evidence']=evidence_list(recs); B.append(t)
print('B part7',len(B))

# Tier C: 120 stress combinations (station x role x type)
C=[]
for (name,role),recs in list(ST.items())[:60]:
    typ=recs[0].get('type_norm') or '未知'
    for r in [role,'研究站点','观测来源']:
        if len(C)>=120: break
        members=sorted({x['doc_id'] for x in recs}); q=f'把{name}作为{r}、且站点类型为{typ}的论文有多少篇？'
        t=task('C','stress_combo',q,members,spec(f'Paper ⊓ ∃uses_station.(Station="{name}" ⊓ role={r}) ⊓ ∃station_has_type.{typ}',f'{typ} {r} papers',f'{name} {r} papers',r,typ,'paper'),{'members':members,'numerator':None,'denominator':None,'answer':'stress; needs verification'},make_grounding(name,recs,role=r,gran=typ),make_ontology('ontology_upgrade','role_schema_missing','hasStationRole','Thing','Paper','StationRole','stress combination'),make_stat(f'{r}+{typ}',f'{name} papers','paper','count','needs verification',members),trace('parse station/role/type','check role + ABox','propose role','ground station','assert role/type','stress count','audit'),'stress')
        t['evidence']=evidence_list(recs); C.append(t)
    if len(C)>=120: break

# de-duplicate by normalized question
def norm(q): return re.sub(r'[\s，。？?、：:；;“”"\'（）()]','',q or '')
seen=set(); all_tasks=[]
for t in A+B+C:
    n=norm(t['question_zh'])
    if n in seen: continue
    seen.add(n); all_tasks.append(t)
for i,t in enumerate(all_tasks,1): t['id']=f'D{i:04d}'
# save
outdir=P/'tiers'; outdir.mkdir(exist_ok=True)
for tier,rows in [('A',[t for t in all_tasks if t['tier']=='A']),('B',[t for t in all_tasks if t['tier']=='B']),('C',[t for t in all_tasks if t['tier']=='C'])]:
    (outdir/f'tier_{tier}.jsonl').write_text('\n'.join(json.dumps(t,ensure_ascii=False) for t in rows),encoding='utf-8')
    (outdir/f'tier_{tier}.json').write_text(json.dumps({'count':len(rows),'tasks':rows},ensure_ascii=False,indent=2),encoding='utf-8')
(P/'tiers'/'dataset_v2.jsonl').write_text('\n'.join(json.dumps(t,ensure_ascii=False) for t in all_tasks),encoding='utf-8')
(P/'tiers'/'build_stats.json').write_text(json.dumps({'total':len(all_tasks),'by_tier':dict(Counter(t['tier'] for t in all_tasks)),'by_group':dict(Counter(t['group'] for t in all_tasks))},ensure_ascii=False,indent=2),encoding='utf-8')
print('TOTAL',len(all_tasks),Counter(t['tier'] for t in all_tasks),Counter(t['group'] for t in all_tasks))
