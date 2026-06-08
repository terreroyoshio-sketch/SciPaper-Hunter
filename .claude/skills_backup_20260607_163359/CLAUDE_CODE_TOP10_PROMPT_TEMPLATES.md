# Claude Code Top 10 Skills — Prompt Templates

---

## Template 1: 网页执行任务

```
请使用 agent-browser。打开以下网页：【URL】。
请读取页面标题、核心内容和关键链接。
不要登录，不要提交表单，不要绕过验证码。
输出摘要、来源 URL 和可复查证据。
```

## Template 2: 查找合适 skill

```
请使用 find-skills。我的任务是【任务描述】。
请先搜索是否已有可靠 skill 可以完成，不要急着自己写。
请输出候选 skill、来源、安装命令、适用场景和风险。
```

## Template 3: 长文压缩

```
请使用 summarize。请把以下长文本压缩为：
核心结论、关键证据、行动项、风险点和后续问题。
不要扩写，不要编造。
```

## Template 4: 创建新 skill

```
请使用 skill-creator。以下是我反复要做的工作流：
【工作流描述】。
请把它封装为标准 SKILL.md，包含 name、description、
goals、constraints、workflow、input、output、
安全边界和低风险测试。
```

## Template 5: 长任务终端控制

```
请使用 tmux。请为以下长时间任务设计 tmux 会话方案，
包括 session 名称、窗口划分、启动命令、日志路径、
观察命令和停止方式。不要运行破坏性命令。
```

## Template 6: Web App 测试

```
请使用 testing 和 agent-browser。请为以下 Web App
功能生成端到端测试计划，包含用户路径、断言、边界条件、
失败场景和可复现命令。先输出计划，不要直接改代码。
```

## Template 7: README / API 文档

```
请使用 docs。请读取项目结构和已有说明，生成 README
或 API 文档。不得编造不存在的功能。请标注需要开发者
确认的部分。
```

## Template 8: 代码重构

```
请使用 refactor。请先识别代码坏味道、重复逻辑、命名
问题和复杂度风险。先输出重构计划和测试策略，不要直接
大规模改代码。
```

## Template 9: Git 交付说明

```
请使用 git-workflow。请基于 diff 生成 commit message、
PR 描述和 changelog。不要执行 git push、reset、clean
或删除分支。
```

## Template 10: 技术调研

```
请使用 research。请围绕【主题】检索公开资料，比较
不同方案，输出来源、优缺点、适用场景和风险。
不得编造来源。
```
