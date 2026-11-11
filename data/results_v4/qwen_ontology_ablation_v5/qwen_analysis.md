# Qwen3.8-27B Ontology Ablation Analysis

Model: `Qwen3.8-27B`; tasks: 60.

| Condition | raw gold trigger acc | pre-adjudication adjusted acc |
|---|---:|---:|
| with ontology | 0.850 | 0.983 |
| without ontology | 0.350 | 0.217 |

The adjusted column uses the 8 `human_decision=revise_gold` rows in `adjudication_workbook_20.csv`; it is a sensitivity check.

`without_ontology` answers every task as `ontology_upgrade`; this exposes the absence of a state/definition signal. That default gives 21/21 on the `ontology_upgrade` subset by class prior, while its overall accuracy is only 0.350.

The raw `ontology_upgrade` accuracy falls from 1.000 to 0.571 because the no-ontology model predicts that class for every task. With ontology, 12/21 upgrade tasks are correct; 8 of the 9 misses are the same `revise_gold` rows in the adjudication workbook, and TP0343 is the only residual true alias/`sameAs` miss. The drop is therefore a class-prior/label-noise artifact, not a degradation of the with-ontology model.
