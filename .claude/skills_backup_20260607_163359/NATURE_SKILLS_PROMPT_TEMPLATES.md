# Nature Skills — 提示词模板

---

## 模板 1：Nature 风格图件生成

```
请使用 nature-figure。根据以下数据、实验结果和论文结论，
设计一张 Nature-tier scientific figure。先输出 figure contract，
包括核心科学结论、panel 结构、图型选择、统计标注、颜色规则、字体、
尺寸、导出格式和 source data traceability。不得伪造数据。
输出可复现绘图代码、图注草稿和审稿人风险提示。
```

---

## 模板 2：多面板图重构

```
请使用 nature-figure。请把以下实验结果组织为一张多面板图。
每个 panel 必须回答一个不同科学问题，避免重复表达。
要求给出 panel A、B、C、D 的逻辑关系、推荐图型、输入数据、可视化要点和图注。
```

---

## 模板 3：Nature 风格英文润色

```
请使用 nature-polishing、academic-vocabulary-auditor、syntax-clarity-auditor
和 disciplinary-tone-auditor。请润色以下英文论文段落，要求符合 Nature 风格，
保留科学含义，不夸大结果，不改变数据，不制造引用。
输出修改后文本和逐条修改说明。
```

---

## 模板 4：摘要润色与压缩

```
请使用 academic-abstract-pipeline 和 nature-polishing。
请将以下摘要压缩到目标字数，并按 Nature 风格优化背景、问题、方法、结果和意义。
不得新增源文本之外的数据。
```

---

## 模板 5：Nature 引用检索

```
请使用 nature-citation、keyword-literature-download 和 literature-boundary-lock。
请将以下论文段落拆成可引用单元，检索能直接支持每个论断的高质量文献。
不得虚构 DOI、作者、期刊或年份。请标注每条候选引用是直接支持、部分支持
还是背景支持，并导出 RIS / DOI 列表。
```

---

## 模板 6：数据可用性声明

```
请使用 nature-data。请根据以下数据来源、代码情况、补充材料、
限制访问条件和仓库信息，生成符合 Nature 风格的数据可用性声明。
不得编造 accession number、DOI 或仓库地址。
若缺失必要信息，请列出需要补充的字段。
```

---

## 模板 7：论文转组会 PPT

```
请使用 nature-paper2ppt、nature-figure 和 word-document-processor。
请把以下论文整理成 10 到 16 页中文组会 PPT 结构。
不要按 Introduction、Methods、Results、Discussion 机械照搬，
而要按科学论证重组。每页只讲一个核心点，关键英文术语保留，
并生成演讲者备注和资产清单。
```

---

## 模板 8：项目申报书图文增强

```
请使用 nsfc-proposal-architecture-pipeline、objective-innovation-auditor-pipeline、
nature-figure 和 word-document-processor。请根据以下项目申报书内容，
提取关键科学问题、研究内容、创新点和技术路线，并设计 1 张技术路线图、
1 张机制图和 1 张预期成果图。不得编造前期数据。
```

---

## 模板 9：文献综述证据图谱

```
请使用 critical-literature-review-pipeline、nature-citation 和 nature-figure。
请基于已核实文献构建主题聚类、争议点和方法局限，
并设计一张 evidence map 或 conceptual framework figure。
不得使用未核实文献。
```

---

## 模板 10：投稿前完整检查

```
请综合使用 nature-polishing、nature-citation、nature-data、nature-figure、
citation-format-syntax-auditor 和 grammar-correction-auditor。
请对以下论文稿进行投稿前检查，重点检查语言、图件、引用、
数据可用性声明、过度声明和格式风险。
只输出问题清单和修订建议，不要擅自改动原稿。
```
