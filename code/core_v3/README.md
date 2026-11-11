# core_v3

解耦后的 v3 评测内核。目标：把 evidence 构造、Stage A checker、deterministic engine、evaluator 分开，并消除 gold leakage 与 proxy/simulation 口径混用。

| 模块 | 职责 | 是否读 gold |
|---|---|---|
| `config.py` | 路径、endpoint、模型名、超时 | 否 |
| `data_loader.py` | 加载资源；`split_task()` 严格拆 `task_input` / `gold` | 是，仅用于拆分与评分 |
| `object_inventory.py` | 从 56 篇 run 构建站点/模型/类型/数据对象清单；多 anchor 解析 | 否 |
| `evidence_builder.py` | 从 annotations + md 构造候选文档与 evidence snippets；不读 `source_docs`、不读 gold | 否 |
| `schema_checker.py` | 只读 question + PopulationSpec + ontology state，输出 trigger_class / trigger_type / proposal / candidate_rule | 否 |
| `population_engine.py` | 确定性 Stage B：角色、粒度、分母、集合、Top-k、趋势、交叉表、replay | 否 |
| `llm_client.py` | OpenRouter / Qwen 统一调用与 JSON 提取 | 否 |
| `evaluator.py` | 按 gold.type 分派指标；direct/proxy/simulation 登记 | 是，仅评分 |

## 入口

```bash
cd paper_en/code
python -u run_v3.py
```

输出：

```text
data/TASK_TYPES_AND_EVALUATION.md
data/EXPERIMENT_REGISTRY.md
data/results_v3/direct_experiments.json/md
data/results_v3/experiment_registry.json
data/results_v3/manifest.json
```

## 不变量

```text
evidence_builder 不读 gold/source_docs
stage_a 不读 gold trigger_annotation
population_engine 不读 gold/gold_truth.csv
evaluator 使用 gold 只做 score
direct / proxy / simulation 分开登记
```
