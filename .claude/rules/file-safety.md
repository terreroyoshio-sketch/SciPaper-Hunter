# 文件安全 — File Safety

## 核心原则
科研数据不可逆丢失的后果严重。所有破坏性操作必须有记录、有备份、可恢复。

---

## 规则列表

### F1. rm -rf 前必须人工确认
- 任何递归删除操作必须先列明影响文件
- 等待人工确认后再执行
- 确认记录写入 `logs/deletion_log.md`

### F2. 删除测试项目也需记录
- 任何删除（无论目标为何）写入 `logs/deletion_log.md`
- 删除前检查是否还有未归档的 evidence matrix
- 删除前检查是否有活跃的引用依赖

### F3. 不得清理未归档的证据矩阵
- `literature_matrix.csv` 未归档前不得删除其来源文件
- `evidence_cards/` 未打包前不得 rm -rf
- 归档方式：备份到 `backups/` 目录或打包为 tar

### F4. 不得覆盖以下文件
- `citation_audit.md`（只能追加，不能覆盖）
- `final_draft/` 目录（只能版本递增）
- `reports/` 下的审计报告

### F5. 重建数据必须标记
- 任何非原始数据必须标记 `RECONSTRUCTED_TEST_DATA`
- 模拟数据标记 `SIMULATED_DATA`
- 标记不可删除（删除标记 = 数据造假）

### F6. 修改前先备份
- 关键文件在修改前必须有备份副本
- 备份文件命名：`filename.bak_YYYYMMDD_HHMMSS`
- 备份保留至少 30 天

---

## 安全操作清单

| 操作 | 前条件 | 后操作 |
|------|--------|--------|
| rm -rf 目录 | 人工确认 + deletion_log | — |
| 覆盖已有文件 | 检查是否为受保护文件 + 备份 | 记录到 file_change_log.csv |
| 重建测试数据 | 标记 RECONSTRUCTED_TEST_DATA | 记录重建原因 |
| 引用审计 | — | 只追加不覆盖 |
| 证据矩阵清理 | 确认已归档 | 记录到 deletion_log.md |
