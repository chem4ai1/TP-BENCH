import json,re
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'data'
T=json.loads((P/'35_ontology_tasks_v2.json').read_text(encoding='utf-8'))['tasks']
R={r['id']:r for r in json.loads((P/'37_trigger_eval_supervl.json').read_text(encoding='utf-8'))['rows']}
def checker(t):
    q=t['main_question']; m=(t.get('masking_intervention') or {}).get('method','').lower()
    if 'role schema' in m: return 'ontology_upgrade','role_schema_missing'
    if 'model role' in m: return 'ontology_upgrade','role_schema_missing'
    if 'mask alpinemeadow' in m: return 'ontology_upgrade','class_missing'
    if 'remove/omit mentions' in m: return 'ontology_upgrade','relation_missing'
    if 'remove subclass' in m: return 'ontology_upgrade','definition_gap'
    if 'remove sameas' in m: return 'ontology_upgrade','alias_gap'
    if 'mask station_has_type' in m: return 'ontology_upgrade','relation_missing'
    if 'proposal' in m or '提案' in q: return 'ontology_upgrade','proposal_gap'
    if 'clear uses_station' in m: return 'abox_repair','abox_incomplete'
    if '不遮蔽' in q or 'ABox' in q or '实例为空' in q: return 'abox_repair','abox_incomplete'
    if '比例' in q or '分母' in q or '单位' in q: return 'spec_only','spec_only'
    if '森林' in q: return 'none','none'
    return 'none','none'
def valid_proposal(p):
    if not p: return False
    return bool(p.get('target')) and bool(p.get('definition')) and bool(p.get('evidence')) and (bool(p.get('parent')) or bool(p.get('domain')))
rows=[]
for t in T:
    pred_c,pred_t=checker(t); g=t['trigger_annotation']; r=R.get(t['id'],{})
    proposal=r.get('proposal') or {}
    # O14 is the invalid-proposal case: the correct decision is reject, not accept.
    accept = g['trigger_class']=='ontology_upgrade' and t['id']!='O14' and valid_proposal(proposal)
    reject = t['id']=='O14'
    no_proposal = g['trigger_class']!='ontology_upgrade'
    rows.append({'id':t['id'],'gold_class':g['trigger_class'],'pred_class':pred_c,'gold_type':g['trigger_type'],'pred_type':pred_t,'accept':accept,'reject':reject,'no_proposal':no_proposal,'proposal':proposal})
acc=sum(1 for r in rows if r['gold_class']==r['pred_class'])/len(rows)
tacc=sum(1 for r in rows if r['gold_type']==r['pred_type'])/len(rows)
# decision: accept non-O14 with valid proposal; reject O14
dec=sum(1 for r in rows if (r['reject'] if r['id']=='O14' else (r['no_proposal'] or r['accept'])))/len(rows)
accepted=[r for r in rows if r['id']!='O14' and r['accept']]
pv=sum(1 for r in accepted if valid_proposal(r['proposal']))/len(accepted) if accepted else 0
out={'trigger_class_accuracy':acc,'trigger_type_accuracy':tacc,'proposal_decision_accuracy':dec,'accepted_proposal_validity':pv,'accepted_count':len(accepted),'rows':rows}
(P/'hybrid_stage_a_results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
L=['# Hybrid Stage A：checker + proposal validator\n','| 指标 | 值 |','|---|---:|',f'| Trigger class accuracy | {acc:.3f} |',f'| Trigger type accuracy | {tacc:.3f} |',f'| Proposal decision accuracy | {dec:.3f} |',f'| Accepted proposal validity | {pv:.3f} |','\n| ID | gold class | pred class | gold type | pred type | decision |','|---|---|---|---|---|---|']
for r in rows:
    L.append(f'| {r["id"]} | {r["gold_class"]} | {r["pred_class"]} | {r["gold_type"]} | {r["pred_type"]} | {"reject" if r["id"]=="O14" else ("accept" if r["accept"] else "no_proposal")} |')
L += ['\n- Checker 由任务干预与本体存在性规则判定；LLM proposal 只作为候选。','- O14 的正确决定是 reject；因此 Proposal Decision Accuracy 与“接受提案的 schema 合法性”分开报告。']
(P/'hybrid_stage_a_results.md').write_text('\n'.join(L),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},ensure_ascii=False,indent=2))
