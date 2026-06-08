# Addy Osmani Agent Skills — Prompt Templates

---

## Template 1: 完整软件开发生命周期

```
请使用 Addy Osmani Agent Skills。按照 /spec → /plan → /build → /test →
/review → /code-simplify → /ship 的顺序处理以下任务。
第一轮只执行 /spec 和 /plan，不要写代码。等我确认后再进入 /build。

任务：【填写任务】

约束：
- 不要一口气写完所有代码。
- 每一步必须有验证方式。
- 不得自动 push、deploy 或 release。
- 每个阶段都要输出完成条件。
```

## Template 2: 只写 spec

```
请执行 /spec。请把以下模糊需求整理为工程规格说明，包括目标、非目标、
用户故事、边界条件、数据模型、接口、失败场景、验收标准和开放问题。
不要写代码。

需求：【填写需求】
```

## Template 3: 生成实施计划

```
请执行 /plan。基于以下 spec，请拆解为小步实施计划。
每一步必须包含目标、影响文件、测试方式、风险和回滚策略。
不要写代码。

Spec：【粘贴 spec】
```

## Template 4: 小步构建

```
请执行 /build，并结合 tdd 和 testing。请只实现计划中的第一个垂直切片。
先写测试或测试计划，再写最小实现。不要顺手改无关文件。

任务切片：【填写任务】
```

## Template 5: 测试审计

```
请执行 /test。请检查当前修改是否有足够测试覆盖，包括单元测试、集成测试、
端到端测试、边界条件、失败路径和回归风险。
不得声称测试通过，除非实际运行并给出日志。
```

## Template 6: 代码审查

```
请执行 /review，并调用 code-reviewer。请从可读性、可维护性、架构一致性、
性能、错误处理、API 设计和回归风险角度审查以下 diff。
不要直接修改代码，先输出审查意见。

Diff：【粘贴 diff】
```

## Template 7: 代码简化

```
请执行 /code-simplify。请检查以下代码是否存在过度抽象、重复逻辑、
命名混乱、无用配置、过多状态或复杂分支。
请先输出简化计划，不要直接大改。

代码：【粘贴代码或文件路径】
```

## Template 8: 上线前 ship 审查

```
请执行 /ship，但不得自动部署。请同时调用 code-reviewer、test-engineer
和 security-auditor，对当前变更进行上线前审查，并输出 go / no-go 决策、
阻塞问题、非阻塞问题和必须补充的测试。
```

## Template 9: 安全审计

```
请调用 security-auditor。请检查当前代码或设计是否存在认证授权、
输入校验、敏感信息泄露、依赖风险、注入、权限越界、日志泄露和数据隐私问题。
不要自动修改代码，先输出风险报告。
```

## Template 10: 与 Matt Pocock skills 联合使用

```
请先使用 grill-me 拷问需求，再执行 /spec 和 /plan。
目标是避免一开始就写代码。请把确认后的术语写入 CONTEXT.md 草稿，
把关键设计决策写入 ADR 草稿。不要实现代码。
```
