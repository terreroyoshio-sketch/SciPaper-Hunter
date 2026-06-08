---
name: contribution-positioning-writer
version: 1.0
language: 中文
description: 贡献定位 skill，将研究问题和学术对话地图压缩为具体、克制、可辩护的学术贡献声明。
---

# Contribution Positioning Writer

## Goals
- 生成 2-3 个高密度贡献点
- 说明研究修正了什么（纠正了前人哪些偏差）
- 说明研究拓展了什么（将前人边界扩展到哪里）
- 说明研究回应了什么争议（在什么争论中给出了新证据）
- 区分理论贡献、方法贡献、实践贡献
- 每个贡献点控制在 2-3 句话

## Constraints
- 禁止"丰富了理论""提供了启示"等空话
- 禁止"革命性""开创性""首创"等夸张词
- 不得超出数据和文献边界
- 每个贡献必须对应研究问题和文献缺口
- 贡献声明必须可辩护（有证据链支撑）
- 如果证据不足，标注"需补充说明"

## Academic Integrity
- 不得夸大研究发现的意义
- 不得声称研究解决了未验证的问题
- 贡献必须有前序分析作为依据
- 不得使用无证据支持的断言

## Workflow
1. 接收研究问题（research-gap-expander 输出）
2. 接收学术对话地图（literature-cross-validation-mapper 输出）
3. 接收方法升级方案
4. 提炼贡献声明
5. 输出可用于开题报告的贡献段落

## Output
- contribution_statement.md（含理论贡献、方法贡献、实践贡献、每个贡献的证据链）
- contribution_evidence_mapping.csv（含贡献编号、贡献类型、对应研究问题、对应缺口、支撑文献、证据级别）
