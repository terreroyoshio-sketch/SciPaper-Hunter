---
name: paperbanana-mcp-wrapper
description: PaperBanana MCP 集成封装。用于通过 MCP 协议调用 PaperBanana 生成学术插图、图形摘要、方法流程图、技术路线图、机制图。需要在 .claude/settings.json 或 claude_code_config.json 中配置 paperbanana MCP 服务器。
---

# PaperBanana MCP Wrapper

## 概述

PaperBanana 是一个基于多智能体（Retriever → Planner → Stylist → Visualizer → Critic）的学术插图生成框架。本 wrapper 通过 MCP（Model Context Protocol）协议桥接 PaperBanana 的生成能力。

## 前置条件

### 1. 安装 paperbanana 包

```bash
pip install paperbanana[mcp]
```

### 2. 配置 MCP 服务器

在 `.claude/settings.json` 或 `claude_code_config.json` 中添加：

```json
{
  "mcpServers": {
    "paperbanana": {
      "command": "uvx",
      "args": ["--from", "paperbanana[mcp]", "paperbanana-mcp"],
      "env": {
        "OPENAI_API_KEY": "your-openai-api-key",
        "GOOGLE_API_KEY": "your-google-api-key"
      }
    }
  }
}
```

> 至少需要设置一个 API Key。Gemini（GOOGLE_API_KEY）可通过 Google AI Studio 免费获取。

### 3. 验证安装

```bash
# 检查 MCP 服务器是否正常运行
paperbanana-mcp --help
```

## MCP 工具列表

| 工具 | 功能 | 适用场景 |
|------|------|---------|
| `generate_diagram` | 从文本+标题生成方法论示意图 | 学术插图、方法流程图 |
| `generate_plot` | 从 JSON 数据生成统计图 | 数据可视化 |
| `continue_run` | 带反馈的迭代优化 | 对生成结果不满意时 |
| `orchestrate_figures` | 全篇论文的图件统筹生成 | 论文多图批量生成 |
| `evaluate_diagram` | 评估图表质量 | 输出质量检查 |
| `batch_diagrams` | 批量生成图表 | 多图同时生成 |

## 调用流程

### 标准流程（推荐）

```
[需求描述]
    ↓
paperbanana-figure-brief-builder  →  将需求转化为结构化 brief
    ↓
PaperBanana MCP generate_diagram  →  生成初稿
    ↓
人工检查 / 或 continue_run 迭代  →  调整优化
    ↓
paperbanana-output-auditor        →  质量审计
    ↓
paperbanana-style-guide-adapter   →  风格适配
    ↓
word-document-processor / ppt-master  →  嵌入文档/PPT
```

### 快速调用（简单场景）

```
直接使用 PaperBanana MCP 的 generate_diagram 工具，
传入 method_text + caption 即可生成。
```

## 适用图件类型

| 类型 | MCP 工具 | 说明 |
|------|---------|------|
| 方法论示意图 | generate_diagram | 最核心的能力，multi-agent pipeline、model architecture |
| 图形摘要 | generate_diagram | 提供全文概要描述 |
| 方法流程图 | generate_diagram | 实验步骤、数据处理流程 |
| 技术路线图 | generate_diagram | 研究方案、技术路线 |
| 机制图 | generate_diagram | 分子机制、信号通路 |
| 统计图 | generate_plot | 柱状图、折线图等 |
| 全篇图件 | orchestrate_figures | 输入论文全文，自动生成所有图表 |

## 使用示例

### 生成方法论示意图

```bash
# 直接通过 MCP 调用，在对话中描述需求
# 示例描述：
# "Method: We propose a multi-modal fusion network consisting of 
#  three branches: visual encoder, text encoder, and cross-modal 
#  attention module. The visual encoder uses ResNet-50 to extract 
#  image features, the text encoder uses BERT for text encoding, 
#  and the cross-modal attention module fuses the two modalities 
#  for final classification."
# Caption: "Figure 1: Overview of the proposed multi-modal fusion network."
```

### 带反馈的迭代优化

```
首次生成后，如果不满意，可以通过 continue_run 
传入具体反馈，例如：
- "Use larger font for axis labels"
- "Change color scheme to blue-green gradient"
- "Add more detailed arrows in the pipeline"
- "Include module labels inside each block"
```

## 注意事项

1. **不编造** — PaperBanana 生成的是 AI 渲染图，不是真实实验数据图
2. **不用于** — 伪造实验结果、篡改数据图
3. **API Key 安全** — API Key 仅用于调用模型 API，不会上传本地论文文件到第三方
4. **首次使用** — 需要下载 PaperBananaBench 参考集，大约需要几分钟
5. **迭代次数** — 默认 3 轮 Critic 优化，可通过参数调整
6. **输出格式** — 默认 PNG 栅格图（非矢量），后续版本可能支持 SVG
