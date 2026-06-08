# Nature Figure + Word Document Processor — 提示词模板

---

## 模板 1：Nature 风格科研图件生成

```
请使用 nature-figure。根据以下数据和论文结论，设计一张符合 Nature-tier journal 风格的科研图件。
先明确 figure contract，包括核心结论、证据层级、图型选择、统计标注、颜色规范、字体、尺寸、
导出格式和 source data traceability。不得伪造数据。输出可复现绘图代码和图注草稿。

[在此处粘贴数据和结论]
```

---

## 模板 2：多面板论文图设计

```
请使用 nature-figure。请将以下实验结果整理为一张多面板 figure。
要求先规划 panel A、B、C、D 的逻辑关系，再生成绘图代码。
每个 panel 必须对应明确的科学结论。不得为了美观而改变数据。

[在此处粘贴实验数据]
```

---

## 模板 3：论文图件审稿人检查

```
请使用 nature-figure 和 reviewer-red-team-auditor。
请从 Nature 审稿人视角检查以下图件设计，重点审查数据是否支撑图题结论、
统计标注是否充分、图注是否过度解释、颜色和版式是否符合发表标准。

[在此处粘贴图件描述和数据]
```

---

## 模板 4：Word 文档创建

```
请使用 word-document-processor。请根据以下内容创建一份结构规范的 Word 文档，
保留标题层级、表格、图题、参考文献、页眉页脚和可编辑格式。
不要只输出 Markdown，最终输出 docx。

[在此处粘贴文档内容]
```

---

## 模板 5：Word 文档修改与格式保留

```
请使用 word-document-processor。请读取以下 docx 文件，在尽量保留原格式、样式、编号、
表格和图注的前提下，完成指定修改。修改前先备份原文件。输出修改后的 docx 和修改记录。

[指定 docx 路径和修改要求]
```

---

## 模板 6：机械工程学报 Word 排版

```
请使用 word-document-processor、markitdown 和 terminology-coherence-editor。
请读取《机械工程学报》模板和我的论文内容，按模板整理成 Word 格式。
要求保留中文标题、英文标题、摘要、关键词、正文双栏、图题、表题、参考文献和作者简介。
```

---

## 模板 7：项目申报书 Word 排版

```
请使用 word-document-processor、nsfc-proposal-architecture-pipeline 和 terminology-coherence-editor。
请把以下项目申报书内容整理为规范 Word 文档，保持表格结构、标题层级、经费预算表、
进度安排和参考文献格式。

[在此处粘贴申报书内容]
```

---

## 模板 8：文献综述图文稿

```
请使用 keyword-literature-download、critical-literature-review-pipeline、nature-figure 和 word-document-processor。
先基于已核实文献生成综述结构，再设计一张机制或理论框架图，最后输出 Word 综述稿。

[在此处粘贴文献清单和研究主题]
```
