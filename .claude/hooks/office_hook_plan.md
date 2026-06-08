# Office Hooks 启用方案

## 概述
办公工作台专用 hooks 草案。**所有 hooks 默认禁用，需人工确认后启用。**

---

## Hook 总览

| Hook | 类型 | 触发时机 | 用途 | 风险 | 建议启用 |
|------|------|---------|------|------|---------|
| pre_delete_guard | PreBash | 执行命令前 | 拦截危险删除操作 | 中 | ✅ |
| post_file_change_log | PostWrite | 写入文件后 | 记录关键文件变更 | 低 | ⚠️ 可选 |
| session_end_office_summary | Stop | 会话结束 | 生成办公任务摘要 | 低 | ✅ |

---

## 1. pre_delete_guard.sh（复用已有）
- **路径:** `.claude/hooks/pre_delete_guard.sh`
- **用途:** 拦截 rm -rf、del /s、rmdir /s，保护 outputs、final_draft 等目录
- **风险:** 中，可能干扰正常删除
- **启用前确认:** 是否要保护 outputs/ 和 04_outputs/ 目录？

## 2. post_file_change_log.sh
- **路径:** `.claude/hooks/post_file_change_log.sh`
- **用途:** 每次写入 outputs/、final_*/、reports/ 后记录到 logs/file_change_log.csv
- **风险:** 低
- **启用前确认:** 是否会因日志噪音过大关闭？

## 3. session_end_office_summary.sh
- **路径:** `.claude/hooks/session_end_office_summary.sh`
- **用途:** 生成 reports/latest_office_status.md，记录完成内容、文件、风险、下一步
- **风险:** 低
- **启用前确认:** 是否需要每次会话结束生成？

---

## 启用配置

```json
{
  "hooks": {
    "PreBash": "bash .claude/hooks/pre_delete_guard.sh {{command}}",
    "PostToolUse": {
      "matcher": "bash .claude/hooks/post_file_change_log.sh {{tool}} {{input}}",
      "scope": "write"
    },
    "Stop": "bash .claude/hooks/session_end_office_summary.sh"
  }
}
```

## 人工确认清单
- [ ] 启用 pre_delete_guard？
- [ ] 启用 post_file_change_log？
- [ ] 启用 session_end_office_summary？
- [ ] hooks 脚本有执行权限？
