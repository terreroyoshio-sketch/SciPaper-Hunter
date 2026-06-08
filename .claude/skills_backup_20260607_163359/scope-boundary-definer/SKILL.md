---
name: scope-boundary-definer
version: 1.0
language: 中文
description: 研究边界划定 skill，识别论文结论的地理、时间、文化、样本和方法边界，避免不当外推。
---

# Scope Boundary Definer

## Goals
- 识别地理边界（数据收集国家/地区，结论是否可跨文化推广）
- 识别时间边界（数据年份、研究时期、结论时效性）
- 识别文化或制度边界（特定制度环境下的发现）
- 识别样本边界（人口特征、行业、组织类型）
- 识别方法适用边界（实验条件、测量工具的适用范围）
- 区分作者明示边界和 AI 推断边界
- 指出可能失效场景（哪些条件下结论可能不成立）

## Constraints
- 不输出"需要更多研究"这类空话
- 不夸大普适性
- 不编造数据集范围
- 必须明确边界来源（作者明示/方法文本推断/样本特征推断）

## Academic Integrity
- 不得编造样本范围和数据来源
- 不得虚构数据集信息
- 区分"作者声称的边界"和"基于方法文本的推断边界"
- 推断边界必须标注"推断"

## Workflow
1. 接收摘要、Methods、Results 和 Discussion
2. 提取作者明示边界（Limitations/未来研究中的明确陈述）
3. 从方法文本推断隐藏边界（样本特征、实验环境、测量工具）
4. 判断可能失效场景
5. 输出边界条件表

## Output
- scope_boundary_table.csv（含文献编号、边界类型、具体边界、来源、边界类型[明示/推断]、失效场景）
- boundary_condition_report.md
