# Brainstorming & PPT Master — 总说明

## brainstorming
- **来源**: obra/superpowers
- **许可证**: MIT
- **安装路径**: `~/.claude/skills/brainstorming/`
- **用途**: 前期方案发散、结构选择、任务拆解、2-3 套方案比较

## ppt-master
- **来源**: hugohe3/ppt-master
- **许可证**: MIT
- **安装路径**: `~/.claude/skills/ppt-master/`
- **用途**: 从 PDF/DOCX/URL/Markdown 生成真正可编辑的 PPTX

## 适用场景对比

| 工具 | 适合 | 不适合 |
|------|------|--------|
| brainstorming | 前期构思、方案比较 | 直接生成成品 |
| ppt-master | 通用可编辑 PPTX 生成 | 学术论文叙事（用 nature-paper2ppt） |
| nature-paper2ppt | 学术论文→汇报结构 | 通用 PPTX 排版 |
| word-document-processor | Word/DOCX 处理 | PPT 生成 |
| nature-figure | 高质量科研图件 | 普通幻灯片制作 |

## 风险
- ppt-master 可选的 AI 图像生成 API 需用户显式配置，默认不启用
- 不读取凭据、不上传文件、不修改系统配置
