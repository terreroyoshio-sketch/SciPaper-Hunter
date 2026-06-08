#!/bin/bash
# post_file_change_log.sh
# PostToolUse Hook — 记录办公任务文件变更
# 用途：写入 outputs/、final_*/、reports/ 后记录日志
# 风险：低

TOOL="$1"
INPUT="$2"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

KEY_PATHS=(
    "outputs"
    "04_outputs"
    "final_docs"
    "final_ppt"
    "final_images"
    "reports"
)

for path in "${KEY_PATHS[@]}"; do
    if [[ "$INPUT" == *"$path"* ]]; then
        FILE_PATH=$(echo "$INPUT" | grep -oP "$path/\S+" || echo "$INPUT")
        echo "$TIMESTAMP,WRITE,$FILE_PATH,office hook auto-log,post_file_change_log," >> "logs/file_change_log.csv"
        break
    fi
done

exit 0
