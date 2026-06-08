---
name: research-idea-conflict-miner
description: 文献冲突驱动选题孵化器 — 通过文献冲突寻找可验证研究问题，不凭空生成 idea。8 阶段工作流，从研究场域压缩到最小可行研究方案。
type: pipeline
version: 1.0.0
triggers:
  - "选题"
  - "科研选题"
  - "研究idea"
  - "开题"
  - "基金选题"
  - "临床研究选题"
  - "医学影像选题"
  - "课题设计"
---

# research-idea-conflict-miner

## 文献冲突驱动选题孵化器

**核心逻辑：** 先定义研究场域 → 输入文献和数据约束 → 生成证据矩阵 → 寻找文献冲突 → 把冲突转化为可验证假设 → 审稿人视角攻击设计 → 输出最小可行方案。

---

## 核心原则（不可绕过）

1. **不准直接生成"创新选题"** — 必须先经过文献冲突分析
2. **不准根据热点词空想题目** — 所有 idea 必须有文献来源
3. **不准编造文献、作者、年份、DOI、期刊名**
4. **不准把无证据支持的想法包装成创新点**
5. **不准用"多模态、精准预测、智能诊断、临床转化、可解释性"等空泛词**
6. **不准把 AI 模拟审稿当成真实审稿**
7. **不准把不可获得的数据写进研究方案**
8. **所有选题必须落到：人群、变量、比较对象、结局、方法、数据可得性、发表风险**

---

## 8 阶段工作流

```
Stage 0: 任务冻结       → 00_plan/field_definition.md
Stage 1: 输入材料整理    → 01_materials/material_inventory.md
Stage 2: 生成证据矩阵    → 02_evidence/literature_evidence_matrix.csv
Stage 3: 挖掘文献冲突    → 03_conflicts/conflict_map.md
Stage 4: 翻译可检验假设  → 04_hypotheses/hypothesis_translation.md
Stage 5: 约束审查        → 05_constraints/constraint_audit.md
Stage 6: 恶毒审稿人攻击  → 06_review/reviewer_attack.md
Stage 7: 最小可行方案    → 07_output/minimal_viable_research_plan.md
Stage 8: 决策报告        → 08_decision/decision_report.md
```

---

## 阶段详情

### Stage 0: 任务冻结 — 研究场域压缩

**输入：** 用户宽泛方向
**输出：** `00_plan/field_definition.md`

把宽泛方向压缩成具体研究场域。如果方向太宽，拆成 3 个具体场域。

研究场域必须回答：
1. 研究对象
2. 核心变量（可量化？单位？测量稳定性？）
3. 主要结局
4. 比较对象
5. 数据来源
6. 样本量
7. 伦理审批
8. 投稿方向

**输出表格格式：**

| 场域编号 | 具体场景 | 研究对象 | 核心变量 | 主要结局 | 数据可得性 | 主要风险 | 是否建议继续 |
|---|---|---|---|---|---|---|---|

---

### Stage 1: 输入材料整理

**输出：** `01_materials/material_inventory.md`

必须收集：
1. 10–30 篇核心论文
2. 相关指南或共识
3. 数据字典
4. 可用变量列表
5. 结局定义
6. 目标人群
7. 已有基线方法
8. 目标期刊要求

**硬性规则：**
- 没有文献 → 不能输出正式 idea
- 没有数据字段 → 不能判断可行性
- 没有结局定义 → 不能进入统计设计

---

### Stage 2: 生成证据矩阵

**调用：** `keyword-literature-download`, `deep-research`, `literature-boundary-lock`
**输出：** `02_evidence/literature_evidence_matrix.csv`

每篇文献拆成：title, authors, year, venue, doi, study_population, sample_size, core_variable, comparator, outcome, statistical_method, main_finding, limitation, data_source, conflict_signal, verification_status

**conflict_signal 类型：**
1. conclusion_conflict — 结论冲突
2. population_conflict — 人群冲突
3. method_conflict — 方法冲突
4. mechanism_conflict — 机制冲突
5. scenario_conflict — 场景冲突
6. metric_conflict — 指标冲突
7. no_conflict_found — 未发现冲突
8. insufficient_information — 信息不足

**硬性规则：**
- 信息来自摘要而非全文 → 标记 `abstract_only`
- DOI 或题名无法核验 → 标记 `unverified`
- unverified 文献不能用于核心结论

---

### Stage 3: 挖掘文献冲突

**输出：** `03_conflicts/conflict_map.md`

**判断流：**
1. 冲突来自样本量太小 → 标记方法偏差
2. 冲突来自结局定义不同 → 标记定义差异
3. 冲突来自人群不同 → 优先考虑亚组问题
4. 冲突来自真实世界 vs 公开数据 → 考虑外部验证
5. **只有冲突可被用户数据验证 → 才进入下一阶段**

**输出表格：**

| 冲突编号 | 类型 | 涉及文献 | 表面矛盾 | 可能原因 | 是否真科学问题 | 是否方法偏差 | 可验证性 |
|---|---|---|---|---|---|---|---|

---

### Stage 4: 把冲突翻译成可检验假设

**输出：** `04_hypotheses/hypothesis_translation.md`

**公式：**
```
原始冲突：文献 A 认为 X 有效，文献 B 认为 X 价值有限
不成熟问题：X 有没有用？
成熟问题：在【人群】中，【变量 X】是否在【比较对象】之外，为【结局 Y】提供额外价值？
```

**每个假设包含：**
1. 研究人群
2. 核心变量
3. 比较对象
4. 主要结局
5. 统计方法
6. 预期解释边界
7. 数据需求
8. 失败条件

---

### Stage 5: 约束审查

**输出：** `05_constraints/constraint_audit.md`

**8 项审查：**
1. 变量约束 — 可量化？单位？稳定？
2. 数据约束 — 样本量？缺失值？
3. 统计约束 — 事件数？过拟合？
4. 临床约束 — 用户关心？能改变判断？
5. 创新约束 — 真实增量？
6. 发表约束 — 证据强度？
7. 伦理约束 — 患者/隐私？
8. 可复现约束 — 有记录？

**评分 0–5/项：**
- ≥35: A. 值得立即做
- 25–34: B. 收缩后可做
- 15–24: C. 补材料再判断
- <15: D. 不建议做

---

### Stage 6: 恶毒审稿人攻击

**调用：** `academic-paper-reviewer`, `reviewer-red-team-auditor`
**输出：** `06_review/reviewer_attack.md`

**4 个审稿角色：**
1. 医学统计学审稿人
2. 临床/场景审稿人
3. 方法学审稿人
4. 怀疑型审稿人

**每个审稿人必须输出：**
- 5 个致命问题
- 问题等级（致命/重大/可修改）
- 补救方案
- 不补救的拒稿风险
- 适合投稿层级

**禁止：** 鼓励式审稿、"整体很好"、泛泛建议。

---

### Stage 7: 最小可行研究方案

**输出：** `07_output/minimal_viable_research_plan.md`

**20 项结构：**
1. 暂定题目 → 9. 核心变量 → 17. 预期创新点
2. 研究背景 → 10. 主要结局 → 18. 主要风险
3. 冲突来源 → 11. 次要结局 → 19. 人工确认问题
4. 研究问题 → 12. 比较对象 → 20. 最终建议
5. 假设 → 13. 统计方法
6. 研究对象 → 14. 样本量风险
7. 纳入标准 → 15. 伦理风险
8. 排除标准 → 16. 预期图表

**题目要求：** 包含对象+变量+结局/场景，不空泛，不强证据加"初步探索"。

---

### Stage 8: 决策报告

**输出：** `08_decision/decision_report.md`

**最终结论（四选一）：**
- A. 立即推进
- B. 收缩后推进
- C. 补材料后再判断
- D. 放弃

**必须包含：** 推荐/不推荐理由，需补文献/数据列表，伦理/发表风险评估，下一步动作。

---

## 引用的外部 Skills

| 阶段 | Skill | 用途 |
|------|-------|------|
| 0 | `brainstorming` | 研究场域发散 |
| 2 | `keyword-literature-download` | 文献检索 |
| 2 | `deep-research` | 深度文献调研 |
| 2 | `literature-boundary-lock` | 证据边界锁定 |
| 5 | `objectivity-calibration-auditor` | 客观性校准 |
| 6 | `academic-paper-reviewer` | 审稿模拟 |
| 6 | `reviewer-red-team-auditor` | 红队攻击 |

---

## 参考文献（本地）

| 文件 | 内容 |
|------|------|
| `references/anti_hallucination_rules.md` | 反编造规则 |
| `references/conflict_typology.md` | 冲突类型学定义 |
| `references/medical_research_rules.md` | 医学研究通用规则 |
| `references/imaging_research_rules.md` | 医学影像科研专用规则 |
| `references/statistics_constraints.md` | 统计约束规则 |
| `references/reviewer_red_team_rules.md` | 审稿人红队攻击规则 |

---

## 快速启动

```bash
# 1. 创建课题项目
python scripts/make_idea_project.py \
  --topic "你的研究方向" \
  --output ./my_idea

# 2. 编辑 00_plan/field_definition.md
# 3. 按 8 阶段顺序执行

# 4. 辅助检查
python scripts/check_matrix_completeness.py 02_evidence/literature_evidence_matrix.csv
python scripts/score_research_idea.py 05_constraints/constraint_audit.md --output report.md
python scripts/export_decision_report.py --input 07_output/ --output 08_decision/decision_report.md
```
