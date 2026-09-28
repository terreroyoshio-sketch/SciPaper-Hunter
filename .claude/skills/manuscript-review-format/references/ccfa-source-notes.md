# 证据文件：manuscript-review-format 来源出处

> 来源: mikubaka88/CCFA-Skills（MIT），只读 extract 副本：`~/.claude/reference/ccfa-skills-extract-20260928/`
> 抓取: 2026-09-28（git clone --depth 1）
> 引用级别: 源仓库文件级（可回溯到具体文件）

---

## 提取对照

| 本技能内容 | 源文件 | 说明 |
|-----------|--------|------|
| 14 节详细格式 + scope 块 | `ccf-paper-reviewer/references/fixed-output-format.md` | 节名/节序按原文逐字；原文明确"do not rename, reorder, merge, or invent peer sections" |
| 写作 9 节 / 简明 5 节 | 同上 | 原文为 "Writing Detailed Profile" 与 "Brief Version" |
| Finding record 九字段 | 同上（"Finding Record" 节） | 原文 nine fields 逐字转录；ID 规则（C001/继承 ID 不改号/[C001] 引用） |
| 七维量表 + 1-5 锚点 + 总评 1-10 + 立场带 + 置信度 1-5 | `ccf-paper-reviewer/references/calibration-and-rank.md` | 表格逐行转录；含 "Originality is an alias for Novelty"、"Quality is a synthesis" 去重规则 |
| Scorecard 模板 | 同上（"Mandatory Scorecard Output"） | markdown 表格结构照录 |
| 改判条件表 | 同上（"Score-Change Conditions"） | 三行结构照录 |
| 一致性自查 6 问 | 同上（"Consistency Check"） | 逐条转录 |
| 跨版本三分规则 | 同上（"Cross-Version Calibration"）+ SKILL.md 的 version-comparison 契约 | 冻结契约、三分不合并、降分溯源、旧问题两版一致 |

## 关键原文（引用时保持）

- "do not rename, reorder, merge, or invent peer sections"
- "Before retaining a major or critical concern, inspect the cited passage and relevant supplied appendix, then look for the strongest evidence that would invalidate the criticism."
- "A missing input is a scope limit, not a confirmed defect."
- "do not manufacture praise or impose a quota"
- "`N/A` … and `not assessed` … neither is zero."
- "Do not round an average of reviewer votes."
- "Report relative progress, current absolute readiness, and comparison confidence separately."
- "The check covers section names/order, finding fields and ID references … It does not verify scientific correctness, source truth, severity, or review completeness."

## 未提取（保留在源仓库）

- 写作子量表：`ccf-paper-reviewer/references/writing-review/writing-review-rubric.md`
- 结构校验脚本：`ccf-paper-reviewer/scripts/validate_version_comparison.py`（可对保存的默认格式报告跑 `--report --mode scientific|writing` 校验）
- 其余 16 个技能（idea/literature/experiment/integrity/rebuttal/figures…）与 ccf-common 共享控制文件

## 边界

- CCFA-Skills 为 MIT（LICENSE 在 extract 根目录）；本技能为格式规范转录（功能性文本），保留来源与许可声明。
- 源项目自注其校验"只验证结构与引用"——格式合规不代表评审质量；本技能不背书其技能族效果。
- extract 副本为只读审计材料，未安装、未运行其任何脚本。
