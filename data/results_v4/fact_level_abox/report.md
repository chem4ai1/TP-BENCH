# Fact-level ABox Recovery Diagnostic

## 1. What changed

`schema_checker.stage_a` now accepts an optional `state_spec` and checks:

```text
state_spec.fact_ids
state_spec.evidence_hashes
state_spec.target_relations
```

When a target relation is present but any target fact is missing, or a present
fact has an evidence-hash mismatch, Stage A returns:

```text
trigger_class = abox_repair
trigger_type  = abox_incomplete
candidate_rule = fact-level ABox backfill
```

The result exposes:

```json
{
  "missing_facts": ["..."],
  "evidence_mismatch": ["..."],
  "target_fact_n": 42
}
```

`FACT_LEVEL_ABOX=1` enables this mode in `evaluate_state_repair.py`; the default
remains the relation-level check so the canonical paper results are not silently
changed.

## 2. Comparison

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

```text
upgrade:  predicted 0.554, reference 0.654
repair:   predicted 0.512, reference 0.512
no change: predicted 0.787, reference 0.787
```

Missing-fact tasks: 150.  
Evidence-mismatch tasks: 0.

## 3. Why the gain is large

The relation-level check only asks whether an ABox relation is empty. It cannot
distinguish:

```text
relation present, all target facts missing
relation present, some target facts missing
relation present, target facts present but object/evidence mismatch
relation present, target facts complete
```

The fact-level check uses the task's state-spec fact identities directly and
therefore catches partial ABox gaps that the relation-level count misses.

## 4. Important caveat

`state_spec.fact_ids` and `evidence_hashes` are reference facts built from the
task's state specification. This diagnostic is therefore **oracle-assisted**:
it verifies whether a state exposes the specified reference facts, but it does
not independently discover those facts from raw text.

It should be reported as a fact-level availability/recovery diagnostic, not as a
fully inductive Stage A improvement. The default paper run keeps the
relation-level mode until this distinction is explicitly accepted.

## 5. Files

```text
code/evaluate_fact_level_abox.py
data/results_v4/fact_level_abox/fact_level_abox.json
data/results_v4/fact_level_abox/state_repair_fact_results.json
data/results_v4/fact_level_abox/state_transition_fact_results.json
```
