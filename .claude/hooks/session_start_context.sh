#!/bin/bash
# session_start_context.sh
# SessionStart Hook — 加载项目状态
# 用途：每次会话开始时提醒当前项目状态
# 风险：低，只读操作

echo "=== 科研工作台状态 ==="

# 检查 CLAUDE.md
if [ -f "CLAUDE.md" ]; then
    echo "[OK] CLAUDE.md 存在"
else
    echo "[WARN] CLAUDE.md 不存在 — 缺少项目总规则"
fi

# 检查 latest_status
if [ -f "reports/latest_status.md" ]; then
    echo "--- 上次会话状态 ---"
    head -20 "reports/latest_status.md"
fi

# 检查 version_log
if [ -f "logs/version_log.md" ]; then
    echo "--- 版本日志最新条目 ---"
    tail -5 "logs/version_log.md"
fi

# 检查未完成的审计
if [ -f "reports/citation_audit.md" ]; then
    echo "[NOTE] 引用审计报告存在 — 检查是否需要更新"
fi

# 反造假提醒
echo "---"
echo "[RULE] 反造假规则生效中 — 不编造文献、数据、统计量"
echo "[RULE] 引用核查通过前不进入写作阶段"
echo "======================"
