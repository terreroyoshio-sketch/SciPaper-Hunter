# 期刊格式转换与稿件排版 — 调用模板

---

## 模板 1：完整期刊格式转换

```
请使用 journal-formatting-pipeline、word-document-processor
和 citation-format-syntax-auditor。以下是我的稿件、参考
文献列表和目标期刊格式指南。请先备份原始文件，再进行扉页、
摘要关键词、标题层级、正文引用、参考文献、图表标题、统计
单位、布局间距、脚注尾注和盲审匿名化审计。不得更改数据和
科学内容。输出格式化稿件、修改记录和需人工核对清单。
```

## 模板 2：APA 第 7 版格式适配

```
请使用 journal-formatting-pipeline。请将以下稿件格式对齐
APA 第 7 版。重点检查标题层级、正文引用、参考文献列表、
统计报告、表格标题、图注、行距、缩进和页边距。不得编造
DOI、页码或缺失参考文献信息。
```

## 模板 3：参考文献格式整理

```
请使用 reference-list-style-aligner 和
in-text-citation-format-converter。请将以下正文引用和
参考文献列表转换为目标期刊格式，并检查正文引用与参考文献
是否一一对应。不得添加或删除引用。缺失 DOI、期号、页码
请标注。
```

## 模板 4：图表标题格式化

```
请使用 figure-table-caption-formatter 和 nature-figure。
请检查以下图题、表题、注释和正文引用，确保编号顺序、标题
位置、格式和图表引用符合目标期刊要求。不要更改表格数据和
图形内容。
```

## 模板 5：统计与单位格式审计

```
请使用 statistical-unit-format-auditor。请检查以下结果
部分的统计符号、p 值、置信区间、效应量、单位和数字格式。
只改格式，不得更改任何数值或统计结论。
```

## 模板 6：盲审匿名化

```
请使用 blind-review-anonymization-auditor。以下是我的
稿件和作者信息。请生成双盲投稿版本，删除或屏蔽作者姓名、
机构、致谢、基金和可能暴露身份的自引。不要误删非作者引用。
输出匿名化记录表和需作者确认的自引清单。
```

## 模板 7：Word 投稿稿排版

```
请使用 word-document-processor、journal-formatting-pipeline
和 layout-spacing-constraint-validator。请按目标期刊指南
整理 DOCX，保留可编辑格式、标题层级、图表、参考文献、
页眉页脚和修改记录。不要把整页转成图片。
```

## 模板 8：投稿前格式预检

```
请使用 journal-formatting-pipeline、cover-letter-pipeline、
nature-data 和 grammar-correction-auditor。请对投稿材料
进行预检，检查主稿、盲审稿、Cover Letter、数据可用性声明、
参考文献、图表和补充材料是否存在格式或合规风险。
```

---

*更多组合方式请参见 JOURNAL_FORMATTING_COMBINED_WORKFLOWS.md*
