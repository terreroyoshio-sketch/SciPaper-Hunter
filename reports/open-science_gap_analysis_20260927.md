# open-science 对照审计报告（2026-09-27）

> 对照对象: [aipoch/open-science](https://github.com/aipoch/open-science)（Apache-2.0，4.9k★，v0.33.3，2026-09 活跃）
> 审计方式: **页面/README 级只读核对**（2026-09-27 快照）；未安装、未运行其代码
> 我们侧实读文件: `.codex/skills/research-execution-provenance/SKILL.md`（v1.1.0）、`templates/research-provenance-record.example.json`（schema_version 2.0）、`.research-ai/engineering-skill-registry.yaml`（schema 2.0）
> 边界: 本报告**不改动** canonical provenance skill；下述"建议吸收"项如需落地须单独立项批准
> 同名警示: 另有 `synthetic-sciences/openscience`（3.6k★，同日创建），关系未查清，勿混用其材料

---

## 对照总表

| # | 维度 | open-science 机制（其 README 自述） | 我们现有对应 | 判定 |
|---|------|-----------------------------------|-------------|------|
| 1 | 产物溯源 | 产物**不可变校验和版本**：含生产者代码、输入、执行历史、环境清单、评审证据 | provenance Skill：`dataset_content_sha256` 绑定、code snapshot、runs/lineage、`environments` 字段、`result_freezes`；语义层（双轴证据模型 + 阻断码）比其描述更严 | 部分覆盖，见建议 1 |
| 2 | 评审证据 | 可选"完成回合自动评审"：pass/warning/failure + **有界修正循环**；评审证据随产物存 | 评审族齐备（academic-paper-reviewer / red-team-reviewer / statistical-reviewer / quality-assurance-auditor）但为**显式触发**；记录模板未见"评审证据"一等字段 | 部分覆盖，见建议 2 |
| 3 | 环境清单 | environment inventory 作为标准产物捕获 | `environments` 字段已有；SKILL.md 语义明确 `ENVIRONMENT_RECORDED < ENVIRONMENT_REPRODUCIBLE` | 已覆盖（操作核对项） |
| 4 | 文献库 | 内置 Literature Library（references/PDFs + BibTeX/RIS 导出） | 分散于 skills：nature-academic-search / paper-lookup / pyzotero / citation-management + Zotero | 不吸收（架构路线不同；导出通路已有） |
| 5 | Skills 分发 | 23 内置 + **525 市场** skills，一键安装/从 GitHub/Git 包导入 | registry schema 2.0（逐条目：许可/维护/安全/本地状态）+ wrapper-first + 安装需批准 | 不吸收路线（治理优先于分发规模） |
| 6 | 工具权限 | 自定义 MCP 连接器支持**工具级权限** | `mcp-permission-auditor` 已审计 read-vs-write scopes、shell/fs/browser reach 等 | 已覆盖 |
| 7 | 人审分级 | 三档：Ask for approval / Auto-approve edits / Full access | provenance SKILL.md 的人类门禁清单（删除原始数据/推送/发布/敏感上传/hardware/伦理声明…）+ 权限模式 | 已覆盖（我方规则粒度更细） |
| 8 | 项目可移植 | 便携 `.science` 包（项目整体打包） | runs/EXP + PROJECT_STATE + freeze 概念；无单一可移植包格式 | 观察（可选吸收，见建议 4） |
| 9 | 运行时 | Electron + ACP agent runtime；后端支持 Claude Code / Codex / CodeBuddy 等 | skill 组合 + CLI 会话（Skill-based 路线） | 不吸收（路线选择）；其后端列表与多 harness 生态同向，可观察 |
| 10 | 可信度 | 自报 BiomniBench-DA Public 50 = 79.05（gpt-5.6-sol xhigh）；已挂 Zenodo DOI | 我方证据纪律（自报 vs 独立复现须分开标注） | 引用时按**自报**处理，分数与模型版本绑定、不可外推 |

## 逐项说明（仅展开有结论的）

**维度 1｜产物溯源**：其"不可变校验和版本"是**产品级自动行为**（写入即固化版本 + 校验和）；我们的是**规则 + 结构校验器 + 人工纪律**（`validate_provenance.py` 只做结构性检查，SKILL.md 明确"hash 只证明声明范围内的内容同一性"）。两者对哈希语义的理解一致；差距在**自动化程度**与**冻结交付物形态**。

**维度 2｜评审证据与修正循环**：其"有界修正循环"（bounded correction cycles）与我方 `agent-execution-patterns` 的反面教材（DOT-2 不收敛：修状态判定，而非调大轮询间隔）是同一类问题的两面 —— 评审循环**必须有上限与终态**。此点值得在采纳时显式写明上限。

**维度 9｜路线差异**：其把工作流做成一体化应用；本工作台坚持 Skill 组合 + 治理层（rules/registry/证据门）。这是路线选择而非缺陷；对照价值在于**其产品功能清单可以当作本工作台能力缺口的检查表**（本报告正是这么用的）。

## 建议吸收（先建议，不落地；落地需单独批准）

1. **冻结场景增补"产物校验和清单"**（吸收）：结果冻结时，把关键产物（数据/图件/代码快照/记录）的"路径 → 校验和"清单作为交付物一并生成。先作为**操作规范**执行；schema 归属（是否并入 `result_freezes`）待下一步核对 validator 与 governance reference 再定——**不先扩 schema**。
2. **评审证据一等化**（吸收）：正式结果评审时留存"reviewer 证据"（评审者/检查项/结论/修正轮次与上限）随记录归档；与现有 reviewer 族输出衔接，不新建评审机制。
3. **环境清单实操核对**（核对，非新机制）：确认正式冻结记录中 `environments` 字段确实被填充，且区分 RECORDED / REPRODUCIBLE 两级。
4. **可移植冻结包**（观察→可选）：冻结场景可选生成单一包（记录 + 产物 + 环境 + 代码快照）。与其 `.science` 包同型；当前不急，列入 backlog。
5. **不吸收并记录理由**：marketplace 一键安装（治理优先，避免绕过审计直装）、Electron 一体化（路线不同）、每轮自动评审（与上下文/token 预算冲突；显式评审族已覆盖需求）。

## 未验证与局限

- 其全部机制描述来自仓库页/README（页面级），**未安装、未运行、未读源码**；"机制存在"按其自述记录，不等于已验证。
- 其 benchmark 分数（79.05）为自报，且与具体模型版本绑定；与本报告结论无依赖。
- 我方字段核对基于模板示例（schema_version 2.0, 2026-09-04）与 SKILL.md（v1.1.0）；未逐行核对 validator 实现，`result_freezes` 内部字段未展开。
- 同名项目 synthetic-sciences/openscience 未审计，本报告不涉及其内容。
