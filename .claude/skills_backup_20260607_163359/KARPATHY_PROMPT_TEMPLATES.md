# Karpathy Guidelines — 提示词模板

---

## 模板 1：代码修改前审计

```
请使用 karpathy-guidelines 和 using-superpowers。
先复述任务目标、边界、风险和验收标准，再检查现有代码。
只提出最小修改计划，不要立刻大范围重构。
```

---

## 模板 2：Bug 修复

```
请使用 karpathy-guidelines。
请先定位最小可复现问题，再写出验证方式。
只修改与 bug 直接相关的文件。修复后运行测试，
不能运行测试时说明原因。
```

---

## 模板 3：项目功能添加

```
请使用 karpathy-guidelines 和 brainstorming。
先给出 2 到 3 个实现方案，选择最简单可维护方案。
不要引入不必要依赖。实现后给出验收检查。
```

---

## 模板 4：Claude Code 提示词扩写

```
请使用 karpathy-guidelines、using-superpowers 和 skill-creator。
把以下粗略任务扩写为完整 Claude Code 提示词，
必须包含目标、边界、输入、输出、步骤、验证标准和失败处理。

[在此处粘贴粗略任务描述]
```

---

## 模板 5：科研代码复现

```
请使用 karpathy-guidelines、markitdown 和 keyword-literature-download。
读取论文和代码仓库，先列出复现目标、环境、数据、指标和最小运行路径。
不要先大改代码。
```

---

## 模板 6：论文项目代码质量检查

```
请使用 karpathy-guidelines 和 reviewer-red-team-auditor。
检查以下项目代码是否存在过度工程、无关重构、硬编码路径、
不可复现、缺少日志、缺少测试等问题。
```

---

## 模板 7：项目申报书相关代码或工具开发

```
请使用 karpathy-guidelines、nsfc-proposal-architecture-pipeline 和
objective-innovation-auditor-pipeline。
开发前先确认工具服务于哪个研究目标和验收标准，
避免做成炫技功能。
```
