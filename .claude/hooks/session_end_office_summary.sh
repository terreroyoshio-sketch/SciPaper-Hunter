#!/bin/bash
# session_end_office_summary.sh
# SessionEnd Hook — 生成办公任务会话摘要
# 用途：记录本次完成、文件、风险和下一步
# 风险：低

TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
REPORT="reports/latest_office_status.md"

cat > "$REPORT" << EOF
# 办公工作台会话状态

**生成时间:** $TIMESTAMP

## 本次完成
- （由会话结束时自动填充）

## 生成文件
- （同上）

## 未完成
- （同上）

## 风险提醒
- 网页信息必须有 URL 和访问日期
- 原始文件不可删除
- 隐私字段不可导出
- 自动化任务未经确认不可启用

## 下一步最小动作
- （同上）

---

*由 session_end_office_summary hook 自动生成*
EOF

echo "[OFFICE SUMMARY] 会话摘要已生成: $REPORT"
