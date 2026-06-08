# /format-doc — 文档排版与导出

## 用途
处理 Word、PDF、LaTeX、Markdown、WPS、LibreOffice 导出。

## 格式要求

### 中文正文
- 字体：宋体（小四，12pt）
- 行距：1.5 倍
- 段落：首行缩进 2 字符

### 英文正文
- 字体：Times New Roman（12pt）
- 行距：1.5 倍
- 段落：段间距 0pt

### 公式
- 字体：Times New Roman 或 LaTeX 标准数学字体（italic）
- 编号：右对齐，括号包裹

### 表格
- 表头：仅加粗，不用深蓝底色
- 表身：宋体/Times New Roman（10pt）
- 线框：简单三线表
- 配色：不使用过度彩色

### 图片
- 格式：优先高清输出
- 流程图：优先 SVG、draw.io、Visio 可编辑格式
- 分辨率：不低于 300 dpi（论文）/ 150 dpi（PPT）

### 页眉页脚
- 页脚：只保留页码
- 页眉：按目标期刊/学校模板

## 导出方式

| 源格式 | 目标格式 | 工具 |
|--------|---------|------|
| Markdown | DOCX | pandoc / WPS |
| Markdown | PDF | pandoc (xelatex) / WPS |
| Markdown | LaTeX | pandoc |
| LaTeX | PDF | xelatex / pdflatex |
| DOCX | PDF | WPS Writer (`wps.exe`) |
| PPTX | PDF | WPS Presentation (`wpp.exe`) |

## WPS 路径

```
C:\Users\张涵\AppData\Local\Kingsoft\WPS Office\12.1.0.26375\office6\
├── wps.exe    # Writer (DOCX ↔ PDF)
├── wpp.exe    # Presentation (PPTX)
└── et.exe     # Spreadsheet (XLSX)
```

## 硬性约束

- ❌ 不改变原始数据趋势
- ❌ 不虚构图表数据
- ❌ 不覆盖未备份的源文件
