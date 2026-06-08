# Nature Standard — 提示词模板

---

## 模板 1：Nature 图件规范化

```
请使用 nature-figure。基于以下数据、图件和论文结论，
设计或重构一张 Nature-tier scientific figure。
先输出 figure contract，包括核心科学结论、panel 结构、
证据层级、图型选择、分辨率、矢量格式、字体字号、配色、
统计标注、图注和 source data traceability。
不得伪造数据，不得覆盖原始图。
```

---

## 模板 2：已有图件投稿前检查

```
请使用 nature-figure 和 reviewer-red-team-auditor。
请检查以下图件是否符合投稿级要求，包括分辨率、矢量可编辑性、
字体统一、panel 一致性、标注清晰度、色彩一致性、
图题是否被数据支撑。只输出问题清单和修订建议。
```

---

## 模板 3：Nature 风格英文润色

```
请使用 nature-polishing、academic-vocabulary-auditor、
syntax-clarity-auditor 和 disciplinary-tone-auditor。
请润色以下论文段落，使其更接近 Nature 风格。
不得改变科学事实、不得新增数据、不得制造引用、不得夸大结果。
输出修改后文本和修改说明。
```

---

## 模板 4：Nature 风格摘要优化

```
请使用 academic-abstract-pipeline 和 nature-polishing。
请将以下摘要压缩并润色为 Nature 风格，
要求保留研究背景、科学问题、核心方法、主要发现和意义。
不得新增原文之外的数据。
```

---

## 模板 5：引用检索与支撑度判断

```
请使用 nature-citation、keyword-literature-download
和 literature-boundary-lock。请将以下论文段落拆分为可引用单元，
并为每个单元检索可核查引用。请标注每条候选文献是直接支持、
部分支持还是背景支持。不得编造作者、年份、DOI 或期刊。
```

---

## 模板 6：数据可用性声明

```
请使用 nature-data。请根据以下数据来源、代码仓库、补充材料、
限制访问条件和伦理边界，生成 Nature 风格数据可用性声明。
不得编造 DOI、accession number、仓库地址或开放状态。
缺失信息请列为待补充项。
```

---

## 模板 7：论文转 PPT

```
请使用 nature-paper2ppt、summarize、nature-figure
和 word-document-processor。请把以下论文整理成
10 到 16 页中文组会 PPT 结构。不要按论文目录机械照搬。
请根据论文类型选择叙事逻辑，每页只保留一个核心结论，
关键英文术语保留，并生成演讲者备注和资产清单。
```

---

## 模板 8：审稿意见回复

```
请使用 nature-response、reviewer-red-team-auditor
和 nature-polishing。以下是我的真实审稿意见、修订稿
和补充实验说明。请逐条拆分意见，标注风险等级，
生成谦逊但有防御力的回复框架。不得虚构实验、数据或修改。
```

---

## 模板 9：投稿前完整预检

```
请综合使用 nature-figure、nature-polishing、nature-citation、
nature-data、cover-letter-pipeline、citation-format-syntax-auditor
和 grammar-correction-auditor。请对以下论文稿做投稿前预检，
重点检查图件、语言、引用、数据可用性声明、Cover Letter、
过度声明和格式风险。只输出问题清单和修订计划。
```

---

## 模板 10：项目申报书 Nature 风格图文增强

```
请使用 nsfc-proposal-architecture-pipeline、
objective-innovation-auditor-pipeline、nature-figure、
word-document-processor 和 terminology-coherence-editor。
请根据以下项目申报书内容设计技术路线图、机制图和成果图，
并润色关键科学问题、创新点和摘要。不得编造前期数据。
```
