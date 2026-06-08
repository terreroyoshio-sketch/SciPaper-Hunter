# 文献综述闭环写作 Skills — 总说明

## 一、背景

本组 skills 的核心目标：让 Claude Code 在写文献综述、SCI 综述、大论文综述、基金标书研究现状、项目申报书研究背景时，**严格基于已核实文献**，按照"数据边界锁定—主题聚类—争议与局限—漏斗结构—研究缺口—引文校对"的流程生成严谨综述。

**核心禁止：禁止 AI 根据内部记忆生成文献、作者、DOI、期刊名。**

---

## 二、新增 Skills 清单

| 序号 | 文件夹名称 | 用途 | 输入 | 输出 |
|------|-----------|------|------|------|
| 1 | `literature-boundary-lock` | 锁定数据环境，禁止虚构文献 | 已核实文献题录/摘要 | 数据边界确认 + 可用文献清单 |
| 2 | `literature-theme-synthesis` | 流水账→主题综合 | 20-30篇文献摘要 | 主题聚类 + 综合段落 |
| 3 | `theoretical-evolution-mapper` | 理论/技术演进映射 | 按时间排序的文献 | 演进段落 + 时间线 |
| 4 | `academic-debate-mapper` | 学术争论提取 | 文献摘要和结果 | 争议点 + 对比段落 |
| 5 | `methodological-limitation-auditor` | 方法论共性缺陷综合 | 方法/局限部分 | 批判性综合段落 |
| 6 | `conceptual-framework-builder` | 概念框架构建 | 变量描述 + 结果 | 框架蓝图 + 支撑文献 |
| 7 | `funnel-logic-organizer` | 漏斗结构排序 | 已综合主题段落 | 宏观→微观有序综述 |
| 8 | `citation-bridge-writer` | 段落衔接桥接 | 段落A + 段落B | 逻辑桥接句 |
| 9 | `research-gap-synthesizer` | 研究缺口提炼 | 综述初稿 + 争议 + 局限 | 高密度研究缺口段落 |
| 10 | `citation-syntax-auditor` | 引文句法校对 | 综述草稿 | 优化后文本 |
| 11 | `literature-review-closed-loop-pipeline` | 10步闭环流水线 | 完整文献库 | 完整综述初稿 |

---

## 三、闭环流水线调用流程

调用 `literature-review-closed-loop-pipeline` 时，自动依次执行：

```
Step  1: literature-boundary-lock        → 锁定数据边界
Step  2: literature-theme-synthesis      → 主题聚类
Step  3: theoretical-evolution-mapper    → 理论演进
Step  4: academic-debate-mapper          → 学术争论
Step  5: methodological-limitation-auditor → 方法局限
Step  6: conceptual-framework-builder    → 概念框架
Step  7: funnel-logic-organizer          → 漏斗结构
Step  8: citation-bridge-writer          → 段落桥接
Step  9: research-gap-synthesizer        → 研究缺口
Step 10: citation-syntax-auditor         → 引文校对
```

---

## 四、为什么必须先锁定数据边界

因为 AI 模型（包括 Claude 和 ChatGPT）在无约束条件下会：

1. **编造不存在的文献** — 生成看起来真实但实际不存在的作者、标题、期刊和 DOI。
2. **编造不存在的 DOI** — 使用真实期刊名但搭配不存在的卷期页码。
3. **编造不存在的作者** — 把不同机构的研究者拼凑成不存在的合作者。
4. **混淆研究结论** — 把文献 A 的结论错误地归到文献 B 上。

`literature-boundary-lock` 通过以下机制防止这些问题：
- 只允许使用用户提供的已核实文本
- 对缺失信息必须标注"未提供"
- 严格使用原文中的作者和年份格式
- 明确声明不能使用外部记忆

---

## 五、为什么不能让 AI 直接"写某主题文献综述"

直接要求 AI"写一篇关于 X 的文献综述"会触发以下风险：

| 风险 | 后果 |
|------|------|
| 虚构引用 | 生成的文献不存在，但看起来真实 |
| 数据混淆 | 不同文献的结果被错误关联 |
| 遗漏关键文献 | AI 根据训练数据生成，可能遗漏领域重要工作 |
| 时间错误 | 把早期工作归到后期，或反之 |
| 结论错误 | 把不存在的结论写为"研究表明" |

**正确的做法**：
1. 先用 `keyword-literature-download` 检索并下载真实文献。
2. 或人工收集已核实的 PDF/题录。
3. 再使用本组 skills 进行基于已核实文献的综述写作。

---

## 六、如何避免虚构作者、DOI、期刊和年份

1. **使用 literature-boundary-lock 作为第一步** — 锁定数据边界。
2. **使用已核实文献清单** — 所有文献必须有题录或摘要来源。
3. **标记缺失信息** — 如果缺少 DOI，标注"未提供"，不能自造。
4. **使用 literature-review-closed-loop-pipeline** — 10 步闭环确保每个环节都被审计。
5. **使用 citation-syntax-auditor 做最终校对** — 检查引文句法，但不新增引用。
6. **最终人工核查** — 所有引用都需要人工对照原文验证。

---

## 七、与已有 Skills 的组合方式

### A. 做严谨文献综述时

```
1. using-superpowers           → 明确综述目标、学科范围、目标期刊、字数、引文格式
2. keyword-literature-download → 检索并下载相关论文，生成题录库
3. markitdown                  → 将 PDF/Word/网页转为 Markdown
4. literature-boundary-lock    → 锁定已核实文献数据边界
5. literature-review-closed-loop-pipeline → 完整闭环流水线
6. citation-syntax-auditor     → 最终校正引文句法
```

### B. 做 SCI 综述型论文时

```
1. brainstorming                → 生成综述角度和主题结构
2. keyword-literature-download  → 构建核心文献库
3. literature-theme-synthesis   → 按主题聚类文献
4. theoretical-evolution-mapper → 写理论/技术演进
5. academic-debate-mapper       → 写学术争议
6. methodological-limitation-auditor → 写方法局限
7. research-gap-synthesizer     → 写最终研究缺口
```

### C. 做大论文综述部分时

```
1. markitdown              → 整理导师给的论文、学位论文和笔记
2. literature-boundary-lock → 限定只能用给定资料
3. funnel-logic-organizer   → 按宏观到微观排序
4. citation-bridge-writer   → 补段落衔接
5. citation-syntax-auditor  → 修正引文句法
```

### D. 做项目申报书研究现状时

```
1. using-superpowers                  → 确认项目目标和申报要求
2. keyword-literature-download        → 检索项目相关文献
3. research-gap-auditor               → 提取研究空白
4. methodological-limitation-auditor  → 提出现有方法不足
5. research-gap-synthesizer           → 写项目必要性段落
```

### E. 写提示词时

以后在生成 Claude Code 提示词时，优先综合调用：
- using-superpowers
- brainstorming
- keyword-literature-download
- markitdown
- academic-abstract-pipeline
- literature-review-closed-loop-pipeline
- citation-syntax-auditor
- research-gap-synthesizer

---

## 八、安全性说明

1. 所有 skills 均为本地 SKILL.md 文件，不执行代码。
2. 不连接外部网络或 API。
3. 不修改系统级配置。
4. 不读取或写入用户文件以外的数据。
5. 原始 skills 已在安装前备份到 `skills_backup_literature_review_*`。

---

## 九、维护说明

- 如果需要修改某个 skill 的提示词，编辑对应文件夹下的 `SKILL.md`。
- 修改后无需重启 Claude Code，下次调用时自动载入最新版本。
- 如果某个 skill 不再需要，删除对应文件夹即可。
- 不要删除旧 skills 或覆盖其他用户的 skills。
