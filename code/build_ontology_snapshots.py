import json, hashlib, copy
from pathlib import Path
from collections import Counter
from core_v3 import config

ann = {d['doc_id']: d for d in [json.loads(l) for l in config.ANNOTATIONS.read_text(encoding='utf-8').splitlines()]}
onto = json.loads(config.ONTOLOGY.read_text(encoding='utf-8'))
OUT = config.DATA/'canonical'; OUT.mkdir(exist_ok=True)
CORE = {'uses_station','station_has_type','applies_model','reports_variable','supported_by'}

def eid(prefix,name): return prefix+'_'+hashlib.md5(str(name).encode('utf-8')).hexdigest()[:10]
def ind(i,cls,attrs,evidence):
    return {'id':i,'class':cls,'attributes':attrs,'source':'p0_p2_backfill','evidence':evidence,'created_at':'2026-11-05T00:00:00'}

v1 = copy.deepcopy(onto)
v1['version']='v2.1.460-empty'
v1['relation_instances']=[r for r in v1.get('relation_instances',[]) if r.get('relation') not in CORE]

v2 = copy.deepcopy(onto)
v2['version']='v2.1.461-backfilled'
v2['relation_instances']=[r for r in v2.get('relation_instances',[]) if r.get('relation') not in CORE]
existing={i['id'] for i in v2.get('individuals',[])}
rels={r['id'] for r in v2.get('relations',[])}
for rid,label,domain,rangev,desc in [
 ('hasStationRole','站点角色','Paper','StationRole','论文与生态站点之间的角色'),
 ('hasModelRole','模型角色','Paper','ModelRole','论文与模型之间的角色'),
 ('mentions','提及','Paper','Thing','论文提及某实体'),
]:
    if rid not in rels:
        v2['relations'].append({'id':rid,'label':label,'domain':domain,'range':rangev,'desc':desc,'status':'proposed','source':'p0_p2_upgrade'})
        rels.add(rid)

counts=Counter()
for d,x in ann.items():
    paper='Paper_'+d
    for s in x.get('stations',[]):
        name=s.get('name_norm') or s.get('name_raw')
        typ=s.get('type_norm')
        role=s.get('role')
        if not name or s.get('relation')!='使用': continue
        sid='Station_'+hashlib.md5(name.encode('utf-8')).hexdigest()[:10]
        if sid not in existing:
            v2['individuals'].append(ind(sid,'EcologicalStation',{'name':name},s.get('evidence',''))); existing.add(sid)
        ev=str(s.get('evidence',''))[:180]
        v2['relation_instances'].append({'relation':'uses_station','subject':paper,'object':sid,'evidence':ev,'source':'p0_p2_backfill','created_at':'2026-11-05T00:00:00'}); counts['uses_station']+=1
        if role and role!='未分类':
            v2['relation_instances'].append({'relation':'hasStationRole','subject':paper,'object':sid,'role':role,'evidence':ev,'source':'p0_p2_backfill','created_at':'2026-11-05T00:00:00'}); counts['hasStationRole']+=1
        if typ:
            tid='SType_'+hashlib.md5(typ.encode('utf-8')).hexdigest()[:10]
            if tid not in existing:
                v2['individuals'].append(ind(tid,'StationType',{'name':typ},s.get('evidence',''))); existing.add(tid)
            v2['relation_instances'].append({'relation':'station_has_type','subject':sid,'object':tid,'evidence':ev,'source':'p0_p2_backfill','created_at':'2026-11-05T00:00:00'}); counts['station_has_type']+=1
    for m in x.get('models',[]):
        name=m.get('name_norm') or m.get('name_raw')
        if not name: continue
        mid='Model_'+hashlib.md5(name.encode('utf-8')).hexdigest()[:10]
        if mid not in existing:
            v2['individuals'].append(ind(mid,'AlgorithmModel',{'name':name},m.get('evidence',''))); existing.add(mid)
        ev=str(m.get('evidence',''))[:180]
        v2['relation_instances'].append({'relation':'applies_model','subject':paper,'object':mid,'evidence':ev,'source':'p0_p2_backfill','created_at':'2026-11-05T00:00:00'}); counts['applies_model']+=1
        role=m.get('role')
        if role and role!='未分类':
            v2['relation_instances'].append({'relation':'hasModelRole','subject':paper,'object':mid,'role':role,'evidence':ev,'source':'p0_p2_backfill','created_at':'2026-11-05T00:00:00'}); counts['hasModelRole']+=1
    for u in x.get('data_uses',[]):
        name=u.get('data_type_norm') or u.get('theme')
        if not name: continue
        vid='Var_'+hashlib.md5(name.encode('utf-8')).hexdigest()[:10]
        if vid not in existing:
            v2['individuals'].append(ind(vid,'Variable',{'name':name},u.get('evidence',''))); existing.add(vid)
        ev=str(u.get('evidence',''))[:180]
        rel='reports_variable' if u.get('relation')=='使用' else 'mentions'
        v2['relation_instances'].append({'relation':rel,'subject':paper,'object':vid,'evidence':ev,'source':'p0_p2_backfill','created_at':'2026-11-05T00:00:00'}); counts[rel]+=1

(OUT/'ontology_v1_empty.json').write_text(json.dumps(v1,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'ontology_v2_backfilled.json').write_text(json.dumps(v2,ensure_ascii=False,indent=2),encoding='utf-8')
manifest={'v1':{'version':v1['version'],'relation_instances':len(v1['relation_instances']),'core_counts':{k:0 for k in CORE}},
          'v2':{'version':v2['version'],'relation_instances':len(v2['relation_instances']),'core_counts':dict(counts),'individuals':len(v2['individuals']),'relations':len(v2['relations'])}}
(OUT/'snapshot_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(manifest,ensure_ascii=False,indent=2))
