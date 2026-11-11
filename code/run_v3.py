import json, hashlib, time, collections
from pathlib import Path
from core_v3 import config, data_loader, object_inventory, evidence_builder, schema_checker, population_engine, evaluator, strict_metrics

config.RESULTS.mkdir(parents=True, exist_ok=True)

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()[:16]

def main():
    ann, md, onto, tasks = data_loader.load_resources()
    inv = object_inventory.build_inventory(ann)
    state = schema_checker.schema_state(onto)
    pairs = [data_loader.split_task(t) for t in tasks]
    variants = {k:v for k,v in evaluator.EXPERIMENT_REGISTRY.items() if v['kind']=='direct'}
    membership_ids = {y['id'] for x,y in pairs if x['group'] in {'role_variant','model_role','granularity','granularity_pair'} and y['status']=='verified'}
    all_results = {}

    for name, meta in variants.items():
        flags = dict(meta.get('flags') or {})
        rows=[]; strict_rows=[]; t0=time.time()
        for x,y in pairs:
            use_spec = flags.get('use_spec', True)
            x_input = dict(x)
            if not use_spec: x_input['population_spec'] = {}
            ev = evidence_builder.build_evidence(x_input, inv, ann, md)
            a = schema_checker.stage_a(x_input, ev, state, flags)
            pred = population_engine.solve(x_input, ev, a, ann, md, inv, flags)
            pred_obj = {
                'status': 'abstain' if pred.get('abstain') else 'ok',
                'answer': pred.get('answer'),
                'members': pred.get('members') or [],
                'denominator_count': pred.get('denominator'),
            }
            ref = {'id': y['id'], 'group': y['group'],
                   'gold': {'answer': y['answer'], 'members': list(y['members']),
                            'denominator': y['denominator'], 'denominator_members': y.get('denominator_members') or []},
                   'evaluation': y.get('evaluation') or {'answer':True,'members':True,'denominator_count':False,'reasons':[]}}
            sr = strict_metrics.evaluate(ref, pred_obj)
            sr['pred_members'] = sorted(pred.get('members') or [])
            sr['pred_unit'] = pred.get('unit')
            sr['pred_answer'] = pred.get('answer')
            sr['trigger_gold'] = y.get('trigger_class')
            sr['trigger_pred'] = a.get('trigger_class')
            sr['trace'] = pred.get('trace')
            sr['review_flags'] = pred.get('review_flags')
            strict_rows.append(sr)
            rows.append(sr)
        agg_all = strict_metrics.summarize(strict_rows)
        trig = [r for r in strict_rows if r.get('trigger_gold')]
        trig_acc = (sum(1 for r in trig if r.get('trigger_gold') == r.get('trigger_pred')) / len(trig)) if trig else None
        agg_all['trigger_accuracy'] = trig_acc
        agg_all['candidate_f1'] = agg_all.get('population_macro_f1')
        agg_all['answer_score'] = agg_all.get('strict_answer_accuracy')
        mem = [r for r in strict_rows if r['id'] in membership_ids and r.get('population') is not None]
        agg_mem = strict_metrics.summarize(mem)
        agg_mem['candidate_f1'] = agg_mem.get('population_macro_f1')
        all_results[name] = {'kind':'direct','flags':flags,'all388':agg_all,'membership47':agg_mem,
                             'rows':rows,'seconds':round(time.time()-t0,2)}
        print(name, 'answer', round(agg_all.get('strict_answer_accuracy') or 0,3),
              'popF1', round(agg_all.get('population_macro_f1') or 0,3),
              'trig', agg_all['trigger_accuracy'], flush=True)

    manifest = {
        'dataset': str(config.DATASET), 'dataset_sha256': sha(config.DATASET),
        'annotations_sha256': sha(config.ANNOTATIONS), 'ontology_sha256': sha(config.ONTOLOGY),
        'scripts': {p.name: sha(p) for p in (Path(__file__).parent/'core_v3').glob('*.py')},
        'guarantees': ['evidence_builder does not read gold or source_docs',
                       'stage_a uses only question+spec+ontology state',
                       'population_engine does not read gold_truth.csv or task.gold',
                       'strict_metrics uses gold for scoring only',
                       'applicability masks follow evaluation fields in corrected references'],
        'variants': {k:{'kind':v['kind'],'flags':v.get('flags',{})} for k,v in all_results.items()},
    }
    (config.RESULTS/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    (config.RESULTS/'direct_experiments.json').write_text(json.dumps(all_results,ensure_ascii=False,indent=2),encoding='utf-8')

    L=['# Strict v3 direct results\n', 'All metrics use corrected TP IDs and reference/evaluation fields.\n',
       '| ID | answer | strict acc | pop macro F1 | nonempty F1 | denom count | trigger |',
       '|---|---:|---:|---:|---:|---:|---:|']
    for k,v in all_results.items():
        a=v['all388']
        L.append(f"| {k} | {a.get('answer_n')} | {a.get('strict_answer_accuracy')} | {a.get('population_macro_f1')} | {a.get('nonempty_population_f1')} | {a.get('denominator_count_accuracy')} | {a.get('trigger_accuracy')} |")
    (config.RESULTS/'direct_experiments.md').write_text('\n'.join(L),encoding='utf-8')
    print('wrote', config.RESULTS/'direct_experiments.md')

if __name__=='__main__': main()
