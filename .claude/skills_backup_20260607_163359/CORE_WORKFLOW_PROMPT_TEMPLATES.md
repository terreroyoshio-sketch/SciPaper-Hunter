# Core Workflow — 提示词模板

---

## 模板 1：长文总结

```
请使用 summarize 和 markitdown。读取以下文件或目录，
提炼核心观点、结构大纲、关键结论、未解决问题和后续行动项。
不要编造文件中不存在的内容。
```

---

## 模板 2：网页资料检索

```
请使用 research 和 agent-browser。
先明确检索目标、可信来源标准和输出格式，再进行网页检索。
不得绕过登录、验证码、付费墙。对所有事实给出来源链接。
```

---

## 模板 3：Git 安全工作流

```
请使用 git-workflow 和 karpathy-guidelines。
先运行 git status，检查当前分支和未提交修改，
再制定最小变更计划。任何提交、回滚、删除分支、强推操作前
都必须停止并要求人工确认。
```

---

## 模板 4：长任务终端管理

```
请使用 tmux。为以下长任务创建命名 session，
记录启动命令、日志路径、检查命令和停止命令。
不要让任务无记录地后台运行。
```

---

## 模板 5：代码重构

```
请使用 refactor、testing 和 git-workflow。
先建立测试或最小验证方式，再进行小步重构。
不得改变外部行为。每一步说明修改文件、修改原因和验证结果。
```

---

## 模板 6：测试驱动修复

```
请使用 testing、using-superpowers 和 karpathy-guidelines。
先复现 bug，再编写或补充测试，再进行最小修复，
最后运行测试并输出结果。
```

---

## 模板 7：项目文档生成

```
请使用 docs 和 summarize。读取项目 README、源码、配置和脚本，
生成准确的安装说明、使用说明、API 文档和常见问题。
不得记录未实现功能。
```

---

## 模板 8：创建新 Skill

```
请使用 skill-creator。将以下成熟工作流封装为标准 Claude Code skill。
必须包含 name、description、goals、constraints、workflow、input、output 和安全边界。
```

---

## 模板 9：自动寻找 Skills

```
请使用 find-skills。根据以下任务需求，拆解所需能力，
搜索可信 skill 来源，比较候选 skill 的维护情况、安装方式、
许可证和风险，最后给出推荐安装方案。
不要安装高风险或来源不明的 skill。
```

---

## 模板 10：论文申报书综合工作流

```
请综合使用 using-superpowers、brainstorming、keyword-literature-download、
critical-literature-review-pipeline、objective-innovation-auditor-pipeline、
nsfc-proposal-architecture-pipeline、nature-figure、word-document-processor、
docs 和 summarize。
先明确任务边界，再检索文献，构建研究现状，审计创新点，
规划申请书结构，最后输出 Word 文档和图件计划。
```
