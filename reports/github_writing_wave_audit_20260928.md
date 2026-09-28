# 写作治理波审计报告（2026-09-28）

> 范围: `github_candidate_audit_20260927.md` 表 B 的写作与治理波 7 项
> 方法: GitHub API 许可核验（2026-09-28）+ 仓库页/README 只读细读；**未安装、未运行**
> 边界: 本报告只出决策建议；吸收/安装需你点名后执行（安装前另做只读快审）
> 状态: 7 项全部拿到许可与活跃度数据

---

## 决策总表

| 项目 | Stars | License | 核验 | 决策建议 |
|------|-------|---------|------|---------|
| [Nanako0129/sepia](https://github.com/Nanako0129/sepia) | 2.9k | **MIT** | A+P | `INSTALL_OR_PATTERN` — 结构级写作质量（与现有词级技能互补） |
| [mikubaka88/CCFA-Skills](https://github.com/mikubaka88/CCFA-Skills) | 2.9k | **MIT** | A+P | `PATTERN_ONLY` — 只提取评审格式与完整性清单（与现有 paper-*/nature-* 重叠大） |
| [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) | 3.7k | **MIT** | A+P | `PATTERN_FIRST` — gate ledger 机制；含 Stop hook，安装须先沙箱验证 |
| [lennney/stop-that-shit](https://github.com/lennney/stop-that-shit) | 2.3k | **MIT** | A+P | `PATTERN_FIRST` — SHIT 分类 + guard 证据分离；含 hook 拦截，同上 |
| [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) | 5.7k | **PolyForm Noncommercial 1.0.0** | A+P | `OBSERVE` — NC 限制（仅自用参考）；图表能力已有 figurelab/nature-figure 覆盖 |
| [AminBlg/SimpleEnglish](https://github.com/AminBlg/SimpleEnglish) | 3.6k | **MIT** | A | `OBSERVE` — 与下一项二选一即可 |
| [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) | 2.3k | **MIT** | A | `OBSERVE` — 同上 |

---

## 逐项要点

### 1. sepia（MIT）— 唯一推荐的"可安装"候选
- **机制**：基于 StoryScope（arXiv:2604.03136）的**叙事结构级**去 AI 痕迹，而非改词。三遍协议：叙事架构（停止解释主题、放松因果链、后置揭示）→ 语篇流（去模板化段落序列、变化节奏）→ 表层风格（陈词、句法、词汇、语域）。
- **证据链**（其自述）：仅用叙事结构特征分类器在 AI 小说上 93.2% macro-F1；人类编辑做表层改写只把检出率从 95.5% 移到 93.9%（=改词没用）；专业散文有一 2026 复现（2,250 篇博文 vs 11,250 AI 镜像，98.0 macro-F1，**preprint、LLM 打分特征**）。
- **可提取的具体资产**：30 特征诊断量表；Per-model 指纹（Claude/GPT/Gemini/DeepSeek/Kimi）；中文规则 `zh.md`（HC3 2023 + ~2000 篇文章 + 119 篇合成，分四层证据）；唯一保留的句法信号 =**句长散布**（人类文本句长方差更大）；原则"Calibrate to the human distribution, don't invert the AI one"（向人类分布校准，别对着 AI 分布反着来）；四种操作 write/review/refactor/recreate。
- **与现有技能关系**：你的 hype-language-cleaner / academic-tone-standardizer / defensive-tone-neutralizer / academic-writing-refiner 全在**词与语气级**；sepia 在**结构级**——互补不重复。
- **⚠️ 学术场景边界（必须写明）**：按你的规则"不承诺查重率或 AIGC 检测结果"。此工具吸收时定位为**写作质量改进**（结构自然度），不得用于规避检测的宣传口径；改写不得改变事实、数据、引用与结论。

### 2. CCFA-Skills（MIT）— 只提取格式
- 17 个技能（idea/literature/experiment/integrity/writing/review/rebuttal/figures…），v0.10.0，60 commits，含 ICLR 2027 适配。
- **值得提取的两件**：① 评审输出的**固定节数格式**（全文评审 14 节 / 写作评审 9 节 / 简报 5 块）+ 七维评分（novelty/correctness/evidence/significance/clarity/reproducibility/ethics）；② 评审区分**两个问题**——稿件是否可投 vs 修改是否真的变好。另有 ccf-integrity-auditor 的检查面（声明/数字/术语/图/引用）。
- **不提取**：其余与你的 paper-*/nature-*/reviewer 族重叠；不整体安装（17 技能体量、动线冲突）。其自注：4 个 check 脚本"只验证结构与引用，不等于模型质量"——引用时保持此限定。

### 3. unlazy（MIT）— gate ledger 模式（先模式、后安装）
- **Depth Tree**：任务拆 N 层，**每个叶节点拿整份时间预算**（预算不切割、重复使用）→"努力随深度放大"。⚠️ 方法细节在其 `references/method.md`（本报告未读），仅记一句摘要，勿当全貌。
- **Gate ledger（真正的机制亮点）**：先写 `GATES.md` 验收台账；每条 gate = `CHECK:`/`EXPECT:`/`CWD:`/`EVIDENCE:`；**可运行 gate 通过 = 退出码 0 且 EXPECT 匹配输出**；证据绑定到定义文本的 SHA-256（结构漂移 → 证据变 stale，其明确声明"检测漂移，不检测篡改"）；`--reverify` 重跑全部（含已完成）；放弃 gate = `HANDOFF REQUIRED` 退出 1，且不能把父项标完成；空台账/重复 id/不完整 gate 被解析器拒绝；可选 Stop hook 未达标时返回 block，**连续 6 次无实质进展自动放行**（防死循环）。
- **其诚实的自我限定（值得学习的态度）**：README 明说研究"不能证明 unlazy 带来固定提升"；2.1.0 未发版，建议 pin commit 安装。
- 与你的 verification-before-completion + evidence-levels + agent-execution-patterns #10 同族。**含 Stop hook → 不建议现在整装；先提取模式**。

### 4. stop-that-shit（MIT）— SHIT 分类 + guard（先模式、后安装）
- **SHIT 四分类**（Scope creep / Hashing & hypothetical hardening / Intent violation / Task thrashing）：范围蔓延；没人看的校验和与为想象未来造的兼容层（"防御要能触发拒绝、恢复或诊断"）；只读评审却改了文件（"审查就报告问题，修改需要授权"）；没有新问题的重复读/测/审。
- **Guard 机制**：工具调用级拦截（review/answer/monitor 模式下写文件 → 拦；加依赖 → 问；子代理超 `agents=N` 预算 → 拦；加哈希 → 拦；`files=` 外写 → 拦）；指令集 review/answer/monitor/change/watch/status；安装后 `OBSERVING / unconfirmed`，显式指令才 `ARMED`。
- **证据分离（与你的证据纪律同构）**：被拒时报告 `permission_deny_returned`，**host 是否真的执行了拦截单独记为 `hostEffect: unobserved`**——"我们拦了"与"宿主遵守了"分开陈述。
- 附带 STSS（slop-trimmer：trim/rewrite/audit 三模式）。**含 hook 拦截 → 同上，先模式**。

### 5-7. lieflat-charts / STE100 两项 — 观察
- lieflat-charts：**PolyForm Noncommercial 1.0.0**（学习/修改/分享/非商业可用；商用另许）。按其条款可自用参考，但**不得并入将再分发的产物**；且你的图表能力（figurelab + nature-figure + 期刊规范）已覆盖其价值。仅记录其风格资产名目（Lupi Editorial/Basics、Glance、Interactive 四风格；Porcelain/Palm/Wire 三色板；12 全页报告模板）供灵感。
- STE100 双件套：MIT；用途是技术文档的"简化技术英语"改写（ASD-STE100 是航空维修文档标准）。注意 **ASD-STE100 标准文本本身有独立版权/使用条款**，技能虽 MIT 但不可连标准词表一起搬运。学术论文场景收益有限，标 OBSERVE。

---

## 建议的吸收组合（待你点名）

- **方案 A（推荐）**：① sepia —— 先只读快审，通过则作为插件安装；② 新建 1 个 reference skill `completion-guard-patterns`（unlazy gate ledger + stop-that-shit SHIT/guard 共 ~8 条模式，含证据文件）——不含 hook 安装。
- **方案 B**：只做 ①（sepia）。
- **方案 C**：只做 ②（模式 skill）。
- **方案 D**：再加 CCFA 评审格式 9 条清单 → 并入方案 A 的 skill 或单列。

未选项保持 OBSERVE，不动作。
