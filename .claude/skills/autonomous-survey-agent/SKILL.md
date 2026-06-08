---
name: autonomous-survey-agent
description: 自主科研综述写作 Agent 工作流 — 9 阶段流水线，从选题冻结到最终导出。用于文献综述、论文 related work、项目申报书研究现状、基金国内外研究现状。
type: pipeline
version: 1.0.0
triggers:
  - "写综述"
  - "文献综述"
  - "survey"
  - "related work"
  - "研究现状"
  - "国内外研究现状"
  - "literature review"
  - "自主科研综述"
quality_gates: 6
stages: 9
---

# autonomous-survey-agent

## 核心原则

1. **不编造文献。** 所有引用必须可追溯到真实出版物。
2. **不编造 DOI。** 无法验证的 DOI 标记为 `missing`，不伪造。
3. **未下载的 PDF 不能说已阅读。**
4. **AI 自评不能充当真实同行评审。**
5. **不承诺具体发表结果。** 系统产出的是"可投稿初稿"，不是"已发表论文"。
6. **不伪造数据。** 综述不编造实验数字。
7. **全过程可追溯。** 每步都有记录，每个决策都有理由。
8. **人工确认不能跳过。** 关键节点必须人类确认。

---

## 适用场景

- 课程文献综述作业
- 论文 related work / 研究现状章节
- 基金申报书国内外研究现状
- 顶刊综述初稿
- 开题报告文献综述部分
- 技术调研报告

**不适用场景：**
- 需要原创实验的论文（本 skill 只处理综述部分）
- 需要一手数据的元分析
- 替代真实同行评审
- 需要在 6 天内完成并投稿的场景

---

## 9 阶段工作流总览

```
阶段 0: 选题冻结 ──────────────────→ project_plan.md
    ↓
阶段 1: 高召回文献检索 ────────────→ raw_candidates.csv, search_log.md
    ↓
阶段 2: 文献质量评分 (LQS) ────────→ scored_literature.csv
    ↓
阶段 3: 证据卡片与文献矩阵 ─────────→ evidence_cards/, literature_matrix.csv
    ↓
阶段 4: 主题聚类与 Taxonomy ───────→ taxonomy.md, outline_v1.md
    ↓
阶段 5: 综述结构写作 ──────────────→ manuscript/sections/*.tex
    ↓
阶段 6: 图表生成 ──────────────────→ figures/, tables/, figure_table_plan.md
    ↓
阶段 7: 引用核查与反造假审计 ───────→ citation_audit.md, citation_verification.csv
    ↓
阶段 8: 模拟审稿与迭代修改 ─────────→ reviews/review_round_*.md
    ↓
阶段 9: 最终导出 ──────────────────→ outputs/final/
```

---

## 6 道质量门禁 (Hard Gates)

### Gate 1: 文献门槛
- [ ] 核心主题每个子方向至少 5 篇文献
- [ ] 每个核心论点至少 2 个来源
- [ ] A 类文献必须有 evidence card
- [ ] 未核查文献不进入核心论点

### Gate 2: 结构门槛
- [ ] 必须有 taxonomy（不能只是平铺分类）
- [ ] 必须有现有综述对比
- [ ] 必须有研究缺口分析
- [ ] 必须有批判性分析
- [ ] 不是文献摘要拼接

### Gate 3: 引用门槛
- [ ] 0 条编造引用
- [ ] 0 条编造 DOI
- [ ] 所有正文引用都在 BibTeX 中
- [ ] 所有关键数字都有来源

### Gate 4: 图表门槛
- [ ] 每张图表都被正文引用
- [ ] 每张图表都有信息增量
- [ ] 无装饰性 AI 图
- [ ] 表格格式朴素、清晰、可打印（三线表）

### Gate 5: 语言门槛
- [ ] 无公众号式表达
- [ ] 无夸大词（革命性、开创性、首次证明等）
- [ ] 无空泛套话（众所周知、具有重要意义等）
- [ ] 中文符合论文规范 / 英文符合正式学术语气

### Gate 6: 伦理门槛
- [ ] AI 生成内容不伪装成人工阅读
- [ ] AI 自评不伪装成真实审稿
- [ ] 未验证材料不用于投稿
- [ ] 无学术造假内容

---

## 阶段详情

### 阶段 0: 选题冻结

**输入：** 用户主题、目标期刊/课程要求、学科方向、页数/字数目标、语言

**输出：** `project_plan.md`

**必须包含：**
1. 研究主题与范围
2. 研究对象
3. 时间范围（文献发表年份窗口）
4. 文献数据库范围
5. 纳入/排除标准
6. 目标读者
7. 预期产物（综述类型：叙述性综述、系统综述、范围综述等）
8. 风险清单
9. 人工确认点列表

**主题太宽时**必须拆成 2–3 个可执行版本，标注推荐优先级。

---

### 阶段 1: 高召回文献检索

**输入：** `project_plan.md`

**输出：** `references/raw_candidates.csv`, `references/search_log.md`

**方法（按优先级使用）：**
1. `arxiv` Python 包 → arXiv API
2. `semanticscholar` Python 包 → Semantic Scholar API
3. Playwright 自动化 → Google Scholar
4. Playwright 自动化 → IEEE/ACM/Springer/Elsevier 网页搜索
5. WebFetch → 目标数据库
6. 引用网络扩展（snowball sampling）

**每条记录至少包括：**
```
title, authors, year, venue, doi, url, abstract,
source_database, search_query, retrieval_date, pdf_status, note
```

**硬性规则：**
- 每个关键词组合记录在 search_log.md
- 每篇文献保留来源数据库
- 无 DOI 写 `missing`，不编造
- 未下载 PDF 写 `not_downloaded`
- 不凭模型记忆补全文献信息
- 目标：50–200 条原始候选

---

### 阶段 2: 文献质量评分 (LQS)

**输入：** `references/raw_candidates.csv`

**输出：** `references/scored_literature.csv`

**评分维度：**

| 维度 | 权重 | 评分标准 |
|------|------|---------|
| 主题相关性 | 30% | 直接相关=10, 间接相关=6, 弱相关=3 |
| 方法代表性 | 20% | 典范方法=10, 代表性=7, 边缘=4 |
| 发表质量 | 15% | 顶刊/顶会=10, 核心期刊=7, 一般=4, 预印本=2 |
| 被引/影响力 | 15% | 高被引=10, 中等=7, 低=3, 新发=5 |
| 近五年时效性 | 10% | 1年内=10, 3年内=7, 5年内=5, 更早=2 |
| 数据可验证性 | 10% | 开源代码+数据=10, 有代码=7, 仅描述=3 |

**分类规则：**
- **A 类（核心，LQS≥7.0）：** 精读，正文 1–3 段
- **B 类（重要，LQS 5.0–7.0）：** 关键论据，2–5 句
- **C 类（支撑，LQS 3.0–5.0）：** 补充证据，1 句
- **D 类（剔除，LQS<3.0）：** 记录剔除理由，不进入正文

**硬性规则：**
- 每个分类必须有理由
- 分数和理由可追踪
- 包含经典文献（不只看近年的）
- 某个主题单元无 A 类文献 → 回阶段 1 补检索

---

### 阶段 3: 证据卡片与文献矩阵

**输入：** `references/scored_literature.csv`

**输出：** `notes/evidence_cards/{author_year}.md`, `references/literature_matrix.csv`

**每张 evidence card 包含：**
1. 研究问题
2. 方法
3. 数据集/样本
4. 核心发现
5. 局限性
6. 与本综述主题的关系
7. 可引用句（可直接用于正文的总结句）
8. 禁止过度解释的边界
9. 原文页码或章节位置
10. 是否已人工核查

**硬性规则：**
- 不是流水账摘要
- 必须提取"这篇文献能支撑什么论点"
- 每个核心结论至少 2 篇以上文献支持
- 无证据支撑的判断标记为 `[hypothesis]` 或 `[author interpretation]`

---

### 阶段 4: 主题聚类与 Taxonomy

**输入：** `notes/evidence_cards/`, `references/literature_matrix.csv`

**输出：** `structure/taxonomy.md`, `structure/outline_v1.md`, `figures/taxonomy_draft.svg`

**可选结构（按主题特性选择）：**
1. 技术路线 × 应用场景
2. 方法类别 × 数据类型
3. 模型能力 × 自主程度
4. 问题阶段 × 解决策略
5. 国内研究 × 国际研究
6. 理论发展 × 方法发展 × 应用发展

**硬性规则：**
- 每个类别必须有代表文献
- 每个类别必须有局限性说明
- 必须指出空白区域（research gap）
- 不允许为了整齐而强行分类
- taxonomy 解释不了重要文献 → 重构

---

### 阶段 5: 综述结构写作

**默认结构（8 节）：**

```
§1 Introduction: Hook → Gap → Contributions → Roadmap
§2 Background: 核心概念、任务定义、基础理论
§3 Taxonomy: 分类依据、分类图、各类关系
§4–6 Main Body: 按主题分节，每节含方法差异、证据、局限
§7 Comparative Analysis: 表格对比、优缺点
§8 Challenges: 未解决问题、方法/数据瓶颈
§9 Future Directions: 具体方向 + 重要性说明
§10 Conclusion: 回答综述问题，不重复摘要
```

**段落规则：**
- 每段有中心句
- 每段有证据
- 每段结尾说明意义或限制
- 不堆引用（每处 1–3 条）
- 不一句话一段
- 不公众号风格
- 无"众所周知""具有重要意义"等空话
- 不多用圆点列表
- 中文符合论文规范 / 英文正式学术语气

**输出：** `manuscript/sections/*.tex` 或 `manuscript/sections/*.md`

---

### 阶段 6: 图表生成

**先出计划，再生成。** 先写 `reports/figure_table_plan.md`，确认后再生成。

**必须包含的图表类型：**
1. Taxonomy 图
2. 文献筛选流程图（PRISMA 风格）
3. 方法对比表（三线表）
4. 数据集/任务对比表
5. 关键系统/模型对比表
6. 挑战与未来方向表
7. 时间线图（如主题适合）

**图表规则：**
- 三线表，列名加粗，无深蓝底色
- 朴素、清晰、可打印配色
- 矢量格式优先（SVG/PDF）
- PNG ≥ 300 dpi
- 图题说明主要信息，不只是描述
- 正文必须引用每张图/表
- 无 AI 装饰图
- 流程图清晰直观、留白合理

**输出：** `figures/`, `tables/`, `reports/figure_table_plan.md`

---

### 阶段 7: 引用核查与反造假审计

**输入：** `manuscript/`, `references/references.bib`

**输出：** `reports/citation_audit.md`, `references/citation_verification.csv`

**检查清单（10 项）：**
1. BibTeX 文件是否存在
2. 正文引用是否都在 .bib 中
3. .bib 条目是否都被正文引用
4. DOI 是否可通过 API 验证
5. 标题/作者/年份/期刊是否一致
6. 是否存在 AI 编造文献
7. 是否存在引用与论点不匹配
8. 是否存在"引用 A 但论证 B"
9. 是否存在无来源的统计数字
10. 是否存在无证据的强结论

**硬性规则：**
`citation_audit.md` 必须明确写出：
- ✅ 已验证数量
- ❓ 未验证数量
- ⚠️ 存疑数量
- 🗑️ 删除建议
- 🔴 必须人工核查的引用

未验证引用不能进入最终投稿版。

---

### 阶段 8: 模拟审稿与迭代修改

**5 个审稿人角色：**

| 角色 | 检查重点 |
|------|---------|
| R1 文献覆盖 | 是否漏掉关键文献 |
| R2 方法学 | 分类、比较、逻辑、方法深度 |
| R3 学术写作 | 语言、段落、过渡、摘要、结论 |
| R4 怀疑型 | 夸大、证据不足、引用错配、创新点虚高 |
| R5 新读者 | 可读性、定义清楚、图表独立理解 |

**每轮输出：** `reviews/review_round_{n}.md`

**评分维度（1–10）：**
1. 文献覆盖
2. 分类质量
3. 批判性分析
4. 逻辑结构
5. 图表质量
6. 引用可靠性
7. 学术语言
8. 可投稿性

**每轮修改后生成：**
- `revision_plan.md`
- `change_log.md`
- `unresolved_issues.md`

**停止条件：**
1. 连续两轮主要问题无明显减少
2. 引用核查仍有严重问题
3. 用户要求停止
4. 达到课程/投稿初稿要求

**⚠️ 重要：** AI 审稿只是内部压力测试，不能代替真实同行评审。

---

### 阶段 9: 最终导出

**输出目录：** `outputs/final/`

```
outputs/final/
├── manuscript.docx (或 .tex)
├── manuscript.pdf
├── references.bib
├── literature_matrix.csv
├── citation_verification.csv
├── figure_table_plan.md
├── citation_audit.md
├── review_reports/     (所有审稿记录)
├── change_log.md
└── README_submission_checklist.md
```

**README_submission_checklist.md 必须包含：**
1. ✅ 已核查的内容列表
2. ❌ 未核查的内容列表
3. ⚠️ 需要人工复查的引用
4. 🤖 AI 生成的图表
5. 📚 数据来源声明
6. ✅ 是否适合投稿的判断
7. 📄 是否只适合作为内部初稿
8. 🔧 下一步人工修改建议

---

## 版本控制

```
versions/v0.1/    (第一版草稿)
versions/v0.2/    (第一轮修改)
versions/v0.3/    (第二轮修改)
...
```

**规则：**
- 每次输出新版本前备份旧版本
- 不覆盖旧版本
- 每版附带 version_log.md

---

## 调用记录 (Agent Run Log)

每次调用记录到 `logs/agent_run_log.csv`：

```csv
timestamp,task,input_files,output_files,model,estimated_tokens,needs_human_approval,passed_gates
2026-06-07T10:00,文献检索,project_plan.md,raw_candidates.csv,claude-sonnet-4,15000,no,g1
```

---

## 被引用的外部 Skills

本 skill 在执行过程中会调用以下已有 skills：

| 阶段 | 外部 Skill | 用途 |
|------|-----------|------|
| 1 | `keyword-literature-download` | 文献关键词搜索 |
| 4 | `critical-literature-review-pipeline` | 主题聚类与批判性分析 |
| 5 | `nature-writing-wrapper` | Nature 风格写作 |
| 5 | `academic-abstract-pipeline` | 摘要写作 |
| 7 | `literature-boundary-lock` | 引用范围锁定 |
| 7 | `citation-format-syntax-auditor` | 引用格式审计 |
| 7 | `objectivity-calibration-auditor` | 客观性校准 |
| 8 | `reviewer-red-team-auditor` | 红队模拟审稿 |
| 8 | `nsfc-reviewer-simulation-auditor` | 基金评审模拟 |
| 9 | `journal-formatting-pipeline` | 期刊格式转换 |

---

## 模板文件

本 skill 附带以下模板（位于 `templates/`）：
1. `review_project_plan.md` — 阶段 0 输出模板
2. `literature_matrix.csv` — 阶段 3 文献矩阵模板
3. `citation_verification.csv` — 阶段 7 引用核查模板
4. `evidence_card.md` — 阶段 3 证据卡片模板
5. `reviewer_report.md` — 阶段 8 审稿报告模板
6. `version_log.md` — 版本日志模板

## 辅助脚本

本 skill 附带以下脚本（位于 `scripts/`）：
1. `check_bibtex.py` — BibTeX 格式校验
2. `check_citation_coverage.py` — 引用覆盖率检查
3. `check_latex_compile.py` — LaTeX 编译检查
4. `make_project_structure.py` — 项目结构生成器

---

## 快速开始

```bash
# 1. 创建综述项目目录
python .claude/skills/autonomous-survey-agent/scripts/make_project_structure.py \
  --topic "你的综述主题" \
  --output ./my_survey

# 2. 进入项目目录，开始阶段 0
cd my_survey
# 编辑 project_plan.md，确认后进入阶段 1

# 3. 按阶段顺序执行
# 每个阶段完成后必须通过对应质量门禁
```

---

## 风险说明

1. **文献检索覆盖不全：** 免费 API 有速率限制，可能漏检重要文献
2. **PDF 获取受限：** 付费墙后的论文无法下载全文
3. **引用验证依赖 API：** CrossRef/Semantic Scholar API 可能不稳定
4. **AI 审稿的局限性：** 不能替代领域专家的真实评审
5. **语言问题：** 非母语写作需要额外人工润色
6. **时间预估：** 完整综述需要数天到数周，取决于主题复杂度
