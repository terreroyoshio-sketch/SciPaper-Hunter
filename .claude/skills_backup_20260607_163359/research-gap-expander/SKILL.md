---
name: research-gap-expander
version: 1.0
language: 中文
description: 研究缺口裂变 skill，基于方法论漏洞和研究边界生成可测试、可操作的研究问题。
---

# Research Gap Expander

## Goals
- 基于方法漏洞生成研究问题
- 基于边界缺口生成研究问题
- 每个问题对应一个明确缺口
- 为每个问题提供方法升级方案
- 方法升级具体到：数据来源、模型、识别策略、实验设计
- 标注每个问题的可行性和风险

## Constraints
- 不生成纯理论空想
- 不生成无法验证或无法操作的问题
- 不使用"首次研究"作为核心创新
- 不脱离文献证据
- 不编造数据可得性
- 每个问题必须能追溯到一个具体缺口（方法漏洞 or 边界缺口）
- 区分"值得做"和"能做得动"的问题

## Academic Integrity
- 不得凭空制造研究缺口
- 缺口必须有前序分析作为依据
- 不得声称数据可得性而不验证
- 不得使用"首次"作为创新理由

## Workflow
1. 接收方法论攻击清单（methodological-weakness-attacker 输出）
2. 接收边界条件汇总（scope-boundary-definer 输出）
3. 生成 3-5 个候选研究问题
4. 为每个问题给出方法升级方案
5. 标注可行性和风险
6. 输出候选问题清单

## Output
- research_gap_candidates.md（含每个问题的缺口来源、研究问题、方法升级、预期贡献）
- research_question_feasibility_table.csv（含问题编号、数据可得性、技术难度、时间成本、失败风险、综合评级）
