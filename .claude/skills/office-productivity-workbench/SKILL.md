# Office Productivity Workbench — 办公学习效率 Skill 工作台

## 用途

帮助用户处理学习、办公、汇报、调研、文档、表格、PPT、图像和自动化提醒任务。不替用户做最终判断，而是把资料整理、结构搭建、格式检查和初稿生成标准化。

## 适用任务

1. **网页调研** — 提取网页内容、来源整理、截图归档
2. **PDF 研报和论文阅读** — 结构摘要、重点页定位
3. **Excel 表格分析** — 清洗、统计、趋势和异常检查
4. **选题和汇报角度研究** — 多角度评估、材料支撑分析
5. **Word 文档润色** — 保留原意的语言和结构优化
6. **信息图和配图提示词生成** — 图像方案和排版建议
7. **PPT 大纲和页面结构** — 故事线、讲稿、视觉建议
8. **通知、邮件、文案初稿** — 受众导向的起草
9. **个人或项目品牌风格统一** — 字体、颜色、版式规则
10. **周期性提醒和复盘清单设计** — 任务方案、不自动执行

## 不适用任务

1. 法律合同最终判断
2. 财务审计最终结论
3. 医疗诊断建议
4. 投稿前最终学术核验
5. 自动发布内容
6. 自动发送邮件
7. 自动删除文件
8. 伪造数据、伪造截图、伪造引用
9. 未经确认修改正式文件
10. 代替用户做商业决策

## 核心原则

1. AI 负责整理、提炼、起草和检查
2. 用户负责最终判断
3. 重要网页必须截图或保存来源
4. 重要 PDF 必须标注页码
5. 重要表格分析必须保留原始数据
6. 文档润色不能改变原意
7. PPT 先搭结构，再做视觉
8. 图像生成要避免 AI 味和虚假细节
9. 自动化任务只生成方案，不擅自启用
10. 任何任务都要留下输入、输出和风险记录

## 模块索引

| 模块 | 用途 | 命令 |
|------|------|------|
| web-extract | 网页提取和调研整理 | `/web-extract` |
| pdf-toolkit | PDF 论文、研报、合同初读 | `/pdf-read` |
| spreadsheet-analysis | 表格清洗、统计、趋势分析 | `/sheet-analyze` |
| topic-research | 选题、汇报角度、分享主题 | `/topic-research` |
| document-polisher | 文档润色、术语统一 | `/doc-polish` |
| imagegen-helper | 配图、信息图、流程图方案 | `/image-brief` |
| presentation-builder | PPT 大纲、讲稿、答辩逻辑 | `/ppt-build` |
| content-writer | 通知、邮件、文案初稿 | `/content-draft` |
| brand-style-kit | 个人/项目视觉风格统一 | `/brand-style` |
| automation-assistant | 提醒、复盘、排期方案 | `/automation-plan` |

## 已有 Skill 引用

本工作台引用以下已在环境中验证的 skills（非依赖，可选）：
- `research-idea-conflict-miner` — 科研选题场景
- `ai-powerpoint-research-workflow` — 科研 PPT 场景
- `academic-paper` — 论文写作场景

## 目录结构

```
skills/office-productivity-workbench/
├── SKILL.md               # 本文件
├── README.md              # 快速入门
├── templates/             # 10 个模块模板 + 最终检查清单
├── references/            # 8 个规则参考
└── scripts/               # 6 个工具脚本
```
