# Anti-Fabrication Rules

**文件:** `references/anti_fabrication_rules.md`
**用途:** 防止 AI 编造文献、DOI、数据和结果。

---

## 核心原则

1. **所有引用必须有真实来源。** 不得使用模型记忆中的"可能存在"的论文。
2. **无法核验的信息必须标注。** 使用以下标签：
   - `[UNVERIFIED]` — 信息未通过外部源核验
   - `[HALLUCINATION_RISK]` — AI 可能编造的内容
   - `[NEEDS_HUMAN_CHECK]` — 需要人工核验
3. **不得填补缺失信息。** 如果检索不到 DOI、页码、卷号，写 `missing` 而不是编造。
4. **不得 "promote" 预印本为已发表。** 除非确认了发表 venue。
5. **下载到 PDF = 已阅读。** 没有下载到 PDF 不能说已精读。

## 引用核查流程

```
对于每个引用:
  1. 从 BibTeX 提取 DOI / arXiv ID / Title
  2. 通过 Semantic Scholar API 核验存在性
  3. 通过 CrossRef API 核验 DOI
  4. 人工抽样核验 (≥20%)
  5. 标注 VERIFIED / NOT_FOUND / MISMATCH
```

## 高风险模式识别

当检测到以下模式时，必须标记为 `[HALLUCINATION_RISK]`:
- 引用出现在没有检索操作的生成中
- DOI 格式正确但检索不到
- 作者、年份、题名不匹配
- 引用结论与该领域共识明显矛盾
- 统计数字没有来源

## ARS 引用锚点格式

参考 ARS 的 3 层引用锚点:
```markdown
<!--ref:key2024-->
<!--loc:kind=quote,text="exact quote from paper"-->
```
