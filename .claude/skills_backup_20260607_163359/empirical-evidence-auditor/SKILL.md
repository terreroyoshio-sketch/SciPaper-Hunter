---
name: empirical-evidence-auditor
version: 1.0
language: 中文
description: 实证证据审查 skill，从论文结果中提取核心假设判定、统计显著性、效应量和关键证据，输出假设判决表。
---

# Empirical Evidence Auditor

## Goals
- 判定假设支持情况：支持、部分支持、拒绝、未检验
- 提取最关键统计系数或质性主题
- 标注 p 值、置信区间或显著性水平
- 标注效应量
- 对缺失报告进行标注

## Constraints
- 仅聚焦核心假设（论文明确提出的 H1/H2 等）
- 不夸大显著性（p<0.05 ≠ 效应大）
- 不编造效应量
- 作者未报告效应量时标注"效应量缺失"
- 不把补充性发现当核心证据
- 区分统计显著性和实际显著性

## Academic Integrity
- 不得编造统计数值
- 不得编造显著性水平
- 不得编造效应量
- 只记录文献中明确报告的结果
- 数值模糊时标注"精确值未报告"

## Workflow
1. 接收 Results 章节
2. 提取假设（H1, H2, H3...）
3. 匹配结果（逐假设匹配检验结果）
4. 判断支持状态（基于统计显著性和方向一致性）
5. 提取 Top 3 最强证据
6. 输出假设判决表

## Output
- hypothesis_verdict_table.csv（含文献编号、假设、预测方向、统计值、p 值、效应量、支持状态、证据强度、缺失标注）
- top_evidence_report.md
