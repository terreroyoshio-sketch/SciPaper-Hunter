---
name: my-academic-research-master
description: 本地科研总控 skill — 编排 ARS + 本地 skills 执行完整科研流水线。负责任务分发、安全规则、质量门禁和版本管理。
type: orchestrator
version: 2.0.0
triggers:
  - "开始科研项目"
  - "写论文"
  - "文献综述"
  - "审稿"
  - "引用核查"
  - "科研"
  - "开题"
  - "基金"
  - "申报书"
---

# my-academic-research-master

**本地科研总控 Skill** — 编排 ARS (Academic Research Skills) + 本地已安装 skills，执行 10 阶段科研流水线。

---

## 默认调用顺序

执行科研任务时，按以下顺序调用（用户可中途指定起点）：

```
Phase 0: 任务冻结
  → deep-research (brief) [快速调研]
  → Brainstorming [选题发散]

Phase 1: 文献检索
  → Using-Superpowers [查找可用 skill]
  → keyword-literature-download [关键词检索]
  → deep-research (lit-review mode) [深度文献调研]

Phase 2: 文献筛选
  → deep-research (fact-check mode) [事实核验]

Phase 3: 证据卡片

Phase 4: 主题聚类与 Taxonomy
  → critical-literature-review-pipeline
  → literature-boundary-lock

Phase 5: 初稿写作
  → academic-paper [ARS 主写作 skill]
  → academic-abstract-pipeline
  → citation-format-syntax-auditor
  → objectivity-calibration-auditor

Phase 6: 图表生成
  → nature-figure (如需要高质量图)

Phase 7: 引用核验
  → literature-boundary-lock
  → citation-format-syntax-auditor
  → 本地 check_bibtex.py / check_citation_coverage.py

Phase 8: 模拟审稿
  → academic-paper-reviewer [ARS 审稿 skill]
  → reviewer-red-team-auditor [本地红队审稿]

Phase 9: 修订

Phase 10: 最终导出
```

---

## 默认安全规则（不可绕过，不可协商）

### R1: 文献真实性
- 任何作者、年份、题目、期刊、DOI 都必须来自真实来源。
- 无法核验的引用必须标成 `[UNVERIFIED]`。
- 不得为了凑参考文献数量编造文献。

### R2: AI 审稿边界
- 不得把 AI 生成的模拟审稿写成真实审稿。
- AI 审稿结论只能写：Accept for internal draft / Minor revision / Major revision / Reject as current draft。
- 不得写"已通过同行评审"或"可直接投稿"。

### R3: 实验结果真实性
- 不得把未运行实验写成实验结果。
- 不得把未下载的 PDF 写成已精读。

### R4: 语言真实性
- 不得为提高创新性使用夸张词（颠覆性、革命性、首次、填补空白等）。
- 不得使用没有证据的表达。

### R5: 投稿准备
- 不得输出可直接投稿的最终版，除非完成：
  1. 引用核验全部通过
  2. 图表核验
  3. 伦理核验
  4. 人工审查清单全部签字

---

## 默认中文写作规则

1. 语言符合论文规范，减少口号式表达
2. 减少公众号式表达（震惊、重磅、干货等）
3. 不要使用过多圆点列表
4. 表格只给列名加粗，不使用深蓝底色
5. 不使用明显 AI 味的三段式套话（"首先...其次...最后..."）
6. 保持学术名词准确，不替换专有名词
7. 尽量避免与原文连续 8 个字完全相同
8. 不随意扩写无证据内容
9. 每段必须有明确的中心句和证据来源

## 默认英文写作规则

1. 使用正式学术论文语气
2. 不使用夸张修辞（extremely, incredibly, remarkably 等）
3. 不写空泛贡献（"This work provides valuable insights" 等）
4. 优先使用短句和清楚的逻辑连接
5. 保持术语一致
6. 每个核心 claim 后必须有 citation 或 `[evidence note]`

---

## 引用的外部 Skills

| Skill | 来源 | 用途 |
|-------|------|------|
| `deep-research` | ARS | 深度研究、文献调研、事实核验 |
| `academic-paper` | ARS | 论文写作、格式转换 |
| `academic-paper-reviewer` | ARS | 多视角审稿 |
| `academic-pipeline` | ARS | 10 阶段流水线编排 |
| `keyword-literature-download` | 本地 | 文献关键词检索 |
| `critical-literature-review-pipeline` | 本地 | 批判性综述 |
| `citation-format-syntax-auditor` | 本地 | 引用格式审计 |
| `objectivity-calibration-auditor` | 本地 | 客观性校准 |
| `reviewer-red-team-auditor` | 本地 | 红队模拟审稿 |
| `literature-boundary-lock` | 本地 | 引用范围锁定 |
| `nature-figure` | 本地 | 高质量科研图表 |
| `academic-abstract-pipeline` | 本地 | 摘要写作 |
| `brainstorming` | 本地 | 选题发散 |
| `using-superpowers` | 本地 | 技能查找 |

---

## 安全闸门（详见 references/quality_gates.md）

| 闸门 | 阶段 | 通过条件 |
|------|------|---------|
| Gate 1: 文献闸门 | Phase 2→3 | 每子方向≥5 篇文献，每结论≥2 来源，A 类有 evidence card |
| Gate 2: 引用闸门 | Phase 7→8 | 0 编造引用，0 编造 DOI，引用与论点匹配 |
| Gate 3: 实验闸门 | 有实验时 | 有日志、有种子、有对照、有统计检验 |
| Gate 4: 语言闸门 | Phase 9→10 | 删除夸张/公众号/空泛/AI 模板表达 |
| Gate 5: 伦理闸门 | Phase 10 | AI 使用披露、伦理审批（如需）、匿名化（如需） |

---

## 快速启动

```bash
# 创建科研项目
python .claude/skills/my-academic-research-master/scripts/make_project_structure.py \
  --topic "你的研究主题" --output ./my_research

# 执行流水线（参考 references/local_pipeline.md）
# Phase 0: 编辑 00_plan/project_plan.md
# Phase 1: 开始文献检索
```

## 配置

所有规则文件位于 `references/` 目录：
- `anti_fabrication_rules.md`
- `citation_verification_rules.md`
- `literature_review_rules.md`
- `paper_writing_rules.md`
- `reviewer_simulation_rules.md`
- `experiment_integrity_rules.md`
- `chinese_academic_style_rules.md`
- `local_pipeline.md`
- `quality_gates.md`
- `experiment_agent_rules.md`
- `openscholar_style_rules.md`
