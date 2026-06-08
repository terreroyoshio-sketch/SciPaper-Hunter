#!/bin/bash
# pre_delete_guard.sh
# PreToolUse Hook — 拦截危险命令
# 用途：阻止意外删除关键研究文件
# 风险：中，可能过度拦截
# 注意：启用前先在 hook_plan.md 确认范围

INPUT="$*"

# 保护的文件模式
PROTECTED_PATTERNS=(
    "rm -rf"
    "rm -r"
    "del /s"
    "rmdir /s"
    "format "
)

# 保护的文件路径
PROTECTED_PATHS=(
    "reports/citation_audit.md"
    "final_draft"
    "literature_matrix.csv"
    "evidence_cards"
)

# 检查危险命令
for pattern in "${PROTECTED_PATTERNS[@]}"; do
    if [[ "$INPUT" == *"$pattern"* ]]; then
        echo "=========================================="
        echo "[GUARD] 检测到危险命令: $pattern"
        echo "[GUARD] 完整命令: $INPUT"
        echo "[GUARD] 此操作已被拦截"
        echo "[GUARD] 如需执行，请在 .claude/hooks/hook_plan.md 中确认"
        echo "=========================================="
        exit 1
    fi
done

# 检查敏感路径
for path in "${PROTECTED_PATHS[@]}"; do
    if [[ "$INPUT" == *"$path"* ]]; then
        echo "=========================================="
        echo "[GUARD] 检测到受保护路径: $path"
        echo "[GUARD] 完整命令: $INPUT"
        echo "[GUARD] 操作已被拦截"
        echo "[GUARD] 如需执行，请先备份并人工确认"
        echo "=========================================="
        exit 1
    fi
done

exit 0
