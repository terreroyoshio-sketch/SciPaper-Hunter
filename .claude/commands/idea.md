# /idea — 科研选题孵化

## 用途
启动 research-idea-conflict-miner，从文献冲突中生成可验证研究假设。

## 调用流程

1. **场域压缩** — 明确研究领域、子领域、可用数据、时间窗口
2. **材料整理** — 列出已有文献、预实验数据、可获取资源
3. **证据矩阵** — 拆解已有文献的研究对象、样本量、变量、结局、方法、结论
4. **冲突识别** — 标记矛盾结论、方法论分歧、证据缺口
5. **假设翻译** — 将冲突转化为可检验假设
6. **约束审查** — 检查数据可得性、伦理、时间、资源制约

## 硬性约束

- ❌ 不凭空生成题目
- ❌ 不编造文献
- ❌ 不编造 DOI
- ❌ 不虚构数据
- ❌ 不虚构研究可行性

## 前置条件

- [ ] 用户已提供研究领域或具体问题
- [ ] 用户已说明可用数据或资源
- [ ] 低于 B 类证据不进入审稿攻击

## 输出

```
outputs/idea/
├── evidence_matrix.csv
├── conflict_map.md
├── hypothesis_candidates.md
├── feasibility_check.md
└── constraint_report.md
```

## 依赖 Skills

- research-idea-conflict-miner
