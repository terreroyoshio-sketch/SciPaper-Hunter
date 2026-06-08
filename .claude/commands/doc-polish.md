# /doc-polish — 文档润色

## 适用场景
Word、Markdown、项目书、报告、通知、SOP 润色。

## 输入要求
- 文档文件（DOCX / MD / TXT）
- 文档类型
- 目标用途

## 调用模块
`office-productivity-workbench` → `document-polisher`

## 工作流
1. 读取原文
2. 判断文档类型
3. 保留原意
4. 优化逻辑顺序
5. 统一术语
6. 统一语气
7. 删除重复和空话
8. 输出修改版和修改说明

## 输出文件
```
outputs/document_polishing/
├── polished_document.md
├── revision_notes.md
├── terminology_check.md
└── risk_changes.md
```

## 禁止事项
- 不改变事实
- 不替换专有名词
- 不扩大结论
- 不把未证实内容写成确定结论
- 不添加 AI 味模板句

## 验收标准
- [ ] 所有修改保持原意
- [ ] 专有名词未被替换
- [ ] 修改说明已生成
- [ ] 夸张表达已删除
