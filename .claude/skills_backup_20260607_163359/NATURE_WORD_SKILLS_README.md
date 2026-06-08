# Nature Figure + Word Document Processor Skills — 总说明

## 新增 Skills

### 1. nature-figure
- **来源**: Yuan1z0825/nature-skills
- **许可证**: MIT
- **安装路径**: `~/.claude/skills/nature-figure/`
- **用途**: 生成符合 Nature 期刊标准的科研图件。支持 Python (matplotlib/seaborn) 和 R (ggplot2/patchwork) 两种 track。
- **核心规则**:
  - 绘图前先定义 figure contract（核心结论、证据链、图型选择）
  - 主输出格式为 SVG（可编辑），辅以 300 dpi PNG
  - 字体使用 Arial / DejaVu Sans
  - 多面板遵循三级信息层次
- **包含**:
  - SKILL.md, README.md
  - 12 个参考文档（api.md, design-theory.md, chart-types.md 等）
  - 10 个图表集参考图、3 个画廊示例图
  - 评估文件

### 2. word-document-processor
- **来源**: qodex-ai/ai-agent-skills
- **许可证**: Proprietary（Anthropic 服务条款）
- **安装路径**: `~/.claude/skills/word-document-processor/`
- **用途**: 全面的 Word 文档处理，支持创建、编辑、格式保留、修订追踪和元数据管理。
- **核心功能**:
  - 文本提取（通过 pandoc 转换 docx → markdown）
  - 从零创建文档（通过 docx-js）
  - 编辑现有文档（通过 Python Document 库）
  - 修订追踪工作流（Redlining）
  - 文档转图片（通过 LibreOffice + poppler）
- **包含**:
  - SKILL.md, ooxml.md, docx-js.md
  - Python OOXML 操作脚本
  - 文档处理库

## 组合调用场景

| 场景 | 核心 Skills | 说明 |
|------|------------|------|
| 论文图件 | nature-figure + reviewer-red-team-auditor | 科研图件生成与审稿人检查 |
| Word 排版 | word-document-processor + terminology-coherence-editor | 按模板排版，统一术语 |
| 综述图文稿 | critical-literature-review-pipeline + nature-figure + word-document-processor | 综述 + 机制图 + Word 输出 |
| 项目申报书 | nsfc-proposal-architecture-pipeline + word-document-processor | 基金申请书结构+Word 成稿 |

详见 `NATURE_WORD_COMBINED_WORKFLOWS.md`。

## 许可证风险

- **nature-figure**: MIT 开源许可证，无使用限制。
- **word-document-processor**: Proprietary 许可证。受 Anthropic 服务条款约束，禁止复制、分发、派生修改。个人使用场景下可正常安装。

## 不适合使用的场景

- nature-figure 不适用于商业仪表盘、Illustrator/Figma 优先的信息图。
- word-document-processor 不适用于需要实时协作编辑的场景（推荐使用 Office 365 在线协作）。
