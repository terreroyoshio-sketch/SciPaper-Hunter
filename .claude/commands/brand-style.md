# /brand-style — 品牌风格统一

## 适用场景
个人、项目、课程、答辩、报告的视觉和文字风格统一。

## 输入要求
- 已有文档、PPT、图片样例

## 调用模块
`office-productivity-workbench` → `brand-style-kit`

## 工作流
1. 收集已有材料
2. 提取常用字体、颜色、版式
3. 生成风格手册
4. 生成封面、表格、标题、页脚规则
5. 生成 PPT 和 Word 样式建议
6. 输出可复用模板说明

## 输出文件
```
outputs/brand_style/
├── style_guide.md
├── color_palette.md
├── font_rules.md
├── table_rules.md
├── ppt_rules.md
└── document_rules.md
```

## 默认规则
- 中文正文宋体小四
- 英文和公式 Times New Roman
- 表格只加粗表头
- 页脚只保留页码
- 不用深蓝底表头

## 禁止事项
- 不使用复杂装饰
- 不随意替换已有品牌色

## 验收标准
- [ ] 配色方案已输出
- [ ] 字体规则已输出
- [ ] 表格/PPT/文档规则已输出
