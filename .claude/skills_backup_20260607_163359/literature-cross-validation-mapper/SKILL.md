---
name: literature-cross-validation-mapper
version: 1.0
language: 中文
description: 文献交叉验证 skill，比对多篇论文的发现，构建支持、对立、扩展和无关的学术对话网络。
---

# Literature Cross Validation Mapper

## Goals
- 识别论文之间的支持关系（A 的结果被 B 复现或支持）
- 识别论文之间的冲突关系（A 与 B 的发现矛盾）
- 识别论文对经典模型的拓展
- 构建学术对话网络（谁支持谁、谁反对谁、谁发展了谁）
- 输出争议点和共识点

## Constraints
- 禁止孤立评价单篇论文，必须置于文献群关系中
- 不编造经典研究
- 不强行制造冲突
- 关系必须有文献证据
- 区分"直接冲突"和"表面矛盾"（方法不同导致的差异）
- 区分"明确支持"和"间接一致"（主题相似但方法不同）

## Academic Integrity
- 不得编造论文之间的引用或对话关系
- 关系判断必须基于文献中的明确陈述或逻辑推断
- 推断关系必须标注"推断"
- 文献中没有对比的信息不得写入

## Workflow
1. 接收多篇论文的引言和 Discussion
2. 提取每篇论文的核心发现
3. 匹配理论或方法线索
4. 判断关系类型：支持、对立、扩展、无关
5. 构建学术对话网络

## Output
- literature_dialogue_map.md（含争议表、共识表、未解决疑问表）
- literature_relation_network.csv（含论文 A、论文 B、关系类型、证据文本、置信度）
