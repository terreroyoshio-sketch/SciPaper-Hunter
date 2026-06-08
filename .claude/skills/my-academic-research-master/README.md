# my-academic-research-master

本地科研总控 Skill — 编排 ARS + 本地 skills 执行完整科研流水线。

## 快速开始

```bash
# 创建科研项目
python scripts/make_project_structure.py \
  --topic "Your Research Topic" \
  --output ./my_research \
  --lang en

# 编辑项目计划
# → 00_plan/project_plan.md

# 开始文献检索
# → 参考 references/local_pipeline.md 的 Stage 1
```

## 文件结构

```
.claude/skills/my-academic-research-master/
├── SKILL.md                    # 主控 skill
├── README.md                   # 本文件
├── references/                 # 规则文件
│   ├── anti_fabrication_rules.md
│   ├── citation_verification_rules.md
│   ├── literature_review_rules.md
│   ├── paper_writing_rules.md
│   ├── reviewer_simulation_rules.md
│   ├── experiment_integrity_rules.md
│   ├── chinese_academic_style_rules.md
│   ├── local_pipeline.md       # 10 阶段流水线
│   ├── quality_gates.md        # 5 道质量闸门
│   ├── experiment_agent_rules.md
│   └── openscholar_style_rules.md
├── templates/                  # 模板文件
│   ├── project_plan.md
│   ├── literature_matrix.csv
│   ├── citation_verification.csv
│   ├── evidence_card.md
│   ├── reviewer_report.md
│   ├── revision_log.md
│   ├── ai_usage_disclosure.md
│   ├── submission_checklist.md
│   └── quick_prompts.md
└── scripts/                    # 辅助脚本
    ├── check_bibtex.py
    ├── check_citation_coverage.py
    ├── check_claim_source_alignment.py
    ├── check_latex_compile.py
    ├── check_docx_structure.py
    └── make_project_structure.py
```

## 编排的 Skills

| Skill | 来源 | 阶段 |
|-------|------|------|
| deep-research | ARS | 0, 1, 2 |
| keyword-literature-download | 本地 | 1 |
| critical-literature-review-pipeline | 本地 | 4 |
| academic-paper | ARS | 5 |
| academic-paper-reviewer | ARS | 8 |
| reviewer-red-team-auditor | 本地 | 8 |
| citation-format-syntax-auditor | 本地 | 5, 7 |
| literature-boundary-lock | 本地 | 7 |
| objectivity-calibration-auditor | 本地 | 5 |

## 质量门禁

| 闸门 | 条件 |
|------|------|
| 文献闸门 | 每子方向≥5篇，每结论≥2来源 |
| 引用闸门 | 0编造引用，0编造DOI |
| 实验闸门 | 有日志、有种子、有对照 |
| 语言闸门 | 无夸张/AI模板/公众号表达 |
| 伦理闸门 | AI披露、伦理审批、匿名化 |
