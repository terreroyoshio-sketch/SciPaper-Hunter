# OpenScholar-Style Literature QA Rules

**文件:** `references/openscholar_style_rules.md`
**用途:** 借鉴 OpenScholar 的检索增强和引用核验思想，建立本地文献问答规则。

---

## 核心原则

1. **回答任何文献问题前先检索** — 不依赖模型记忆
2. **每个结论必须有 citation** — 每个 claim 追到来源
3. **引用必须来自检索结果** — 不可来自模型训练数据中的"记忆"
4. **对不确定结论标注 uncertainty**
5. **对争议性结论列出不同观点**
6. **对综述类问题输出 evidence map**
7. **不要把摘要当作全文证据** — 摘要可能和正文不一致
8. **优先使用原文来源**

## 检索优先级

```
原文 PDF (已下载) > DOI 出版社页面 > PubMed > arXiv > Semantic Scholar > Crossref
```

## Evidence Map 格式

对于综述类问题，输出 evidence map:

```
问题: {research question}

证据 1: {作者年份}
  支持论点: {论点}
  证据强度: {强/中/弱}
  一致性: {与证据2一致/冲突}

证据 2: {作者年份}
  支持论点: {论点}
  证据强度: {强/中/弱}
  一致性: {与证据1一致/冲突}

总体评估: {结论}
不确定性: {剩余不确定的问题}
```

## 引用核验流程（OpenScholar 风格）

```
1. arXiv ID 检查 → 是否在 arXiv 中存在
2. CrossRef/DataCite DOI 检查 → DOI 是否可解析
3. Semantic Scholar 题名匹配 → 题名、作者、年份是否一致
4. LLM 相关性评分 → 该引用是否真正支持论点
```

## 四类输出标记

| 标记 | 含义 |
|------|------|
| ✅ VERIFIED | 通过至少 2 层核验 |
| ⚠️ PARTIAL | 部分核验通过 |
| ❓ UNCERTAIN | 未能充分核验 |
| 🔴 CONFLICT | 与检索结果矛盾 |
