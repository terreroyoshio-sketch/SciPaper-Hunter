# /review-lit — 文献综述生成

## 用途
调用文献综述流水线，从检索到结构化综述，分阶段输出。

## 调用流程

1. **文献检索** — 使用 deep-research / my-academic-research-master 检索文献
2. **边界锁定** — 使用 literature-boundary-lock 锁定分析范围
3. **矩阵构建** — 拆解文献为证据矩阵
4. **批判性综述** — 使用 critical-literature-review-pipeline 生成综述
5. **引用核验** — 使用 citation-format-syntax-auditor 核查引用

## 硬性约束

- ❌ 不直接写完整综述正文
- ❌ 不跳过文献检索步骤
- ❌ 不编造文献
- ❌ 不编造 DOI
- ❌ abstract_only 不得标记为 full_text_verified

## 必须先输出

```
outputs/review-lit/
├── search_log.md                    # 检索策略与结果
├── raw_candidates.csv               # 初始候选文献
├── literature_matrix.csv           # 证据矩阵
├── evidence_cards/                  # 文献卡片
│   ├── card_001.md
│   └── ...
├── taxonomy.md                      # 主题分类
└── boundary_report.md              # 边界锁定报告
```

## 依赖 Skills

- my-academic-research-master
- deep-research
- critical-literature-review-pipeline
- literature-boundary-lock
- citation-format-syntax-auditor
