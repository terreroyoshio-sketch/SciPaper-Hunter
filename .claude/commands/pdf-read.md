# /pdf-read — PDF 阅读与结构摘要

## 适用场景
PDF 论文、研报、合同、说明书的初读。

## 输入要求
- PDF 文件路径或 URL

## 调用模块
`office-productivity-workbench` → `pdf-toolkit`

## 工作流
1. 提取目录
2. 判断文档类型
3. 生成结构摘要
4. 标注重点页码
5. 提取关键表格和图
6. 提取结论和限制
7. 标注必须人工精读的页码

## 输出文件
```
outputs/pdf_reading/
├── pdf_structure.md
├── key_pages.md
├── extracted_tables/
└── risk_pages.md
```

## 禁止事项
- 不把摘要当完整理解
- 合同、金额、责任条款不能只看摘要
- 引用 PDF 内容必须保留页码
- 扫描版 PDF 需 OCR

## 验收标准
- [ ] 文档类型已判断
- [ ] 重点页已标注
- [ ] 合同关键条款已提醒人工复核
- [ ] 所有引用标注了页码
