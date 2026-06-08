# /check-citations — 引用核查

## 用途
只做引用核查，不润色、不改写正文。检查引用完整性和真实性。

## 调用流程

1. **文献边界锁定** — 调用 literature-boundary-lock 锁定引用范围
2. **引用格式审计** — 调用 citation-format-syntax-auditor 检查格式
3. **一致性检查** — 正文引用 ↔ BibTeX ↔ DOI 三方校验
4. **支撑性检查** — 引用是否支撑所在句子的论点

## 核查清单

| 检查项 | 通过条件 |
|--------|---------|
| 正文引用 ↔ BibTeX | 每个正文引用在 BibTeX 中存在 |
| BibTeX ↔ 正文引用 | 每个 BibTeX 条目至少被引用一次 |
| DOI 真实性 | DOI 可通过 doi.org 解析 |
| 引用支撑论点 | 引用文献的结论支持引用处的声明 |
| UNVERIFIED 标记 | 无未标记的 unverified 引用 |
| Hallucination | 无编造的作者、卷期、页码 |

## 硬性约束

- ❌ 不润色正文
- ❌ 不改写正文
- ❌ 不放过 unverified 引用
- ❌ DOI missing 不得标记为 fully_verified
- ❌ Semantic Scholar 有记录 ≠ 全文已核验
- ❌ abstract_only 必须标明

## 输出

```
reports/citation_audit.md
references/citation_verification.csv
```

## 依赖 Skills

- literature-boundary-lock
- citation-format-syntax-auditor
