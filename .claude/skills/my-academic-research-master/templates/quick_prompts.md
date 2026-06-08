# Quick Prompts

**文件:** `templates/quick_prompts.md`
**用途:** 常用科研任务的快捷提示词。

---

## 1. 选题提示词

```
请使用 my-academic-research-master、deep-research 和 Brainstorming，
围绕以下方向提出 5 个可执行科研选题。
每个选题必须包含研究问题、创新点、可用开源数据集、可检索关键词、
近 5 年代表文献、可行实验方案、投稿方向和风险。
禁止编造文献。

方向是：{主题}
```

## 2. 文献综述提示词

```
请使用 my-academic-research-master、keyword-literature-download、
critical-literature-review-pipeline 和 citation-format-syntax-auditor，
为以下主题建立文献综述项目。
先检索并生成 literature_matrix.csv，再写 taxonomy 和 outline，
不要直接写正文。

主题是：{主题}
```

## 3. SCI 初稿提示词

```
请使用 academic-pipeline，从 Stage 1 开始，为以下研究生成论文初稿。
必须先完成文献核验、证据卡片、结构设计和图表计划。
没有证据的内容只允许写成待验证假设。

研究主题是：{主题}
```

## 4. 论文审稿提示词

```
请使用 academic-paper-reviewer 和 reviewer-red-team-auditor 审查我的论文。
重点检查文献真实性、引用是否支撑论点、方法是否合理、
结果是否被夸大、语言是否像投稿论文。
请输出 Major Issues、Minor Issues、具体修改表和是否适合投稿。

论文路径：{路径}
```

## 5. 项目申报书提示词

```
请使用 critical-literature-review-pipeline、objective-innovation-auditor-pipeline
和 nsfc-proposal-architecture-pipeline，帮我重构项目申报书。
重点检查立项依据、科学问题、研究内容、创新点、技术路线和可行性。
所有创新点必须有对比文献或前期基础支撑。

申报书路径：{路径}
```

## 6. 引用核查提示词

```
请只做引用核查，不要润色。
检查正文所有引用是否存在、BibTeX 是否完整、DOI 是否真实、
引用是否支撑所在句子。
输出 VERIFIED、MISMATCH、NOT_FOUND、NEEDS_HUMAN_CHECK 四类结果。

论文路径：{路径}
BibTeX路径：{路径}
```

## 7. 图表美化提示词

```
请只优化图表，不改正文结论。
表格使用简洁三线表，列名加粗即可，不要深蓝底色。
流程图保持白底、清晰、直观，优先输出 SVG 或 draw.io，可导入 Visio。
所有图表必须能被正文引用。

图表计划路径：{路径}
```
