# 科研工作台 — Research Workbench

> 项目定位：辅助文献检索、选题、综述、论文写作、引用核查、审稿模拟、图表排版和科研材料导出。
> 创建日期：2026-06-08

---

## 默认规则

1. **反造假优先** — 不编造文献、数据、统计量、伦理审批。未核验信息必须标注。
2. **文献核验优先** — 引用必须可追踪、可验证。DOI missing 不得标记为 fully_verified。
3. **数据可得性优先** — 未获得数据前不写样本量、不写统计量、不写"实验结果表明"。
4. **伦理审批优先** — 涉及人的数据必须检查伦理要求。AI 不替代伦理审批。
5. **不写不可验证结论** — 所有结论必须有证据支撑。

详细规则见 `.claude/rules/` 目录。

---

## 核心 Skills

| Skill | 用途 |
|-------|------|
| academic-paper | 12-agent 论文写作流水线 |
| academic-paper-reviewer | 多角度论文评审 |
| academic-pipeline | 学术研究编排器 |
| ai-powerpoint-research-workflow | 科研 PPT 工作流 |
| autonomous-survey-agent | 自主综述写作 Agent |
| deep-research | 13-agent 深度研究团队 |
| my-academic-research-master | 本地科研总控 |
| research-idea-conflict-miner | 冲突驱动选题孵化器 |
| sci-research-writing-narrative | SCI 叙事写作 |

**缺失 skills（在备份中，需人工恢复）:**
- keyword-literature-download
- critical-literature-review-pipeline
- literature-boundary-lock
- citation-format-syntax-auditor
- objectivity-calibration-auditor
- reviewer-red-team-auditor

---

## 常用 Commands

| 命令 | 用途 |
|------|------|
| `/idea` | 科研选题孵化（调用 research-idea-conflict-miner） |
| `/review-lit` | 文献综述流程 |
| `/check-citations` | 引用核查 |
| `/redteam` | 审稿人攻击 |
| `/paper-draft` | 论文初稿生成（有前置条件检查） |
| `/format-doc` | 文档排版与导出 |
| `/pacs-precheck` | 医学影像 PACS 预查 |

详细说明见 `.claude/commands/` 目录。

---

## 文件安全

- 删除、覆盖、清理前必须确认
- `citation_audit.md` 只追加不覆盖
- `final_draft/` 只版本递增不覆盖
- 测试/重建数据必须标记 `RECONSTRUCTED_TEST_DATA`
- 关键文件修改前先备份（命名：`filename.bak_YYYYMMDD_HHMMSS`）
- 所有删除操作记录到 `logs/deletion_log.md`

---

## 6 层架构

| 层 | 路径 | 用途 |
|----|------|------|
| Commands | `.claude/commands/` | 高频快捷调用 |
| Skills | `.claude/skills/` | 标准科研 SOP |
| Rules | `.claude/rules/` | 长期约束规则 |
| Hooks | `.claude/hooks/` | 自动化钩子（草案） |
| Agents | `.claude/agents/` | 上下文隔离的 subagent 定义 |
| Plugin | `.claude-plugin-draft/` | 预留迁移方案 |

---

## 输出习惯

每次复杂任务结束后，输出：

1. ✅ 完成了什么
2. 📄 生成了哪些文件
3. ❌ 没完成什么
4. ⚠️ 风险是什么
5. 👣 下一步最小动作是什么

---

## 排版参考

- 中文正文：宋体小四（12pt），1.5 倍行距，首行缩进 2 字符
- 英文正文：Times New Roman（12pt），1.5 倍行距
- 表格：三线表，仅表头加粗
- 图片：300 dpi，优先 SVG/Visio
- 公式：Times New Roman italic 或 LaTeX 数学字体
