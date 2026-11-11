# TP-BENCH: Supplemental Artifact

Supplemental material for *Target-Population Construction as Data Preparation
for Statistical Queries* (ICDE 2027).

This artifact contains the two-stage target-population pipeline, the 412-task
TP-Bench dataset, the ontology states before and after repair, and the raw
outputs of the state-repair ablations reported in the paper.

## Contents

```text
code/core_v3/                two-stage pipeline
                             - stage A: state-availability checker and repair
                               operator selection
                             - stage B: deterministic execution engine
                             - evaluator and reporting utilities
code/run_v3.py               pipeline entry point
code/build_state_specs.py    rebuilds the 412 per-task state specifications
code/evaluate_state_transition.py
code/evaluate_significance.py
code/evaluate_fact_level_abox.py
code/ablation_r1_r8.py
code/a5_denominator_ablation.py
code/run_qwen_ontology_ablation.py
                             state-repair and formal-target-population ablations
data/tiers/dataset_v4_state.jsonl
                             canonical TP-Bench, 412 tasks, 412 unique IDs
data/tiers/*manifest*.json   state-gap and state-ready task manifests
data/canonical/              ontology snapshots before and after ABox backfill
data/ontology_v2.json        ontology version snapshot
data/raw/doc_annotations.jsonl
                             source annotations cited by the tasks
output/mineru_md/            source documents underlying the mention frames
data/results_v4/             raw ablation outputs
  state_transition/          state-repair transition results
  qwen_ontology_ablation_v5/ ontology-upgrade ablation results
  fact_level_abox/           fact-level ABox repair results
tables/                      LaTeX tables used in the paper
reproduce.sh                 integrity check for the packaged data
```

## Quick check

```bash
bash reproduce.sh
```

Expected output:

```text
TP-Bench: 412 tasks, 412 unique IDs
Ontology snapshots, annotations and ablation outputs: present
```

## Requirements

Python 3.10+ and `requests`. The LLM-backed stages expect an
OpenAI-compatible endpoint configured through environment variables
(`API_KEY_DIR`, `OPENROUTER_KEY_PATH`, `PANSHI_KEY_PATH`, `QWEN_URL`,
`QWEN_MODEL`). No credentials are included in this repository.

## License

Released under the MIT License; see `LICENSE`. The source documents in
`output/mineru_md/` remain subject to the terms of their original
publications.
