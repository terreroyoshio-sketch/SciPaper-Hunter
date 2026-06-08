#!/bin/bash
# session_end_summary.sh
# SessionEnd Hook — 生成会话摘要
# 用途：记录本次完成、未完成、下一步
# 风险：低，只追加写

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
REPORT="reports/latest_status.md"

# 检查 logs/version_log.md 获取当前版本
VERSION="unknown"
if [ -f "logs/version_log.md" ]; then
    VERSION=$(grep "^# v" "logs/version_log.md" | tail -1 | sed 's/# //')
fi

cat > "$REPORT" << EOF
# 会话状态报告

**生成时间:** $TIMESTAMP
**版本:** $VERSION

## 本次完成
- （由会话结束时自动填充）

## 未完成
- （同上）

## 下一步最小动作
- （同上）

## 风险提醒
- 反造假规则始终生效
- 引用核查通过前不进入写作
- 所有修改在 cold start 后以 CLAUDE.md、commands、rules、agents 为准

---

*由 session_end_summary hook 自动生成*
EOF

echo "[SUMMARY] 会话摘要已生成: $REPORT"
