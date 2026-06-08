# autonomous-survey-agent

自主科研综述写作 Agent 工作流 — 9 阶段流水线，从选题冻结到最终导出。

## 快速开始

### 1. 创建综述项目

```bash
python .claude/skills/autonomous-survey-agent/scripts/make_project_structure.py \
  --topic "你的综述主题" \
  --output ./my_survey \
  --lang zh
```

### 2. 按 9 阶段执行

```
阶段 0: 选题冻结       → 编辑 project_plan.md
阶段 1: 文献检索       → references/raw_candidates.csv
阶段 2: 质量评分       → references/scored_literature.csv
阶段 3: 证据卡片       → notes/evidence_cards/
阶段 4: Taxonomy       → structure/taxonomy.md
阶段 5: 写作           → manuscript/sections/
阶段 6: 图表           → figures/, tables/
阶段 7: 引用核查       → reports/citation_audit.md
阶段 8: 模拟审稿       → reviews/
阶段 9: 导出           → outputs/final/
```

### 3. 运行辅助脚本

```bash
# 检查 BibTeX 格式
python scripts/check_bibtex.py references.bib

# 检查引用覆盖率
python scripts/check_citation_coverage.py manuscript.tex references.bib

# 检查 LaTeX 编译
python scripts/check_latex_compile.py manuscript.tex
```

## 目录结构

```
.claude/skills/autonomous-survey-agent/
├── SKILL.md               # 主 skill 定义（9 阶段 + 6 质量门禁）
├── README.md              # 本文件
├── templates/             # 模板文件
│   ├── review_project_plan.md
│   ├── literature_matrix.csv
│   ├── citation_verification.csv
│   ├── evidence_card.md
│   ├── reviewer_report.md
│   └── version_log.md
└── scripts/              # 辅助脚本
    ├── check_bibtex.py
    ├── check_citation_coverage.py
    ├── check_latex_compile.py
    └── make_project_structure.py
```

## 核心能力

| 能力 | 说明 |
|------|------|
| 文献检索 | arXiv/Semantic Scholar API + Playwright 自动化 |
| LQS 评分 | 6 维度加权评分（主题相关 30%/方法 20%/发表 15%/被引 15%/时效 10%/验证 10%） |
| 引用深度分类 | A(1-3段)/B(2-5句)/C(1句)/D(剔除) |
| Evidence Card | 每篇 A 类文献详细卡片 |
| Taxonomy | 多维矩阵分类，必须含空白区域 |
| 段落逻辑 | Claim-Evidence-Implication / Compare-Contrast |
| 反造假审计 | 10 项检查：BibTeX、DOI、引用匹配、论点对应 |
| 模拟审稿 | 5 角色（文献覆盖/方法学/写作/怀疑型/新读者） |
| 版本控制 | v0.1/v0.2/... 快照保存 |
| 质量门禁 | 6 道 hard gates，未通过不准进入最终版 |

## 调用外部 Skills

| 阶段 | Skill | 用途 |
|------|-------|------|
| 1 | `keyword-literature-download` | 文献关键词搜索 |
| 4 | `critical-literature-review-pipeline` | 主题聚类与批判分析 |
| 5 | `nature-writing-wrapper` | 学术写作 |
| 7 | `citation-format-syntax-auditor` | 引用格式审计 |
| 8 | `reviewer-red-team-auditor` | 红队模拟审稿 |

## 硬性规则（不可绕过）

1. 不编造文献、DOI
2. 未下载 PDF 不能说已阅读
3. AI 自评不能充当真实同行评审
4. 不承诺具体发表结果
5. 全过程可追溯，每步有记录
6. 人工确认不能跳过

## 风险说明

- **文献覆盖不全：** 免费 API 有速率限制
- **PDF 获取受限：** 付费墙后的论文无法下载全文
- **AI 审稿局限性：** 不能替代真实专家评审
- **时间预估：** 完整综述数天到数周
