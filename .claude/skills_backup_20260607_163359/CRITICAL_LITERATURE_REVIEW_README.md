# 批判性文献综述闭环流水线 Skills — 总说明

## 一、背景

本组 skills 的核心目标：让 Claude Code 在写 SCI 综述、学位论文综述、国自然基金国内外研究现状、项目申报书研究背景时，**严格避免文献幻觉**，并通过主题聚类、国内外研究范式对比、学术争议梳理、方法论局限性分析、漏斗式逻辑排序和研究空白界定，**生成严谨、批判性、可追溯的文献综述**。

**核心禁止**：
- 严禁 AI 凭内部记忆写文献综述。
- 严禁虚构作者、年份、题名、DOI、期刊、卷期页码。
- 所有综述内容必须来自用户提供的人工核实文献文本。

---

## 二、新增 Skills 清单

| 序号 | 文件夹名称 | 用途 | 输入 | 输出 |
|------|-----------|------|------|------|
| 1 | `literature-boundary-lock` | 文献边界锁定，禁止幻觉 | 已核实文献题录/摘要 | 边界确认 + 可用文献清单 |
| 2 | `literature-theme-clustering` | 主题聚类，消除流水账 | 无序文献摘要 | 主题聚类表 + 综合段落 |
| 3 | `domestic-international-paradigm-comparator` | 国内外研究范式客观对比 | 国内+国际文献分组 | 范式对比 + 协同空白 |
| 4 | `academic-disagreement-mapper` | 学术分歧映射 | 文献摘要 + 结果 | 争议点 + 对比段落 |
| 5 | `methodological-limitation-synthesizer` | 方法论局限性综合 | 方法/局限部分 | 共性局限 + 批判段落 |
| 6 | `paragraph-logic-bridge` | 段落逻辑桥接 | 段落 A + B | 桥接句 + 关系说明 |
| 7 | `funnel-logic-sorter` | 漏斗逻辑排序 | 未排序段落 | 宏观→微观有序文本 |
| 8 | `objectivity-calibration-auditor` | 客观性校准 | 原始摘要 + 评价段落 | 校准后版本 + 风险 |
| 9 | `research-gap-definer` | 研究空白界定 | 综述初稿 + 局限 | 空白段落 + 目标桥接 |
| 10 | `citation-format-syntax-auditor` | 引文句法与格式规范 | 综述草稿 | 优化后文本 + 问题清单 |
| 11 | `critical-literature-review-pipeline` | 完整闭环流水线 | 完整文献库 | 完整综述初稿 |

---

## 三、流水线调用流程

调用 `critical-literature-review-pipeline` 时，自动依次执行：

```
Step  1: literature-boundary-lock              → 锁定数据边界
Step  2: literature-theme-clustering           → 主题聚类
Step  3: domestic-international-paradigm-comparator → 国内外范式对比
Step  4: academic-disagreement-mapper           → 学术争议
Step  5: methodological-limitation-synthesizer  → 方法局限
Step  6: funnel-logic-sorter                    → 漏斗排序
Step  7: paragraph-logic-bridge                 → 段落桥接
Step  8: objectivity-calibration-auditor        → 客观性校准
Step  9: research-gap-definer                   → 研究空白
Step 10: citation-format-syntax-auditor         → 引文校对
```

---

## 四、为什么必须先锁定数据边界

因为 AI 模型在无约束条件下会：
1. **编造不存在的文献** — 生成看起来真实但实际不存在的作者、标题、期刊和 DOI。
2. **编造不存在的 DOI** — 使用真实期刊名但搭配不存在的卷期页码。
3. **混淆研究结论** — 把文献 A 的结论错误地归到文献 B 上。
4. **错误归因** — 把不同机构的研究者拼凑成不存在的合作者。

`literature-boundary-lock` 通过以下机制防止：只允许使用用户提供的已核实文本，对缺失信息标注"未提供"。

---

## 五、为什么不能让 AI 直接"写某主题文献综述"

直接要求 AI"写一篇关于 X 的文献综述"会触发以下风险：

| 风险 | 后果 |
|------|------|
| 虚构引用 | 生成的文献不存在，但看起来真实 |
| 数据混淆 | 不同文献的结果被错误关联 |
| 遗漏关键文献 | AI 根据训练数据生成，可能遗漏领域重要工作 |
| 时间错误 | 把早期工作归到后期，或反之 |

**正确做法**：
1. 先用 `keyword-literature-download` 检索真实文献。
2. 或人工收集已核实的 PDF/题录。
3. 再使用本组 skills 进行基于已核实文献的综述写作。

---

## 六、如何避免虚构作者、DOI、期刊和年份

1. 使用 `literature-boundary-lock` 作为第一步。
2. 所有文献必须有题录或摘要来源。
3. 标记缺失信息，不自行补写。
4. 使用 `critical-literature-review-pipeline` 确保每个环节被审计。
5. 最终人工核查所有引用。

---

## 七、如何避免流水账综述

流水账 = "作者 A 说 X，作者 B 说 Y，作者 C 说 Z"。

改用 `literature-theme-clustering`：
- 按主题分组，不是按作者或时间。
- 每个主题句由多位作者共同支撑。
- 引文放在论断末尾的括号中，而不是句子开头。

---

## 八、如何写出批判性综述

批判性综述 ≠ 贬低前人。

使用以下组合：
1. `academic-disagreement-mapper` — 提取争议，而非掩盖矛盾。
2. `methodological-limitation-synthesizer` — 综合共性局限，而非逐篇批评。
3. `objectivity-calibration-auditor` — 校准评价，防止过度贬低。
4. `research-gap-definer` — 从争议和局限中自然推出空白。

---

## 九、与已有 Skills 的组合方式

详见 `CRITICAL_LITERATURE_REVIEW_WORKFLOWS.md`。

---

## 十、安全性说明

1. 所有 skills 均为本地 SKILL.md 文件，不执行代码。
2. 不连接外部网络或 API。
3. 不修改系统级配置。
4. 原始 skills 已在安装前备份。
