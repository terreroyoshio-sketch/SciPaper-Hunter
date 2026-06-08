# 引用政策 — Citation Policy

## 核心原则
每个引用必须可追踪、可验证、可回溯。引用必须真实支撑所在句子。

---

## 规则列表

### C1. 所有引用元数据可追踪
- 作者、年份、题目、期刊、DOI 必须完整
- DOI unmber 不得标记为 fully_verified

### C2. 核验等级
| 等级 | 定义 | 标记 |
|------|------|------|
| abstract_only | 仅摘要可见 | [ABSTRACT ONLY] |
| full_text_verified | 全文已核验 | [FULL TEXT] |
| doi_verified | DOI 可解析 | [DOI VERIFIED] |
| unverified | 未核验 | [UNVERIFIED] |

### C3. Semantic Scholar ≠ 全文已核验
- Semantic Scholar 有记录仅表示 metadata 存在
- 不等于全文已核验
- 不等于引用内容正确

### C4. 引用必须支撑所在句子
- 引用 A 不能支撑结论 B
- 引用文献的结论必须与引用处声明一致
- 不得将综述中的二手引用当作一手引用

### C5. 禁止行为
- ❌ 编造作者
- ❌ 编造 DOI
- ❌ 编造卷期页码
- ❌ 用引用 A 支撑结论 B
- ❌ 将 abstract_only 标记为 fully_verified
- ❌ 编造研究方法和样本量

---

## 审计

每次输出时检查：
- [ ] 每个引用都有 DOI
- [ ] 每个引用都在 BibTeX 中
- [ ] BibTeX 没有未使用的条目
- [ ] 引用与论点对应
- [ ] 无 UNVERIFIED 混入正文
