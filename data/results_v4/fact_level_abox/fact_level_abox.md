# Fact-level ABox recovery

Canonical relation-level vs fact-level results. The fact-level mode uses the task's `state_spec.fact_ids` and `evidence_hashes`; it is an oracle-assisted availability diagnostic.

| Metric | Relation-level | Fact-level |
|---|---:|---:|
| E1 trigger accuracy | 0.784 | **0.913** |
| E1 abox_repair recall | 0.676 | **0.983** |
| E1 no-intervention recall | 0.979 | 0.979 |
| E2 required-element accuracy | 0.694 | **0.849** |
| E2 subtype accuracy | 0.729 | **0.889** |
| Predicted exact | 0.566 | **0.591** |
| Predicted P macro-F1 | 0.658 | **0.736** |
| Predicted nonempty F1 | 0.661 | **0.764** |
| Predicted abstain | 0.255 | **0.133** |
| Reference exact | 0.624 | 0.624 |

By gold state:

| Gold state | n | Predicted exact (relation) | Predicted exact (fact) | Reference exact |
|---|---:|---:|---:|---:|
| upgrade | 143 | 0.554 | 0.554 | 0.654 |
| repair | 173 | 0.453 | **0.512** | 0.512 |
| no change | 96 | 0.787 | 0.787 | 0.787 |

Missing-fact tasks: 150.  
Evidence-mismatch tasks: 0.

The default paper run remains relation-level; `FACT_LEVEL_ABOX=1` enables the fact-level diagnostic.
