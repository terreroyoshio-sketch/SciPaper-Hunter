# MCP 审计与建议

**审计日期:** 2026-06-08
**审计目标:** 评估当前 MCP 配置，提出是否安装新 MCP 的建议

---

## 当前状态

| 检查项 | 结果 |
|--------|------|
| 项目级 settings.json | ❌ 不存在 |
| 全局 ~/.claude.json | ✅ 存在（含 MCP servers？无法解析） |
| 当前 MCP 数量 | 0（项目级未配置） |

---

## 候选 MCP 评估

| MCP | 已安装 | 用途 | 建议保留 | 风险 | 备注 |
|-----|--------|------|---------|------|------|
| context7 | ❌ 否 | 查最新开发文档 | ❌ 不建议 | 低 | 更适合编程项目，非论文写作核心需求 |
| browser-mcp / puppeteer | ❌ 否 | 网页自动化和截图 | ❌ 不建议 | 低 | 本地已有 browser-harness，功能重叠 |
| sequential-thinking | ❌ 否 | 复杂推理链 | ⚠️ 可选 | 低 | 可辅助但不可替代证据核查 |
| filesystem | ❌ 否 | 文件操作 | ❌ 不建议 | 低 | Claude Code 已有 Read/Write/Edit 工具 |
| zotero | ❌ 否 | Zotero 文献库 | ⚠️ 视需要 | 低 | 仅当 Zotero 已安装且需要自动导出引用时考虑 |

---

## 结论与硬性规则

1. **当前不需要安装新 MCP。** 科研工作流的核心需求（文献检索、引用核查、文稿写作、格式导出）可通过现有 skills + 命令行工具满足。

2. **以下 MCP 在未来可能有价值:**
   - **Zotero MCP** — 如果 Zotero 本地库 > 200 条引用，可提升引用管理效率
   - **Sequential Thinking** — 适合复杂研究设计推理，但不应依赖它替代证据核查

3. **硬性约束:**
   - ❌ 不要安装未经评估的新 MCP
   - ❌ 不要修改 `~/.claude.json`
   - ❌ 不要保存 API Key
   - ❌ 不要把浏览器登录态暴露给未知 MCP
   - ❌ 不要将模拟审稿接入真实 MCP 服务

---

## 如果未来需要安装 MCP

```bash
# 安装步骤
1. 评估 MCP 的安全性和必要性
2. 在 .claude/settings.json 中配置（不修改 ~/.claude.json）
3. 先测试连接，再用于正式工作
4. 记录到 logs/version_log.md
```

---

*审计人: Claude Code*
