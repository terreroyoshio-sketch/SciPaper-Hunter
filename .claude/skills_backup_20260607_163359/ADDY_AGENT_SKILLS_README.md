# Addy Osmani Agent Skills — README

**来源**: https://github.com/addyosmani/agent-skills (MIT)
**Stars**: 41.7K | **版本**: v0.6.0 | **Skills**: 23 | **Commands**: 7 | **Agents**: 3
**安装日期**: 2026-05-15

---

## 标准开发生命周期

```
/spec → /plan → /build → /test → /review → /code-simplify → /ship
```

## 7 个 Slash Commands

| 命令 | 阶段 | 用途 |
|------|------|------|
| /spec | Define | 写结构化工程规格，目标、非目标、用户故事、验收标准 |
| /plan | Plan | 把 spec 拆成小步可验证任务 |
| /build | Build | 一次只做一个垂直切片，TDD 优先 |
| /test | Verify | 运行测试、补测试、记录结果 |
| /review | Review | 五轴审查: 正确性/可读性/架构/性能/安全 |
| /code-simplify | Simplify | 删除不必要复杂度，降低维护成本 |
| /ship | Ship | 并行调用 3 个 agent persona，输出 go/no-go |

## 3 个 Agent Personas

| Persona | 角色 | 职责 |
|---------|------|------|
| code-reviewer | 资深工程师 | 代码质量、架构、可维护性、API 设计 |
| test-engineer | QA 专家 | 测试覆盖、边界条件、回归、端到端 |
| security-auditor | 安全工程师 | OWASP Top 10、认证授权、注入、数据泄露 |

## 23 个 Skills

| 阶段 | Skills |
|------|--------|
| Define | interview-me, idea-refine, spec-driven-development |
| Plan | planning-and-task-breakdown |
| Build | incremental-implementation, test-driven-development, context-engineering, source-driven-development, doubt-driven-development, frontend-ui-engineering, api-and-interface-design |
| Verify | browser-testing-with-devtools, debugging-and-error-recovery |
| Review | code-review-and-quality, code-simplification, security-and-hardening, performance-optimization |
| Ship | git-workflow-and-versioning, ci-cd-and-automation, deprecation-and-migration, documentation-and-adrs, shipping-and-launch |
| Meta | using-agent-skills |

## 风险边界

- /ship 只做 go/no-go 审查，不自动部署
- 无脚本自动执行 git push/reset/clean/delete
- hooks 仅注入消息，不修改文件
- 所有代码修改类能力结合 tdd/testing 验证

## 与已有 Skills 的组合

| 阶段 | Addy Skills | 已有 Skills |
|------|-------------|-------------|
| Define | /spec, interview-me, idea-refine | grill-me, brainstorming |
| Plan | /plan, planning-and-task-breakdown | writing-plans, to-issues |
| Build | /build, incremental-implementation | tdd, testing, karpathy-guidelines |
| Test | /test | testing, Playwright, webapp-testing |
| Review | /review, code-review-and-quality | refactor, improve-codebase-architecture |
| Simplify | /code-simplify | improve-codebase-architecture |
| Ship | /ship, shipping-and-launch | git-workflow, verification-before-completion |
| Security | security-auditor, security-and-hardening | cso, security-review |
