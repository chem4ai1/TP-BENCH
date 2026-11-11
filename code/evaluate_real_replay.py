import json, collections
from pathlib import Path
from core_v3 import config, data_loader, object_inventory, evidence_builder, schema_checker, population_engine

ann, md, _, _ = data_loader.load_resources(); inv=object_inventory.build_inventory(ann)
D=[json.loads(l) for l in (config.DATA/'results_v4/dataset_v3_coverage.jsonl').read_text(encoding='utf-8').splitlines()]
C=[t for t in D if t['tier']=='C']
v1=json.loads((config.DATA/'canonical/ontology_v1_empty.json').read_text(encoding='utf-8'))
v2=json.loads((config.DATA/'canonical/ontology_v2_backfilled.json').read_text(encoding='utf-8'))
s1,s2=schema_checker.schema_state(v1),schema_checker.schema_state(v2)
OUT=config.DATA/'results_v4'; OUT.mkdir(exist_ok=True)
rows=[]; trans=collections.Counter()
for t in C:
    x,y=data_loader.split_task(t); ev=evidence_builder.build_evidence(x,inv,ann,md)
    a1=schema_checker.stage_a(x,ev,s1,{}); a2=schema_checker.stage_a(x,ev,s2,{})
    p1=population_engine.solve(x,ev,a1,ann,md,inv,{'replay_enabled':False})
    p2=population_engine.solve(x,ev,a2,ann,md,inv,{})
    pre='explicit_abstain' if a1['trigger_class'] in ('abox_repair','ontology_upgrade') else ('silent_zero' if p1.get('answer')==0 else 'answerable')
    post='answerable' if not p2.get('abstain') else 'abstain'
    comp=1 if pre=='explicit_abstain' and post=='answerable' else 0
    silent=1 if pre=='silent_zero' and isinstance(p2.get('answer'),(int,float)) and p2['answer']>0 else 0
    regress=1 if pre=='answerable' and p1.get('answer')!=p2.get('answer') else 0
    trans[(a1['trigger_class'],a2['trigger_class'])]+=1
    rows.append({'id':t['id'],'question':x['question'],'v1_trigger':a1['trigger_class'],'v2_trigger':a2['trigger_class'],'pre_status':pre,'post_status':post,'v1_answer':p1.get('answer'),'v2_answer':p2.get('answer'),'gold_answer':y['answer'],'comparability':comp,'silent_zero':silent,'regression':regress})
n=len(rows)
summary={'n':n,'comparability_audit':sum(r['comparability'] for r in rows)/n,'silent_zero_rate':sum(r['silent_zero'] for r in rows)/n,'regression_rate':sum(r['regression'] for r in rows)/n,'trigger_transitions':{f'{a}->{b}':c for (a,b),c in trans.items()},'v1_version':v1['version'],'v2_version':v2['version'],'v1_core_abox':0,'v2_core_abox':sum(s2['abox'].get(k,0) for k in ['uses_station','station_has_type','applies_model','reports_variable','mentions','hasStationRole','hasModelRole'])}
(OUT/'real_replay_results.json').write_text(json.dumps({'summary':summary,'rows':rows},ensure_ascii=False,indent=2),encoding='utf-8')
L=['# P1 真实 ontology v1/v2 replay\n',f"- v1: `{v1['version']}`，核心 ABox=0",f"- v2: `{v2['version']}`，核心 ABox={summary['v2_core_abox']}",'','| 指标 | 值 |','|---|---:|']+[f'| {k} | {v:.3f} |' for k,v in summary.items() if isinstance(v,(int,float)) and k not in ('n','v2_core_abox')]
L+=['\n## Trigger transitions\n','| transition | n |','|---|---:|']+[f'| {k} | {v} |' for k,v in summary['trigger_transitions'].items()]
L+=['\n## 说明\n','- v1 为空 ABox 时显式 abstain；v2 回填后给出可计算答案。','- silent zero 指 v1 直接返回 0 而没有 abstain，是最危险的不可比情况。','- regression 指 v1 已有可回答结果但 v2 改变答案且无版本解释。']
(OUT/'real_replay_results.md').write_text('\n'.join(L),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
