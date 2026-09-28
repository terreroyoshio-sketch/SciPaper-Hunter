---
name: manuscript-review-format
description: 当需要产出结构化论文评审报告时使用 —— 审稿、模拟审稿人、投稿成熟度评估、稿件硬伤检查、评审打分、版本对比评审、审稿综合意见。提供三档固定格式（详细 14 节 / 写作 9 节 / 简明 5 节）、带反证复核的 finding record 规范、七维评分量表（1-5）与 1-10 总评锚点、跨版本对比三分规则。格式与量表提取自 CCFA-Skills（MIT）公开文档，只做格式参考，不安装其技能族。
type: reference
version: 1.0.0
source: mikubaka88/CCFA-Skills（MIT）ccf-paper-reviewer 公开文档，2026-09-28 快照（extract 副本在 ~/.claude/reference/ccfa-skills-extract-20260928/）
triggers:
  - "审稿"
  - "评审报告"
  - "模拟审稿"
  - "投稿成熟度"
  - "结构化评审"
  - "评审格式"
  - "稿件硬伤"
  - "评审打分"
  - "版本对比"
  - "review report"
  - "reviewer panel"
  - "评审意见怎么写"
---

# Manuscript Review Format

## 核心原则

三条不可让步的纪律（来源原文见 `references/ccfa-source-notes.md`）：

- **格式固定**：节名、节序不得重命名、重排、合并或自创平级节。模板外格式（venue 专用或用户指定）可以覆盖，但必须**声明这是覆盖**，不得假装通过了默认格式校验。
- **每条判断落到证据锚点**：不得写"文章组织不好"；要写"§3.1（第 2 段）引入方法但未命名/未说明动机，且未把增量贡献与组件分离。清晰度 3/5"。
- **反证先行 + 缺材料≠缺陷**：保留一条 major/critical 问题前，必须先检查被引段落与附录中**最强的一条可反驳它的材料**，记录复核结果（survived / narrowed / withdrawn）；缺失的输入是范围限制，不是已确认的缺陷。

## 三档格式

选择规则：**detailed 为默认**；只有用户显式要求"简要版 / 简短 / 快速概览 / 只给结论 / brief"才用 brief。短 prompt、单篇稿件、窄主题、未要求打分**都不算** brief 请求。报告详细程度与评审范围独立（详细格式的写作评审仍只评写作）。

### A. 详细版（默认）：14 节

科学/完整评审与详细版本对比用全部 14 节；不适用的节**保留标题**并给一行原因，不得删节。节名（中/英双语，按序）：

1. 评审信息与范围 / Review Information（含开头 scope 块：`Template: ccfa-review-1`、mode、detail、rubric、source version、contribution type）
2. 总体结论与关键理由 / Expected Review Outcome（结论由 findings 推出，不得先定分再造理由）
3. 预审与投稿适配 / Desk Rejection Assessment（pass / concern / not assessed；未知页数/匿名信息不构成失败）
4. 论文摘要与贡献拆解 / Summary And Contributions（不带批评）
5. 主要优势 / Strengths（逐条编号 + 具体锚点；不设表扬配额，也不制造表扬）
6. 主要问题与严重程度 / Major Concerns（每条用 finding record）
7. 次要问题与写作表达 / Minor And Presentation Concerns（同一科学缺陷不重复拆成多条写作扣分）
8. 新颖性与相关工作 / Novelty And Positioning（表格：Work / 已有结论 / 重叠与剩余差异 / 后果·concern ID；禁止编造对比行）
9. 方法正确性与主张支撑 / Soundness And Claim Support（表格：Claim·位置 / 已查支撑 / 判断 / 后果·concern ID）
10. 实验、证明与可复核性 / Evaluation And Reproducibility（按论文类型定证据期望；理论文不强制实证清单）
11. 多视角评审与综合意见 / Reviewer Perspectives And Synthesis（多视角可一致；未实际分开调用不得声称独立评审人）
12. 维度评分与置信度 / Critical Reviewer Ratings（七维表 + scorecard，见下）
13. 作者关键问题与改判条件 / Questions And Decision Conditions（区分：澄清 / 补证据 / 实质研究变更；不得承诺录用或保证提分）
14. 修改优先级与复审记录 / Action Priorities And Re-Review（表格：ID / 优先级 / 必改项 / 为何重要 / 状态·版本）

### B. 写作版：9 节（仅写作，无科学录用分）

1. 评审信息与范围 / Review Information　2. 写作结论与关键理由 / Writing Outcome　3. 论证与结构重建 / Argument And Structure　4. 主要优势 / Strengths　5. 写作问题与严重程度 / Writing Concerns　6. 读者视角与综合意见 / Reader Perspectives And Synthesis　7. 写作评分与置信度 / Writing Ratings（用其独立写作量表，本技能未提取）　8. 作者关键问题与改判条件 / Questions And Decision Conditions　9. 修改优先级与复审记录 / Action Priorities And Re-Review

### C. 简明版：5 节（仅显式请求）

1. 结论 / Verdict　2. 主要优点 / Strengths　3. 关键问题 / Concerns（用紧凑 finding record，可省重复文字，不可省证据基础）　4. 评分概览与置信度 / Ratings　5. 下一步 / Next Actions

简明 ≠ 无根据；不得因展示简短而做更浅的科学评审。

## Finding Record（问题记录规范）

每条问题**只定义一次**：`### C001: <短标题>`，新 ID 用 `C001, C002...`；继承的 ID（如 R1）不得改号；别处引用用 `[C001]`。已解决的问题保留身份与紧凑记录，不得重编号或静默删除。九字段：

```text
Type / 类型: confirmed_flaw | unsupported_claim | clarification
Severity / 严重程度: critical | major | minor
Location / 位置: 精确到页/节/段/行/图/表
Evidence / 证据: 已查依据（必要时含来源版本）
Countercheck / 反证复核: 已查的最强反驳与其结果（minor 可写 not needed + 原因）
Judgment / 判断: 对主张或读者的后果（不得从缺失输入推断缺陷）
Criterion / 维度: 影响的维度
Resolution / 解决或改判条件: 可行的解决/改变判断的条件
Status / 状态: unresolved | partially_resolved | resolved | not_applicable
```

类型三分不可与严重度、置信度混用：`confirmed_flaw` 要有观察到的错误或矛盾；`unsupported_claim` 针对实际提出的主张；`clarification` 是未决问题。

## 七维评分量表（generic-7）

维度分 1-5 整数；**顺序固定**（`Originality` 是 Novelty 的别名、不加分；`Quality` 是综合、不是第八维；定位/相关工作只做 Novelty 的证据，不重复扣分）：

| Key | English | 中文 | 强证据（高分） | 弱证据（低分） |
|-----|---------|------|---------------|---------------|
| novelty | Novelty | 新颖性 | 非平凡新贡献/洞见，与最近工作有已验证差异 | 已证重叠、过度宣称、贡献不清 |
| soundness | Soundness | 正确性 | 假设/推导/算法/设计对主张有效 | 已识别逻辑矛盾、无效假设、证明缺口、协议缺陷 |
| evidence | Evidence | 证据 | 与主张与贡献类型匹配的可查支撑 | 中心主张无支撑或被已查材料反驳 |
| significance | Significance | 意义 | 对目标社区有实质新知识/能力/数据/实用价值 | 宣称重要性实为不符 |
| clarity | Clarity | 清晰度 | 贡献/机制/证据/边界可复原 | 具体组织、记号或解释缺陷阻碍理解 |
| reproducibility | Reproducibility | 可复核性 | 定义/步骤/协议/数据细节足以核查 | 已识别缺失使相关主张无法独立评估 |
| ethics_limitations | Ethics / Limitations | 伦理与局限 | 风险与实质局限被处理并披露 | 实质风险/局限未处理（政策问题须引已核规则） |

**维度锚点**：5 明显强 / 4 好 / 3 混合 / 2 弱 / 1 致命或近致命。

**总评 1-10**：10 获奖级或一线录用；9 强接受；8 接受；7 弱接受；6 边界偏正；5 边界偏负；4 弱拒绝；3 拒绝；2 强拒绝；1 预审级/不可审。

**立场带**：明确接受（多数维度 4-5，总评 8-10）｜倾向接受（1-2 个中等关切，通常 7）｜边界（优劣均衡，通常 5-6）｜倾向拒绝（1 个重大或多个中等关切，通常 4）｜明确拒绝（致命技术/新颖性/证据/政策/会场问题，通常 1-3）。

**置信度 1-5**：5 决定性证据与反证均已核查、残余不确定很小；4 主判断检查充分；3 有实质未决点可能改变判断；2 关键点或自身领域知识不足；1 仅够试探性判断。**置信度独立于质量分**；低置信度改变的是确定性，不自动改质量分。

**打分规则**：每维至少一条可查的稿件引用；`N/A`（不适用）与 `not assessed`（材料未提供）都**不是 0**；不得对同一问题双重扣分；不得对评审人打分取平均凑整数；6/7 之间须说明决定性取舍；未提供附录/代码本身不迫使置信度到 1。**无真实可比语料时，省略排名、百分位、超越计数与分布图**。

### Scorecard（放第 12 节内）

```markdown
### Scorecard

| Dimension | Score (1-5) | Confidence (1-5) | Evidence basis | Deduction / score-change condition |
|:---|:---:|:---:|:---|:---|
| [七维按序] | [1-5 或状态] | [1-5 或状态] | [节/段/行] | [扣分与修复条件] |

**Overall:** [1-10]  | **Scholarly Confidence:** [1-5]

**Recommendation:** [accept/weak-accept/borderline/weak-reject/reject]
**Verdict:** [什么证据会改变判断，为什么]
```

无打分请求时：Score 列换 Judgment 列，行数不变，定性判断替代。

### 改判条件表（scorecard 后）

| Change | Condition | Likely affected dimensions | Expected movement |
| --- | --- | --- | --- |
| 提分 | [具体证据/修改] | [维度] | [可到下一锚点；不保证] |
| 降分 | [更细检查揭示的失败] | [维度] | [可到更低锚点或改变立场] |
| 短期难改 | [需要新结果/新方法] | [维度] | [投稿前不太可能改变] |

## 跨版本对比（re-review / 版本比较）

- 比较前**冻结契约**：维度、权重、锚点、评审角色、阈值、证据标准。
- 输出**三分且永不合并**：相对进步（历史/当前/差值/权重记分卡）｜当前绝对成熟度（独立记分卡）｜比较置信度。第 12 节用三个子标题：`### Relative Progress / 相对进步`、`### Absolute Readiness / 绝对成熟度`、`### Confidence And Comparability / 置信度与可比性`。
- 每个**降分必须可溯源**：当前版本回退或新揭露的证据；此前未察觉的旧问题对**两个版本一致适用**，不得只降当前版。
- 问题账本保留历史维度与权重；不做逐迭代的日期化报告副本（一份 canonical 报告就地更新）。

## 定稿前一致性自查

1. 总评是否与**最强未解决弱点**一致？
2. 怀疑型评审人会不会重复某个致命关切？
3. 每条优势是否有精确稿件证据？
4. 改判条件是否具体可行？
5. 分数是否按目标会场校准（而非泛泛的积极）？
6. 版本对比是否两版同契、且每个降分都过了溯源规则？

## 来源与边界

- 格式与量表提取自 mikubaka88/CCFA-Skills（**MIT**）的 `ccf-paper-reviewer` 公开文档（`references/fixed-output-format.md` 与 `references/calibration-and-rank.md`），快照 2026-09-28；extract 只读副本在 `~/.claude/reference/ccfa-skills-extract-20260928/`。逐条出处见 `references/ccfa-source-notes.md`。
- 本技能**只提取格式规范**，不含其 17 技能族的其余内容；未安装（其安装形态为多宿主 skill 包）。
- **写作量表未提取**（`writing-review/writing-review-rubric.md` 在源仓库，本技能只引用其存在）；**其确定性校验脚本未安装**（`ccf-paper-reviewer/scripts/validate_version_comparison.py` 在源仓库，可对保存的默认格式报告做结构校验——不含科学正确性）。
- 源项目自注：其 check 脚本"只验证结构与引用，不等于模型质量"；本技能保持同一限定——格式合规 ≠ 评审质量。
