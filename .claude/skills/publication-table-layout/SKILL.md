---
name: publication-table-layout
description: 论文三线表排版与几何验收：python-docx 构造（仅三条横线、表级居中、固定列宽、按语义列对齐、表头跨页重复）+ XML 属性检查 + LibreOffice 渲染后 pdfplumber 实测居中（center_error ≤1.0mm）。Word/DOCX 表格不居中、列宽漂移、表内对齐不一致、边框杂乱时使用。不负责图件（各家族技能）、不负责表格数据本身。
---

# Publication Table Layout — 三线表排版

## 四层分离（不得混为一谈）

1. **表级对齐**：`Table.alignment = CENTER`（= 底层 `w:jc`），控制整表在左右页边距之间居中——**≠ 单元格文字居中**（python-docx 官方文档语义）。
2. **表宽**：由内容自然宽度决定（短表**不**撑满全页；长表可接近 text width）；text width = 页宽 − 左右边距，禁止写死厘米值。
3. **列宽**：内容估算 + **fixed layout** + autofit OFF（防 Word 打开后漂移）。
4. **单元格对齐（按语义）**：表头通常居中；长文本列左对齐；数值/百分比/p 值列一致（居中或按小数点）；第一列不得因"整体居中"而机械居中；垂直居中。

## 三线纪律

只允许 3 条规则线：**top / header separator / bottom**（top/bottom 略粗于中间线，1.5pt vs 1.0pt）；禁止竖线、全网格、底纹、粗边框。表题在表**上方**、左对齐、与表格间距统一。

## 用法

```python
from three_line_table import add_three_line_table, style_document
style_document(doc)                     # Normal：Times New Roman + SimSun，10.5pt
add_three_line_table(doc, headers, rows,
                     col_align=["left", "center", "center"],  # 语义对齐
                     caption="表 1. …")
doc.save("table.docx")
```

## 几何验收（`scripts/table_qa.py`）——两条证据链

- **XML 链**：`w:jc=center`、`tblLayout=fixed`、autofit OFF、tblGrid 宽度和、逐列 paragraph 对齐集合、垂直对齐、边框清单（越界边 → violation）。
- **渲染链（关键）**：LibreOffice headless → PDF → pdfplumber 找页面上的横线规则 → 由规则实测表宽与左右留白 → `center_error_mm = 表格几何中心 − 正文文本框中心`；**PASS ≤ 1.0 mm**（阈值可配置但必须记录）。仅检查属性不算过。

```bash
python scripts/table_qa.py <file.docx> --out <dir>     # 输出 table_qa_report JSON
```

输出字段：`table_width / text_area_width / left_whitespace / right_whitespace / center_error_mm / alignment_property / autofit / grid_widths / paragraph_alignments / vertical_alignments / border 统计 / PASS|FAIL`；多页表逐页统计规则线数。

## 何时不用

- 图件内表格（走 multipanel-compositor）；非三线表模板要求（期刊模板另有规定的从模板）。
