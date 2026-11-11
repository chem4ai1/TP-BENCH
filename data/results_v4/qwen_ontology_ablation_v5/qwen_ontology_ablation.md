# Qwen3.8-27B: With vs Without Ontology

Model: `Qwen3.8-27B`; tasks: 60; calls: 120; elapsed: 238.9s.

| Condition | parse rate | trigger accuracy | gold required match |
|---|---:|---:|---:|
| with_ontology | 1.000 | 0.850 | 0.804 |
| without_ontology | 1.000 | 0.350 | 0.391 |

| Gold trigger | n | with ontology | without ontology |
|---|---:|---:|---:|
| abox_repair | 25 | 1.000 | 0.000 |
| no_intervention | 14 | 1.000 | 0.000 |
| ontology_upgrade | 21 | 0.571 | 1.000 |
