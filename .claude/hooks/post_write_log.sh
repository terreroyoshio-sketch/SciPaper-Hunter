#!/bin/bash
# post_write_log.sh
# PostToolUse Hook — 记录关键文件变更
# 用途：每次创建或修改关键文件后写入变更日志
# 风险：低
# 注意：只在写入到关键路径时触发

TOOL="$1"
INPUT="$2"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# 只记录关键路径
KEY_PATHS=(
    ".claude/commands"
    ".claude/rules"
    ".claude/agents"
    ".claude/hooks"
    "reports"
    "outputs"
    "CLAUDE.md"
)

for path in "${KEY_PATHS[@]}"; do
    if [[ "$INPUT" == *"$path"* ]]; then
        # 提取文件路径（假设 input 中包含路径信息）
        FILE_PATH=$(echo "$INPUT" | grep -oP "$path/\S+" || echo "$INPUT")
        echo "$TIMESTAMP,WRITE,$FILE_PATH,hook auto-log,post_write_log," >> "logs/file_change_log.csv"
        break
    fi
done

exit 0
