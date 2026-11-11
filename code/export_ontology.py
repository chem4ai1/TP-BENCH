import json
from collections import Counter
from pathlib import Path

src = Path(__file__).resolve().parents[1] / 'data/ontology_v2.json'
out = Path(__file__).resolve().parents[1] / 'data/25_ontology_export.md'
d = json.loads(src.read_text(encoding='utf-8'))

L = []
L.append('# 现有本体导出与分析\n')
L.append('## 1. 基本信息\n')
L.append('| 项目 | 值 |')
L.append('|---|---|')
L.append(f'| 版本 | `{d.get("version")}` |')
L.append(f'| 类 | {len(d["classes"])} |')
L.append(f'| 属性 | {len(d["properties"])} |')
L.append(f'| 关系 | {len(d["relations"])} |')
L.append(f'| 个体 | {len(d.get("individuals", []))} |')
L.append(f'| 关系实例 | {len(d.get("relation_instances", []))} |')
L.append('')

ind_cls = Counter(x.get('class') for x in d.get('individuals', []))
rel_cnt = Counter(x.get('relation') for x in d.get('relation_instances', []))
L.append('### 个体分布\n')
L.append('| 类 | 个体数 |')
L.append('|---|---:|')
for k, v in ind_cls.most_common():
    L.append(f'| {k} | {v} |')
L.append('')
L.append('### 关系实例分布\n')
L.append('| 关系 | 实例数 |')
L.append('|---|---:|')
for r in d['relations']:
    L.append(f'| `{r["id"]}` | {rel_cnt.get(r["id"], 0)} |')
L.append('')

L.append('## 2. 类层次\n')
L.append('| 类 ID | 标签 | 父类 | 说明 |')
L.append('|---|---|---|---|')
for c in d['classes']:
    L.append(f'| {c["id"]} | {c.get("label", "")} | {c.get("parent") or "—"} | {str(c.get("description", ""))[:80]} |')
L.append('')

L.append('## 3. 对象关系\n')
L.append('| 关系 | 标签 | domain → range | 说明 |')
L.append('|---|---|---|---|')
for r in d['relations']:
    L.append(f'| `{r["id"]}` | {r.get("label", "")} | {r.get("domain")} → {r.get("range")} | {str(r.get("desc", ""))[:60]} |')
L.append('')

L.append('## 4. 数据属性\n')
L.append('| 属性 | 标签 | domain → range |')
L.append('|---|---|---|')
for p in d['properties']:
    L.append(f'| `{p["id"]}` | {p.get("label", "")} | {p.get("domain")} → {p.get("range")} |')
L.append('')

L.append('## 5. 实例样本\n')
for cls, limit in [('Paper', 8), ('EcologicalStation', 12), ('Dataset', 3)]:
    L.append(f'### {cls}\n')
    L.append('| ID | 关键属性 |')
    L.append('|---|---|')
    for x in [i for i in d['individuals'] if i.get('class') == cls][:limit]:
        attrs = x.get('attributes', {})
        key = ', '.join(f'{k}={v}' for k, v in list(attrs.items())[:4])
        L.append(f'| `{x["id"]}` | {key} |')
    L.append('')

L.append('## 6. 关键发现：TBox 与 ABox 不匹配\n')
L.append('''现有本体在 **TBox** 层面相对完整：有 Paper、EcologicalStation、StationType、AlgorithmModel、Variable、Evidence 等类，也有 uses_station、station_has_type、applies_model、reports_variable 等关系。但在 **ABox** 层面，核心统计关系几乎没有实例：

```text
uses_station      0
station_has_type  0
applies_model     0
reports_variable  0
has_theme         0
supported_by      0
```

只有：

```text
uses_dataset       103
station_located_in  29
```

这意味着：

1. 阶段 A 的 `SchemaReadiness` 不能只看“类/关系是否存在”，必须区分 **TBox coverage** 与 **ABox coverage**。
2. 阶段 B 不能直接从本体计数；必须先 grounding / backfill，否则站点、模型、主题统计都会得到 0。
3. 本体没有“研究站点 / 观测来源 / 背景提及”的角色关系，也没有“实际采用 / 对比基线 / 仅引用”的模型角色关系；`role_q` 在当前本体中不可表达，这是 **Schema Gap**，不是 ABox 缺失。
4. `unit_q`（paper/mention/pair）和 `D(q)`（分母集合）不属于本体，必须由 `PopulationSpec` 显式声明。
5. `Evidence` 类和 `supported_by` 关系存在，但关系实例为 0，证据链需要阶段 B 回填。
''')

L.append('## 7. 与两阶段的交互\n')
L.append('''### 阶段 A

| PopulationSpec 字段 | 本体对应 | 现状 |
|---|---|---|
| `U_q` | Paper / EcologicalStation 类 | 有类；Paper 只有 23 个个体 |
| `C_q^pop` | 类表达式 + uses_station + station_has_type | 类/关系存在，关系实例为 0 |
| `N_q` | applies_model / reports_variable 等 | 关系存在，实例为 0 |
| `D_q` | 由 PopulationSpec 定义，不直接存本体 | 需显式声明 |
| `role_q` | 无对应关系/类 | **Schema Gap** |
| `gran_q` | StationType 子类（高寒草甸等） | 类存在，关系实例为 0 |
| `unit_q` | 无对应 | 必须在 PopulationSpec 中声明 |
| `evidence_q` | Evidence + supported_by | 类存在，实例为 0 |
| `schema_version` | 本体版本 | v2.1.460 |

### 阶段 B

| 阶段 B 动作 | 本体读写 |
|---|---|
| grounding | 读 Paper/EcologicalStation/Variable 个体；写类/关系断言 |
| 成员构建 | 读 uses_station/station_has_type/applies_model；当前为空，需要回填 |
| 实例回填 | 写 Paper–Station、Station–StationType、Paper–Model、Evidence 关系 |
| 聚合 | 读成员集合；不直接依赖本体计数 |
| 总体审计 | 检查成员是否满足 PopulationSpec；检查 ABox 覆盖 |
''')

out.write_text('\n'.join(L), encoding='utf-8')
print('wrote', out, len('\n'.join(L)))
