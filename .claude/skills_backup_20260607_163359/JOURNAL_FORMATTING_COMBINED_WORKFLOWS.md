# 期刊格式转换 — 组合工作流说明

---

## A. 标准投稿排版工作流

```
1. Using-Superpowers
   明确目标期刊、投稿格式、输出格式、是否盲审和验收标准。

2. Markitdown
   将 PDF、Word 或 LaTeX 原稿转成可处理文本。

3. journal-formatting-pipeline
   执行扉页、摘要、标题、引用、参考文献、图表、统计单位和布局审计。

4. word-document-processor
   生成或修改 DOCX，保留可编辑格式。

5. citation-format-syntax-auditor
   检查引用句法。

6. grammar-correction-auditor
   最终语法校对。
```

**适用场景**: 向任何期刊投稿的标准格式排版流程。

**含公式稿件增强**:
若稿件包含数学公式，在步骤 1-2 之间插入：
```
1.5. math-doc-pipeline
    将 Markdown 源稿中的 LaTeX 公式统一规范，用 Pandoc/XeLaTeX
    预检排版和公式渲染，确保 DOCX 中公式为 Word 原生 OMML、
    PDF 中公式正确渲染。再进入 journal-formatting-pipeline 做格式审计。
```

---

## B. APA 第 7 版格式转换工作流

```
1. journal-formatting-pipeline
   整体格式对齐 APA 第 7 版。

2. in-text-citation-format-converter
   转换正文引用（作者年份制）。

3. reference-list-style-aligner
   格式化参考文献列表。

4. statistical-unit-format-auditor
   审计统计格式（斜体、大小写、间距）。

5. layout-spacing-constraint-validator
   检查行距（双倍行距）、缩进（首行缩进 0.5in）、页边距（1in）。
```

**适用场景**: 投稿要求 APA 第 7 版格式的心理学、教育学、社会科学期刊。

---

## C. 盲审稿生成工作流

```
1. word-document-processor
   备份并读取原始 DOCX。

2. blind-review-anonymization-auditor
   执行匿名化审计。

3. reference-list-style-aligner
   检查自引是否需要匿名处理。

4. docs
   生成匿名化记录和投稿清单。
```

**适用场景**: 双盲同行评审投稿前的匿名化处理。

---

## D. Nature / CNS 投稿格式工作流

```
1. nature-figure
   检查图件质量（分辨率、格式、颜色模式）。

2. nature-data
   生成数据可用性声明。

3. nature-polishing
   润色语言。

4. journal-formatting-pipeline
   执行格式和匿名化预检。

5. cover-letter-pipeline
   生成投稿信。
```

**适用场景**: Nature、Science、Cell 及其子刊投稿。

---

## E. 学位论文或中文期刊排版工作流

```
1. word-document-processor
   读取学校或期刊模板。

2. journal-formatting-pipeline
   适配标题、摘要、图表、参考文献和布局。

3. reference-list-style-aligner
   转换参考文献格式（如 GB/T 7714）。

4. layout-spacing-constraint-validator
   检查页边距、行距、缩进。
```

**适用场景**: 学位论文排版或中文期刊（如《科学通报》《中国科学》）投稿。

---

## F. Cover Letter + 稿件一体化投稿工作流

```
1. cover-letter-pipeline
   生成投稿信。

2. journal-formatting-pipeline
   格式化主稿件。

3. ethics-compliance-statement-formatter
   格式化伦理与合规声明。

4. reviewer-data-formatter
   格式化推荐/回避审稿人信息。

5. journal-formatting-pipeline + blind-review-anonymization-auditor
   生成盲审版本。
```

**适用场景**: 需要同时准备 Cover Letter、主稿和盲审稿的完整投稿包。

---

## G. 文献综述 + 格式输出工作流

```
1. critical-literature-review-pipeline
   生成批判性文献综述。

2. introduction-reconstruction-pipeline
   重构引言部分。

3. journal-formatting-pipeline
   统一格式输出。

4. citation-format-syntax-auditor
   优化引用句法。
```

**适用场景**: 先写文献综述和引言，再统一格式投稿。

---

## H. 修改稿重投格式检查工作流

```
1. journal-formatting-pipeline
   重新执行格式审计。

2. nature-response
   起草修改回复信。

3. reference-list-style-aligner
   检查新增参考文献格式。

4. grammar-correction-auditor
   语法二次校对。
```

**适用场景**: 收到审稿意见后修改稿重投时的格式复查。

---

## I. 含公式稿件排版 + 投稿工作流

```
1. math-doc-pipeline
   接收 Markdown 源稿，统一 LaTeX 公式语法（`$...$`/`$$...$$`）。
   创建 build/ 目录。
   生成 reference.docx 控制样式。
   用 Pandoc + XeLaTeX 预检 PDF 公式渲染。
   检查 DOCX 中公式是否为 Word 原生 OMML。

2. journal-formatting-pipeline
   对排版后的稿件执行扉页、摘要、标题、引用、参考文献、
   图表、统计单位和布局审计。

3. scientific-visualization / nature-figure
   审计图件质量和期刊规格。

4. word-document-processor
   如需要，做最终格式微调。

5. grammar-correction-auditor + citation-format-syntax-auditor
   语法和引用二次检查。
```

**适用场景**: 数学/物理/工程/计算机等含大量公式的论文投稿。
