# Open-Source Skill Review Report

**Date:** 2026-06-07
**Task:** 核验并学习 5 个开源科研项目

---

## 评审总表

| 项目 | 是否适合安装 | 适合任务 | 不适合任务 | 安装方式 | 风险 | 推荐优先级 |
|------|------------|---------|-----------|---------|------|----------|
| **Academic Research Skills (ARS)** | **✅ 适合安装** | 文献检索、论文写作、同行评审模拟、完整科研流水线 | 需要原创实验的论文（需配合 experiment-agent） | Plugin 或手动 git clone + 复制 skill 目录 | CC-BY-NC 4.0 禁止商用；依赖 tectonic 编译 APA 格式 PDF | ⭐⭐⭐ 最高 |
| **OpenScholar** | **❌ 不适合本地完整部署** | 检索增强生成、引用准确性核查 | 轻量综述、快速写作（太重） | 仅学习思想，不部署 | 需要 200M+ 向量的本地索引，CPU 内存需求极高 | ⭐ 仅学习 |
| **AutoResearchClaw** | **⚠️ 学习但不安装** | 端到端自动化科研流水线（23 阶段） | 纯文献综述（过度设计） | `pip install -e .` | 需要 Docker + 较多 API Key；全流水线运行成本高 | ⭐⭐ 学习其 SKILL.md 加载机制 |
| **Dr. Claw** | **⚠️ 学习但不安装** | 长期多项目科研管理 IDE | 单篇论文快速写作（太重） | `npx dr-claw` 或 npm 全局安装 | 依赖 React/Node.js 全栈；需要至少一个 AI CLI；仍在活跃开发 | ⭐⭐ 学习其技能组织方式 |
| **24/7 Deep Researcher** | **❌ 不适合默认安装** | 深度学习实验自动化（需 GPU） | 纯文献综述、无实验论文 | `pip install -r requirements.txt && python install.py` | 需要 GPU + API Key；只跑文献综述不要装 | ⭐ 仅学习 |

---

## 详细评审

### 1. Academic Research Skills (ARS)

**仓库:** https://github.com/Imbad0202/academic-research-skills
**Stars:** 28.3k | **License:** CC-BY-NC 4.0 | **版本:** v3.11.1

**包含的 4 个核心 skill:**
| Skill | 版本 | 功能 |
|-------|------|------|
| `deep-research` | v2.9.4 | 13-agent 研究团队，7 种模式（full/quick/review/lit-review/fact-check/socratic/systematic-review） |
| `academic-paper` | v3.2.0 | 12-agent 论文写作，10 种模式，Style Calibration，反 AI 高频词检查 |
| `academic-paper-reviewer` | v1.10.0 | 7-agent 审稿（EIC + 3 动态审稿人 + 魔鬼代言人），6 种模式 |
| `academic-pipeline` | v3.11.1 | 10 阶段编排器，2 个强制完整性门禁（Stage 2.5 + 4.5） |

**关键特性:**
- ✅ 3 层引用锚点（quote/page/section），防幻觉
- ✅ CLAIM-FAITHFULNESS AUDIT（需要 ARS_CLAIM_AUDIT=1 开启）
- ✅ 确定性引用存在性检查（4 个文献索引交叉核验）
- ✅ 阶段 2.5 和 4.5 的强制完整性门禁（不能跳过）
- ✅ Style Calibration 机制（学习用户过去 3+ 篇论文风格）
- ✅ 25 个 AI 高频词警告
- ✅ 输出 APA/IEEE/Chicago/MLA/Vancouver + LaTeX/DOCX
- ✅ 10 个 `/ars-*` 快捷命令

**限制:**
- ⚠️ **CC-BY-NC 4.0 license** — 禁止商业使用（教学、学术、个人使用允许）
- ⚠️ APA 7.0 PDF 编译需要 `tectonic` + Source Han Serif TC 字体（我们可用 latexmk 替代）
- ⚠️ 不支持无网络环境（依赖 Semantic Scholar API）

**安装决策: 安装** — Plugin 方式优先，手动复制为备选。

---

### 2. OpenScholar

**仓库:** https://github.com/akariasai/openscholar
**License:** Apache 2.0

**关键机制:**
- 基于 peS2o 数据存储（4500 万篇论文，2 亿+ 段落嵌入）
- 检索增强生成：检索 → 重排序 → 自反思生成 → 事后引用归因
- 自反馈循环（`--feedback`）：生成后自我批评和优化
- 事后引用归因（`--posthoc`）：确保引用与论点匹配
- 支持 Semantic Scholar API + you.com 网页搜索

**本地部署需求（不可行）:**
- 需要 200M+ 嵌入向量的本地索引
- "requires a lot of CPU memory"（官方原话）
- 需要 S2_API_KEY（Semantic Scholar）和 you.com API Key
- 需要 Python 3.10（我们的是 3.14）

**可借鉴的思想:**
1. 引文归因的事后核验
2. 自反馈循环（生成 → 自评 → 修正）
3. 最小引用数过滤（`min_citation`）
4. 检索增强的文献回答

**安装决策: 不安装**。只学习其设计思想，在 `openscholar_style_rules.md` 中记录工作原则。

---

### 3. AutoResearchClaw

**仓库:** https://github.com/aiming-lab/AutoResearchClaw
**License:** MIT | 96.3% Python

**关键机制:**
- 23 阶段 8 阶段流水线（从选题到发表）
- 多源文献发现：OpenAlex → Semantic Scholar → arXiv
- 4 层引用验证：arXiv ID → CrossRef/DataCite DOI → Semantic Scholar 题名匹配 → LLM 相关性评分
- PIVOT/REFINE 自主决策循环
- 自学习/MetaClaw：从失败中提取教训，转化为可复用 skills
- 6 种人机交互模式（全自动到逐步指导）
- 技能库：SKILL.md 自动加载机制

**值得学习的机制:**
1. **SKILL.md 加载机制** — 只需把 SKILL.md 放到 `.claude/skills/` 即可被自动发现
2. **`researchclaw skills validate`** — 验证 SKILL.md 格式的命令
3. **4 层引用验证流水线**
4. **PIVOT/REFINE 决策模式** — 适合长时间研究项目
5. **预算控制** — `hitl.cost_budget_usd: 50.0`

**不安装的原因:**
- 完整流水线（23 阶段）对纯文献综述过度设计
- 需要 Docker + 多个 API Key
- 全流水线运行成本高
- 已有 `autonomous-survey-agent` 覆盖了同样需求

**安装决策: 不安装完整系统**。但其 skill 加载机制和引用验证方法已融入我们的设计。

---

### 4. Dr. Claw

**仓库:** https://github.com/OpenLAIR/dr-claw
**License:** GPL-3.0 / AGPL-3.0 | 主要语言: JavaScript 39.3%, TypeScript 24.8%

**关键机制:**
- 科研 IDE：Web UI + Node.js 后端 + AI CLI 集成
- 100+ 内置 skills
- 项目管理：Survey → Ideation → Experiment → Publication → Promotion
- 文献管理：arXiv/HuggingFace/GitHub/微信公众号 聚合阅读
- 本地 Zotero 集成
- Local-first 架构

**值得学习的机制:**
1. **100+ skills 的组织方式** — `skills/` 目录自动 symlink 到项目
2. **项目目录结构** — 各阶段有独立目录
3. **会话管理** — 智能命名和阶段标记
4. **Claude Code Plugin** — 60+ skills 子集（终端友好）

**不安装的原因:**
- 需要 Node.js + React 全栈 + 至少一个 AI CLI
- `npx dr-claw` 本身轻量，但完整 IDE 太重
- 我们已有 skills 组织方式（直接放 `.claude/skills/`）

**安装决策: 不安装完整系统**。其 skill 组织方式已借鉴。

---

### 5. 24/7 Deep Researcher

**仓库:** https://github.com/Xiangyue-Zhang/auto-deep-researcher-24x7
**License:** Apache 2.0

**关键机制:**
- Leader-Worker 架构（Leader 分发任务给 IdeaAgent/CodeAgent/WritingAgent）
- 恒定大小内存（`PROJECT_BRIEF.md` 3000 字 + `MEMORY_LOG.md` 2000 字）
- 零成本监控（`kill -0 $PID` + `nvidia-smi`，不用 LLM 检查）
- THINK → EXECUTE → MONITOR → REFLECT 循环
- 实验账本（`experiments.jsonl`）持久化
- Dead Ends 和 Insights 日志

**激活条件（必须全部满足）:**
1. ❓ 用户明确要跑真实代码实验
2. ❓ 已有数据集
3. ❓ 已有 baseline
4. ❓ 有 GPU 或可用计算环境
5. ❓ 有明确评价指标
6. ❓ 能保存日志和模型权重

**当前评估: 上述条件均不满足**。当前只是搭建科研工作流环境，不是深度学习实验。

**可借鉴的思想:**
1. 恒定大小内存机制 — 适合长期运行的项目
2. 零成本监控 — 节省 API 调用
3. 实验账本 — 实验的完整记录
4. Dead Ends / Insights 分离跟踪

**安装决策: 不安装**。仅在需要跑深度学习实验时考虑。

---

## 安装优先级总结

```
优先级 1 (立即安装):   Academic Research Skills (ARS)
优先级 2 (学习借鉴):   AutoResearchClaw (SKILL.md 机制)
优先级 3 (学习借鉴):   OpenScholar (引用核验思想)
优先级 4 (条件安装):   24/7 Deep Researcher (只在有 GPU 实验时)
不推荐安装:            Dr. Claw 完整 IDE (太重)
```
