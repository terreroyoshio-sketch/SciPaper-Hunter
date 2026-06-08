# Citation Verification Rules

**文件:** `references/citation_verification_rules.md`
**用途:** 确保所有引用可核验、匹配正文论点。

---

## 10 项必查清单

1. **BibTeX 存在性** — 项目是否有 references.bib 文件
2. **正文引用匹配** — 每个 `\cite{key}` 是否都在 .bib 中
3. **BibTeX 条目使用** — 每个 .bib 条目是否被正文引用
4. **DOI 真实性** — DOI 能否通过 CrossRef/Semantic Scholar API 核验
5. **元数据一致性** — 标题、作者、年份、期刊是否一致
6. **AI 编造文献检查** — 是否存在模型幻觉引用
7. **引用-论点匹配** — 引用是否真正支持所在句子
8. **"引用 A 论证 B"** — 是否引用了文献 A 但论证的是 B 的内容
9. **数据来源** — 统计数字是否有可追溯的来源
10. **过度结论** — 是否做出了引用不足以支持的强结论

## 核验结果标记

| 标记 | 含义 |
|------|------|
| ✅ VERIFIED | 通过 API 核验，信息一致 |
| ❓ NOT_FOUND | 未在数据库中检索到 |
| ⚠️ MISMATCH | 元数据不一致（年份/作者/题名） |
| 🔴 NEEDS_HUMAN_CHECK | AI 无法判断，需要人工核验 |
| 🗑️ REMOVAL_SUGGESTED | 建议删除（编造或无法核验） |

## 引用覆盖率要求

- 文献闸门前: ≥80% 引用已核验
- 最终稿前: 100% 引用至少通过一次 API 核验
- 0 条编造引用
- 0 条编造 DOI
