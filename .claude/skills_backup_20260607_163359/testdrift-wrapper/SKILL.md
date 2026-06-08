---
name: testdrift-wrapper
version: 1.0
language: 中文
description: 测试漂移检查 skill，用于在代码变更后识别测试缺口、生成测试计划、补充测试并运行验证，防止 AI 写完代码却遗漏测试。
---

# TestDrift Wrapper

## Goals
- 检查最近代码变更。
- 识别新增函数、修改函数、新增组件和 API 变化。
- 检查是否已有对应测试。
- 生成测试缺口报告。
- 生成单元测试、集成测试或端到端测试计划。
- 用户确认后再写测试。
- 运行测试并保存日志。

## Constraints
- 不得伪造测试通过。
- 不得一口气重写测试体系。
- 不得改无关代码。
- 不得默认删除旧测试。
- 不得把脆弱测试当成完成。
- 不得在没有日志时声称测试成功。

## Workflow
1. 获取 git diff 或用户提供的变更文件。
2. 识别变更影响范围。
3. 检查 tests 目录和测试命名规则。
4. 输出测试缺口报告。
5. 生成测试计划。
6. 用户确认后写测试。
7. 运行测试。
8. 保存日志。
9. 输出通过、失败和待修复项。

## Integration
- 与 testing、tdd、webapp-testing、Addy /test 互补
- testing/tdd 负责测试方法论，testdrift-wrapper 负责变更缺口检测
- 推荐与 git-workflow 联合使用，每次 commit 前运行

## Output
- test_gap_report.md
- test_plan.md
- test_run_log.txt
- failed_tests.md
- coverage_notes.md
