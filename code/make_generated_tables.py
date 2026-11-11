import json
from pathlib import Path
from core_v3 import config
P=config.PAPER_EN if hasattr(config,'PAPER_EN') else config.CODE.parent
paper_dir = P/'paper' if (P/'paper').exists() else P/'icde_statqa'
OUT=paper_dir/'generated'; OUT.mkdir(parents=True,exist_ok=True)
V=json.loads((config.DATA/'results_v3/direct_experiments.json').read_text(encoding='utf-8'))
B=json.loads((config.DATA/'baselines/b1_b5_corrected.json').read_text(encoding='utf-8'))
E=json.loads((config.DATA/'baselines/b1b5_extended_estimates.json').read_text(encoding='utf-8'))
C=json.loads((config.DATA/'results_v4/coverage_main_table.json').read_text(encoding='utf-8'))
A=json.loads((config.DATA/'results_v4/aggbench_strict/summary.json').read_text(encoding='utf-8'))
M=json.loads((config.DATA/'corrected/manifest.json').read_text(encoding='utf-8'))
ST=json.loads((config.DATA/'results_v4'/'state_transition'/'state_transition_results.json').read_text(encoding='utf-8'))
SR=json.loads((config.DATA/'results_v4/state_repair/state_repair_results.json').read_text(encoding='utf-8'))
SG=json.loads((config.DATA/'results_v4/state_repair/significance.json').read_text(encoding='utf-8'))
SM=json.loads((config.DATA/'tiers/state_ready_manifest.json').read_text(encoding='utf-8'))
FC=json.loads((config.DATA/'results_v4/aggbench_structured_typed/full_chain_source_metrics.json').read_text(encoding='utf-8'))
D4=[json.loads(l) for l in (config.DATA/'tiers/dataset_v4_state.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]

def f(x,n=3):
    return '--' if x is None else f'{float(x):.{n}f}'
def g(x,n=0):
    return '--' if x is None else f'{float(x):.{n}f}'

def table_main():
    return table_state_repair_ablation()

def table_b1b5():
    L=['\\begin{tabular}{lrr}','\\toprule','System & Exact & Macro $F_1$ \\\\','\\midrule']
    labels={'B1_RAG':'RAG','B2_Extraction':'Extraction','B4_Qwen_retrieval':'Qwen3.8-27B retrieval-only','B5_Full':'Full chain'}
    for k in ['B1_RAG','B2_Extraction','B4_Qwen_retrieval','B5_Full']:
        s=B['systems'][k].get('summary',{}); L.append(f"{labels[k]} & {f(s.get('strict_answer_accuracy'))} & {f(s.get('population_macro_f1'))} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_b1b5_extended():
    L=['\\begin{tabular}{llrrrrrrr}','\\toprule',
       'Class & System & Exact & Macro $F_1$ & NACE m & NACE md & ACE & Recall \\\\','\\midrule']
    for r in E['rows']:
        L.append(f"{r['class']} & {r['system']} & {f(r['exact'])} & {f(r['macro_f1'])} & {f(r['nace_mean'])} & {f(r['nace_med'])} & {f(r['ace_mean'])} & {f(r['recall'])} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)


def table_coverage():
    L=['\\begin{tabular}{lrrrrrr}','\\toprule','Family & $n$ & Cov P & Cov R & Cov $F_1$ & Over & Under \\\\','\\midrule']
    for k,v in C['by_family'].items(): L.append(f"{k.replace('_','\\_')} & {v['n']} & {f(v['coverage_p'])} & {f(v['coverage_r'])} & {f(v['coverage_f1'])} & {f(v['over'])} & {f(v['under'])} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_agg_ontology():
    x=json.loads((config.DATA/'results_v4/aggbench_structured_typed/summary.json').read_text(encoding='utf-8'))
    boot=json.loads((config.DATA/'results_v4/aggbench_structured_typed/paired_bootstrap.json').read_text(encoding='utf-8'))
    L=['\\begin{tabular}{llrrrr}','\\toprule','Domain & $k$ & Pre-repair target state & Repaired target state & $\\Delta F_1$ (pp) & 95\\% CI (pp) \\\\','\\midrule']
    for dom in ['research','finance']:
        key=f'qwen_{dom}_lambda2.0'
        v=x['runs'][key]['variants']
        for k in [20,50]:
            b=v[f'baseline_top{k}']['source_f1']; o=v[f'typed_union_top{k}']['source_f1']
            ci=boot['domains'][dom][str(k)]
            L.append(f"{dom} & {k} & {b*100:.1f} & \\textbf{{{o*100:.1f}}} & +{ci['delta_f1']*100:.1f} & [{ci['lo']*100:.1f}, {ci['hi']*100:.1f}] \\\\")
    L+=['\\bottomrule','\\end{tabular}']
    return '\n'.join(L)

def table_agg():
    L=['\\begin{tabular}{lrrrrr}','\\toprule','Domain / retrieval & $n$ & Source P & Source R & Source $F_1$ & Count MAE \\\\','\\midrule']
    for dom in ['research','finance']:
        for name in ['top20','top50','overlap2_top20','overlap2_top50']:
            v=A['domains'][dom]['variants'][name]
            L.append(f"{dom} {name.replace('_','\\_')} & {v['n']} & {f(v.get('source_p'))} & {f(v.get('source_r'))} & {f(v.get('source_f1'))} & {f(v.get('count_mae'))} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_replay():
    r=json.loads((config.DATA/'results_v4/real_replay_results.json').read_text(encoding='utf-8'))['summary']
    L=['\\begin{tabular}{lr}','\\toprule','Metric & Value \\\\','\\midrule',f"Tier C tasks & {r['n']} \\\\",f"Comparability & {r['comparability_audit']:.3f} \\\\",f"Silent-zero rate & {r['silent_zero_rate']:.3f} \\\\",f"Regression rate & {r['regression_rate']:.3f} \\\\",f"v1 core ABox & {r['v1_core_abox']} \\\\",f"v2 core ABox & {r['v2_core_abox']} \\\\",'\\bottomrule','\\end{tabular}']
    return '\n'.join(L)

def table_state_diagnosis():
    e1, e2 = SR['E1_expressibility_diagnosis'], SR['E2_state_delta']
    L=['\\begin{tabular}{lr}','\\toprule','Diagnostic metric & Value \\\\','\\midrule',
       f"E1 trigger accuracy & {f(e1.get('accuracy'))} \\\\",
       f"E1 upgrade recall & {f(e1['by_gold']['ontology_upgrade']['accuracy'])} \\\\",
       f"E1 repair recall & {f(e1['by_gold']['abox_repair']['accuracy'])} \\\\",
       f"E1 no-change recall & {f(e1['by_gold']['no_intervention']['accuracy'])} \\\\",
       f"E2 required-element accuracy & {f(e2.get('required_element_accuracy'))} \\\\",
       f"E2 subtype accuracy & {f(e2.get('subtype_accuracy'))} \\\\",
       '\\bottomrule','\\end{tabular}']
    return '\n'.join(L)

def table_state_confusion():
    c = SR['E1_expressibility_diagnosis']['confusion']
    rows=[('Gold: upgrade','ontology_upgrade'),('Gold: repair','abox_repair'),('Gold: no change','no_intervention')]
    L=['\\begin{tabular}{lrrr}','\\toprule','Gold state & Pred. upgrade & Pred. repair & Pred. no change \\\\','\\midrule']
    for label,g in rows:
        L.append(f"{label} & {c[g+'->ontology_upgrade']} & {c[g+'->abox_repair']} & {c[g+'->no_intervention']} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_state_restored():
    e = SR['E3_restored_computation']['all']
    L=['\\begin{tabular}{lrrrr}','\\toprule','Condition & Exact & Macro $F_1$ & Nonempty $F_1$ & Abstain \\\\','\\midrule']
    for label,key in [('No state repair','frozen'),('Predicted state repair','predicted'),('Reference state repair','gold')]:
        v=e[key]
        L.append(f"{label} & {f(v.get('strict_answer_accuracy'))} & {f(v.get('population_macro_f1'))} & {f(v.get('nonempty_population_f1'))} & {f(v.get('abstain_rate'))} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_coverage_state():
    e=SR['E3_restored_computation']['all']['coverage']; no_auditor=SR['E6_state_repair_ablation']['no_auditor']['coverage']
    L=['\\begin{tabular}{lrrrrr}','\\toprule','Condition & Cov P & Cov R & Cov $F_1$ & Over & Under \\\\','\\midrule']
    for label,v in [('No state repair',e['frozen']),('Predicted repair',e['predicted']),('Reference repair',e['gold']),('No coverage auditor',no_auditor)]:
        L.append(f"{label} & {f(v['precision'])} & {f(v['recall'])} & {f(v['f1'])} & {f(v['overcoverage'])} & {f(v['undercoverage'])} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_state_replay():
    e5=SR['E5_replay_comparability']; tc=ST['E5_replay_comparability']['tier_c_real_replay']
    L=['\\begin{tabular}{lr}','\\toprule','Replay metric & Value \\\\','\\midrule',
       f"Restoration rate & {f(e5['restoration_rate'])} \\\\",
       f"Regression rate & {f(e5['regression_rate'])} \\\\",
       f"Comparability & {f(e5['comparability'])} \\\\",
       f"Tier C comparability & {f(tc['comparability_audit'])} \\\\",
       '\\bottomrule','\\end{tabular}']
    return '\n'.join(L)

def table_state_by_group():
    e=SR['E3_restored_computation']['by_trigger']
    L=['\\begin{tabular}{lrrrrr}','\\toprule','Gold state & $n$ & No repair & Predicted & Reference & Cov $F_1$ no-repair$\\rightarrow$predicted$\\rightarrow$reference \\\\','\\midrule']
    for key,label in [('ontology_upgrade','Upgrade'),('abox_repair','Repair'),('no_intervention','No change')]:
        v=e[key]; c=v['coverage']
        L.append(f"{label} & {v['n']} & {f(v['frozen'].get('strict_answer_accuracy'))} & {f(v['predicted'].get('strict_answer_accuracy'))} & {f(v['gold'].get('strict_answer_accuracy'))} & {f(c['frozen']['f1'])}$\\rightarrow${f(c['predicted']['f1'])}$\\rightarrow${f(c['gold']['f1'])} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_state_repair_main():
    e = SR['E3_restored_computation']['all']; c=e['coverage']
    L=['\\begin{tabular}{lrrrrrr}','\\toprule','Condition & Exact & Macro $F_1$ & Coverage $F_1$ & Under & Over & Abstain \\\\','\\midrule']
    for label,key in [('No state repair (frozen $O$)','frozen'),('Full method','predicted')]:
        v=e[key]
        L.append(f"{label} & {f(v.get('strict_answer_accuracy'))} & {f(v.get('population_macro_f1'))} & {f(c[key]['f1'])} & {f(c[key]['undercoverage'])} & {f(c[key]['overcoverage'])} & {f(v.get('abstain_rate'))} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_state_repair_diagnosis():
    e1=SR['E1_expressibility_diagnosis']; e2=SR['E2_state_delta']
    L=['\\begin{tabular}{lr}','\\toprule','Diagnostic metric & Value \\\\','\\midrule',
       f"E1 trigger accuracy & {f(e1.get('accuracy'))} \\\\",
       f"E1 upgrade recall & {f(e1['by_gold']['ontology_upgrade']['accuracy'])} \\\\",
       f"E1 repair recall & {f(e1['by_gold']['abox_repair']['accuracy'])} \\\\",
       f"E1 no-change recall & {f(e1['by_gold']['no_intervention']['accuracy'])} \\\\",
       f"E2 required-element accuracy & {f(e2.get('required_element_accuracy'))} \\\\",
       f"E2 subtype accuracy & {f(e2.get('subtype_accuracy'))} \\\\",
       '\\bottomrule','\\end{tabular}']
    return '\n'.join(L)

def table_state_repair_by_trigger():
    e=SR['E3_restored_computation']['by_trigger']
    L=['\\begin{tabular}{lrrrr}','\\toprule','Gold state & $n$ & Predicted & Reference & Cov $F_1$ pred$\\rightarrow$ref \\\\','\\midrule']
    for key,label in [('ontology_upgrade','Upgrade'),('abox_repair','Repair')]:
        v=e[key]
        cov=v['coverage']
        L.append(f"{label} & {v['n']} & {f(v['predicted'].get('strict_answer_accuracy'))} & {f(v['gold'].get('strict_answer_accuracy'))} & {f(cov['predicted']['f1'])}$\\rightarrow${f(cov['gold']['f1'])} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_state_repair_coverage():
    e=SR['E3_restored_computation']['all']['coverage']
    L=['\\begin{tabular}{lrrrrr}','\\toprule','Condition & Cov P & Cov R & Cov $F_1$ & Over & Under \\\\','\\midrule']
    for label,key in [('No state repair','frozen'),('Predicted repair','predicted'),('Reference repair','gold')]:
        v=e[key]
        L.append(f"{label} & {f(v['precision'])} & {f(v['recall'])} & {f(v['f1'])} & {f(v['overcoverage'])} & {f(v['undercoverage'])} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_state_repair_ablation():
    e=SR['E6_state_repair_ablation']
    rows=[('No repair (frozen $O$)','frozen'),('Full method','full'),('No coverage auditor','no_auditor'),('No role relation','no_role'),('No denominator spec','no_denominator')]
    L=['\\begin{tabular}{lrrrr}','\\toprule','Setting & Exact & Macro $F_1$ & Cov $F_1$ & Abstain \\\\','\\midrule']
    for label,key in rows:
        if key=='frozen':
            m=SR['E3_restored_computation']['all']['frozen']; c=SR['E3_restored_computation']['all']['coverage']['frozen']
        else:
            m=e[key]['metrics']; c=e[key]['coverage']
        L.append(f"{label} & {f(m.get('strict_answer_accuracy'))} & {f(m.get('population_macro_f1'))} & {f(c.get('f1'))} & {f(m.get('abstain_rate'))} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_eval_scope():
    n=len(D4)
    status={k:sum(1 for r in D4 if r.get('state_ready_status')==k) for k in ('strict_ready','empty_reference_ready','empty_result_ready','derived_ready','needs_membership_or_answer_gold','no_intervention_ready','spec_only')}
    answer_n=sum(1 for r in D4 if (r.get('evaluation') or {}).get('answer'))
    member_n=sum(1 for r in D4 if (r.get('evaluation') or {}).get('members'))
    denom_n=sum(1 for r in D4 if (r.get('evaluation') or {}).get('denominator_count'))
    b1b5_n=B.get('subset_size',85)
    tier_c_n=ST.get('E5_replay_comparability',{}).get('tier_c_real_replay',{}).get('n',44)
    L=['\\begin{tabular}{llr}','\\toprule','Evaluation & Task set & $n$ \\\\','\\midrule',
       f"State diagnosis (E1/E2) & all TP-Bench & {n} \\\\",
       f"Restored computation (E3) & answer / membership eligible & {answer_n} / {member_n} \\\\",
       f"Coverage (E4) & state-annotated tasks & {n} \\\\",
       f"State repair state specs & all TP-Bench & {n} \\\\",
       f"S1 state-repair core & original evidence + nonempty refs & {status['strict_ready']} \\\\",
       f"S2 controlled-gap & empty-ref / empty-result / closed-world & {status['empty_reference_ready']+status['empty_result_ready']+status['derived_ready']} \\\\",
       f"S3 diagnosis-only & no answer/membership refs & {status['needs_membership_or_answer_gold']} \\\\",
       f"Auxiliary B1--B5 & membership subset & {b1b5_n} \\\\",
       f"Tier C replay & exact-gold subset & {tier_c_n} \\\\",
       f"Denominator & denominator-count refs & {denom_n} \\\\",
       f"AGGBench & research / finance & 288 / 210 \\\\",
       '\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_significance():
    L=['\\begin{tabular}{lrrr}','\\toprule','Comparison & mean & 95\\% CI & McNemar $p$ \\\\','\\midrule']
    for key,label in [('frozen','No repair / exact'),('predicted','Predicted / exact'),('gold','Gold / exact')]:
        v=SG['exact'][key]
        L.append(f"{label} & {f(v['mean'])} & [{f(v['lo'])}, {f(v['hi'])}] & -- \\\\")
    for key,label in [('frozen_vs_predicted','Frozen vs predicted'),('frozen_vs_gold','Frozen vs gold'),('full_vs_no_auditor','Full vs no auditor'),('full_vs_no_role','Full vs no role'),('full_vs_no_denominator','Full vs no denom')]:
        v=SG['mcnemar'][key]
        L.append(f"{label} & -- & -- & {v['p_value']:.2g} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)

def table_full_chain_aggb():
    L=['\\begin{tabular}{llrrrrrrrr}','\\toprule',
       'Domain & $k$ & $n$ & Src P & Src R & Src $F_1$ & Under & Over & NACE m/md & ACE \\\\','\\midrule']
    for dom,k in [('research',20),('research',50),('finance',20),('finance',50)]:
        v=FC['groups'][f'{dom}_top{k}']
        nace='--' if v['nace_mean'] is None else f"{f(v['nace_mean'])}/{f(v['nace_median'])}"
        L.append(f"{dom} & {k} & {v['n']} & {f(v['source_precision'])} & {f(v['source_recall'])} & {f(v['source_f1'])} & {f(v['undercoverage'])} & {f(v['overcoverage'])} & {nace} & {f(v['count_mae'])} \\\\")
    L+=['\\bottomrule','\\end{tabular}']; return '\n'.join(L)


def write(name,text):
    (OUT/name).write_text(text+'\n',encoding='utf-8')

write('main_table.tex',table_main()); write('b1b5_table.tex',table_b1b5()); write('coverage_table.tex',table_coverage()); write('aggbench_table.tex',table_agg()); write('aggbench_ontology_table.tex',table_agg_ontology()); write('replay_table.tex',table_replay()); write('state_diagnosis_table.tex',table_state_diagnosis()); write('state_confusion_table.tex',table_state_confusion()); write('state_restored_table.tex',table_state_restored()); write('coverage_state_table.tex',table_coverage_state()); write('state_replay_table.tex',table_state_replay()); write('state_by_group_table.tex',table_state_by_group()); write('state_repair_main_table.tex',table_state_repair_main()); write('state_repair_diagnosis_table.tex',table_state_repair_diagnosis()); write('state_repair_by_trigger_table.tex',table_state_repair_by_trigger()); write('state_repair_coverage_table.tex',table_state_repair_coverage()); write('state_repair_ablation_table.tex',table_state_repair_ablation()); write('evaluation_scope_table.tex',table_eval_scope()); write('state_repair_significance_table.tex',table_significance()); write('full_chain_aggb_table.tex',table_full_chain_aggb()); write('b1b5_extended_table.tex',table_b1b5_extended())
main=SR['E3_restored_computation']['all']['predicted']
cov=SR['E3_restored_computation']['all']['coverage']['predicted']
nums={'MainExact':f(main.get('strict_answer_accuracy')),'MainFone':f(main.get('population_macro_f1')),'MainNonempty':f(main.get('nonempty_population_f1')),'MainMicro':f(main.get('population_micro_f1')),'MainAnswerN':str(main.get('answer_n')),'MainPopN':str(main.get('population_n')),'CoverageFone':f(cov.get('f1')),'CoverageP':f(cov.get('precision')),'CoverageR':f(cov.get('recall')),'RepairN':str(M.get('reference_repairs')),'UniqueN':str(len(D4)),'LegacyN':str(M.get('legacy_unique_ids'))}
L=['% generated from result files; do not hand-edit']
for k,v in nums.items(): L.append(f'\\newcommand{{\\{k}}}{{{v}}}')
write('numbers.tex','\n'.join(L))
# Markdown companion
md=['## Generated tables','### State-repair ablation','| Setting | Exact | Macro F1 | Coverage F1 | Abstain |','|---|---:|---:|---:|---:|']
for label,key in [('No state repair','frozen'),('Predicted state repair','predicted'),('Reference state repair','gold')]:
    v=SR['E3_restored_computation']['all'][key]; c=SR['E3_restored_computation']['all']['coverage'][key]
    md.append(f"| {label} | {f(v.get('strict_answer_accuracy'))} | {f(v.get('population_macro_f1'))} | {f(c.get('f1'))} | {f(v.get('abstain_rate'))} |")
for label,key in [('No coverage auditor','no_auditor'),('No role relation','no_role'),('No denominator spec','no_denominator')]:
    v=SR['E6_state_repair_ablation'][key]['metrics']; c=SR['E6_state_repair_ablation'][key]['coverage']
    md.append(f"| {label} | {f(v.get('strict_answer_accuracy'))} | {f(v.get('population_macro_f1'))} | {f(c.get('f1'))} | {f(v.get('abstain_rate'))} |")
md += ['','### B1—B5','| System | Exact | Macro F1 | Nonempty F1 |','|---|---:|---:|---:|']
for k in ['B1_RAG','B2_Extraction','B4_Qwen_retrieval','B5_Full']:
    s2=B['systems'][k].get('summary',{}); md.append(f"| {k} | {f(s2.get('strict_answer_accuracy'))} | {f(s2.get('population_macro_f1'))} | {f(s2.get('nonempty_population_f1'))} |")
md += ['','### Coverage','| Family | n | Cov P | Cov R | Cov F1 |','|---|---:|---:|---:|---:|']
for k,v in C['by_family'].items(): md.append(f"| {k} | {v['n']} | {f(v['coverage_p'])} | {f(v['coverage_r'])} | {f(v['coverage_f1'])} |")
OUT.joinpath('tables.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
print('wrote',OUT)
