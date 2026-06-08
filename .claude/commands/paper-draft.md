# /paper-draft — 论文初稿生成

## 用途
从已通过核验的材料生成论文初稿。

## 调用流程

1. **加载核验材料**
2. **结构规划**
3. **分节撰写**
4. **引用嵌入**
5. **初稿输出**

## 前置条件（**全部满足才能执行**）

- [ ] `literature_matrix.csv` 已存在
- [ ] `evidence_cards/` 已存在
- [ ] `citation_audit.md` 已通过（无未解决的红旗）
- [ ] `project_plan.md` 已确认
- [ ] 无反造假违规
- [ ] 不得使用 `RECONSTRUCTED_TEST_DATA` 作为正式依据

## 硬性约束

- ❌ 前置条件不满足时必须停止并报告缺失项
- ❌ 不编造数据
- ❌ 不编造结果
- ❌ 不编造统计量
- ❌ 不编造作者和单位
- ❌ 缺失信息标注"需补充"

## 输出

```
outputs/paper-draft/
├── manuscript_v0.md
├── reference_list.md
└── draft_notes.md              # 标注缺失项和不确定性
```

## 依赖 Skills

- academic-paper
- nature-writing-wrapper
- citation-format-syntax-auditor
