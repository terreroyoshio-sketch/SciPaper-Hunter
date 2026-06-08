# Office Productivity Workbench — 快速入门

## 这是什么

一个办公学习效率 Skill 工作台，把网页调研、PDF 阅读、表格分析、选题研究、文档润色、图像生成、PPT 构建、内容写作、品牌风格、自动化提醒标准化为 10 个可复用模块。

## 使用方式

```bash
# 查看命令列表
ls .claude/commands/
```

在 Claude Code 会话中使用：
- `/web-extract` — 网页调研
- `/pdf-read` — PDF 阅读
- `/sheet-analyze` — 表格分析
- `/topic-research` — 选题研究
- `/doc-polish` — 文档润色
- `/image-brief` — 图像提示词
- `/ppt-build` — PPT 构建
- `/content-draft` — 内容写作
- `/brand-style` — 品牌风格
- `/automation-plan` — 自动化方案

## 创建新项目

```bash
python .claude/skills/office-productivity-workbench/scripts/make_office_project.py --name 项目名称
```

## 核心原则

1. 用户负责最终判断
2. AI 负责整理、起草和检查
3. 所有信息保留来源
4. 不自动执行破坏性操作
5. 每个任务要留审计记录

## 依赖

| 工具 | 用途 | 状态 |
|------|------|------|
| Python 3 | 脚本运行 | ✅ 已安装 |
| python-docx | DOCX 处理 | ✅ 已安装 |
| openpyxl | XLSX 处理 | ✅ 已安装 |
| python-pptx | PPTX 处理 | ✅ 已安装 |
| Pandoc | 文档转换 | ✅ 已安装 |
| WPS Office | 排版导出 | ✅ 已安装 |
| MS Office | 可选 | ✅ 已安装 |
| Visio | 流程图 | ✅ 已安装 |
