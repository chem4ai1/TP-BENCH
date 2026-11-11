#!/usr/bin/env bash
# Supplemental material for "Target-Population Construction as Data Preparation
# for Statistical Queries" (ICDE 2027).
#
# The layout is kept compatible with code/core_v3/config.py:
#   <repo>/code/core_v3/config.py -> CODE=<repo>/code, PAPER_EN=<repo>, DATA=<repo>/data
#
# Requirements: Python 3.10+, requests. LLM-backed stages expect a local
# OpenAI-compatible endpoint and read credentials from files pointed to by
# API_KEY_DIR, OPENROUTER_KEY_PATH, PANSHI_KEY_PATH, QWEN_URL and QWEN_MODEL.
# No credentials are shipped in this repository.
#
# Contents:
#   code/core_v3/                  two-stage pipeline: Stage A checker,
#                                  Stage B deterministic engine, evaluator
#   code/run_v3.py                 pipeline entry point
#   code/build_state_specs.py      rebuild the 412 per-task state specifications
#   code/evaluate_state_transition.py, evaluate_significance.py,
#        ablation_r1_r8.py, a5_denominator_ablation.py,
#        run_qwen_ontology_ablation.py, evaluate_fact_level_abox.py
#                                   state-repair / formal-target-population ablations
#   data/tiers/dataset_v4_state.jsonl   canonical TP-Bench, 412 tasks
#   data/canonical/, data/ontology_v2.json
#                                  ontology snapshots before/after ABox backfill
#   data/raw/doc_annotations.jsonl, output/mineru_md/
#                                  annotations and source documents
#   data/results_v4/               raw ablation outputs
#   tables/                        LaTeX tables used in the paper
#
# Run `bash reproduce.sh` for an integrity check, then invoke the entry points
# above with your own endpoint and credentials.

set -euo pipefail
cd "$(dirname "$0")"

python3 - <<'PY'
import json, pathlib
p = pathlib.Path("data/tiers/dataset_v4_state.jsonl")
rows = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
ids = {r["id"] for r in rows}
assert len(rows) == 412, len(rows)
assert len(ids) == 412, len(ids)
print(f"TP-Bench: {len(rows)} tasks, {len(ids)} unique IDs")
for name in ("data/ontology_v2.json",
             "data/raw/doc_annotations.jsonl",
             "data/results_v4/state_transition/state_transition_results.json"):
    assert pathlib.Path(name).is_file(), name
print("Ontology snapshots, annotations and ablation outputs: present")
PY
