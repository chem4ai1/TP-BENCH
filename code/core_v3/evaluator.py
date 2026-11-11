import json, math, re
from collections import defaultdict

VALID_TRIGGERS = {'ontology_upgrade', 'abox_repair', 'spec_only', 'none'}

def _num(x):
    try: return float(x)
    except Exception: return None

def _set_of_cells(v):
    if not isinstance(v, list): return set()
    return {json.dumps(c, ensure_ascii=False, sort_keys=True) for c in v}

def answer_score(y, pred):
    g, p, gt = y.get('answer'), pred.get('answer'), y.get('gold_type')
    if pred.get('abstain') and gt not in ('expert_behavior',): return 0.0
    if gt in ('count', 'ratio', 'bool'):
        a, b = _num(g), _num(p)
        return 1.0 if a is not None and b is not None and abs(a-b) < 0.02 else 0.0
    if gt == 'structured' and isinstance(g, dict):
        if not isinstance(p, dict): return 0.0
        scores = []
        for k in ('ratio_all','ratio_station','denom_all','denom_station','before','after','threshold'):
            if k in g and k in p:
                a,b=_num(g[k]),_num(p[k]); scores.append(1.0 if a is not None and b is not None and abs(a-b)<0.02 else 0.0)
        if 'cells' in g:
            a,b=_set_of_cells(g['cells']),_set_of_cells(p.get('cells'))
            scores.append(len(a&b)/max(1,len(a|b)) if (a or b) else 1.0)
        if 'top3' in g:
            a={str(x[0]) if isinstance(x,(list,tuple)) else str(x) for x in g['top3']}
            b={str(x[0]) if isinstance(x,(list,tuple)) else str(x) for x in p.get('top3',[])}
            scores.append(len(a&b)/max(1,len(a|b)) if (a or b) else 1.0)
        if 'decision' in g:
            scores.append(1.0 if str(g.get('decision'))==str(p.get('decision')) else 0.0)
        if 'holds' in g:
            scores.append(1.0 if bool(g.get('holds'))==bool(p.get('holds')) else 0.0)
        return sum(scores)/len(scores) if scores else 0.0
    if gt == 'list':
        a,b=set(map(str,g or [])),set(map(str,p or [])); return len(a&b)/max(1,len(a|b)) if (a or b) else 1.0
    if gt in ('text','expert_behavior'):
        gs=str(g or '').strip(); ps=json.dumps(p,ensure_ascii=False) if isinstance(p,(dict,list)) else str(p or '')
        if not gs: return 0.0
        if gs in ps or any(tok and tok in ps for tok in ('reject','blocked','cannot','abstain')): return 1.0
        return 0.0
    return 0.0

def candidate_scores(y, pred):
    g=set(y.get('members') or []); p=set(pred.get('members') or [])
    if not g and not p: return 1.0,1.0,1.0
    tp=len(g&p); pr=tp/len(p) if p else 0.0; rc=tp/len(g) if g else 0.0
    f=2*pr*rc/(pr+rc) if pr+rc else 0.0
    return pr,rc,f

def evaluate_one(y, stage_a, pred):
    cp,cr,cf=candidate_scores(y,pred)
    gt=y.get('trigger_class')
    trig = gt in VALID_TRIGGERS
    return {
        'id': y.get('id'), 'group': y.get('group'), 'tier': y.get('tier'),
        'gold_type': y.get('gold_type'), 'answer_score': answer_score(y,pred),
        'candidate_p': cp, 'candidate_r': cr, 'candidate_f1': cf,
        'trigger_valid': trig,
        'trigger_ok': 1 if trig and stage_a.get('trigger_class')==gt else 0,
        'trigger_type_ok': 1 if trig and y.get('trigger_type') and stage_a.get('trigger_type')==y.get('trigger_type') else 0,
        'abstain': bool(pred.get('abstain')),
        'pred_answer': pred.get('answer'),
        'pred_trigger': stage_a.get('trigger_class'),
        'gold_trigger': gt,
    }

def aggregate(rows):
    n=len(rows) or 1
    trig_rows=[r for r in rows if r['trigger_valid']]
    out={
        'n': len(rows),
        'answer_score': sum(r['answer_score'] for r in rows)/n,
        'candidate_precision': sum(r['candidate_p'] for r in rows)/n,
        'candidate_recall': sum(r['candidate_r'] for r in rows)/n,
        'candidate_f1': sum(r['candidate_f1'] for r in rows)/n,
        'abstain_rate': sum(1 for r in rows if r['abstain'])/n,
        'trigger_accuracy': sum(r['trigger_ok'] for r in trig_rows)/len(trig_rows) if trig_rows else None,
        'trigger_type_accuracy': sum(r['trigger_type_ok'] for r in trig_rows)/len(trig_rows) if trig_rows else None,
        'trigger_n': len(trig_rows),
    }
    by=defaultdict(list)
    for r in rows: by[r['group']].append(r)
    out['by_group']={k:{'n':len(v),'answer_score':sum(x['answer_score'] for x in v)/len(v),
                        'candidate_f1':sum(x['candidate_f1'] for x in v)/len(v),
                        'trigger_accuracy':sum(x['trigger_ok'] for x in v if x['trigger_valid'])/max(1,sum(1 for x in v if x['trigger_valid']))}
                     for k,v in by.items()}
    return out

EXPERIMENT_REGISTRY = {
  'A0_Full': {'kind':'direct','flags':{}},
  'A1_NoStageA': {'kind':'direct','flags':{'use_spec':False,'schema_audit_enabled':False}},
  'A2_NoPopulationSpec': {'kind':'direct','flags':{'use_spec':False}},
  'A3_NoRole': {'kind':'direct','flags':{'role_enabled':False}},
  'A4_NoGranularity': {'kind':'direct','flags':{'granularity_enabled':False}},
  'A5_NoDenominator': {'kind':'direct','flags':{'denominator_enabled':False}},
  'A6_NoSchemaAudit': {'kind':'direct','flags':{'schema_audit_enabled':False}},
  'A7_NoProposal': {'kind':'direct','flags':{'proposal_enabled':False}},
  'A8_NoApproval': {'kind':'direct','flags':{'approval_enabled':False}},
  'A9_NoAuditor': {'kind':'direct','flags':{'auditor_enabled':False}},
  'A10_NoReplay': {'kind':'direct','flags':{'replay_enabled':False}},
  'B1_RAG_proxy': {'kind':'proxy','note':'historical RAG baseline, not v3 direct variant'},
  'B2_MentionAll_proxy': {'kind':'proxy','note':'historical mention-all baseline'},
  'A10_old_simulation': {'kind':'simulation','note':'old v1/v2 was hardcoded, replaced by A10_NoReplay'},
}
