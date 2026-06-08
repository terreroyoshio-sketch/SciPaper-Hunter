# /redteam — 审稿人攻击

## 用途
启动 academic-paper-reviewer 和 reviewer-red-team-auditor 进行严格审稿模拟。

## 调用流程

1. **加载论文** — 读取当前稿件的完整内容
2. **学术评审** — 使用 academic-paper-reviewer 多角度评审
3. **红队攻击** — 使用 reviewer-red-team-auditor 寻找漏洞
4. **分类输出** — 按严重程度分类

## 输出分类

| 级别 | 定义 | 处理方式 |
|------|------|---------|
| 🔴 致命缺陷 | 设计错误、数据造假、结论不成立 | 必须修复或放弃 |
| 🟠 重大缺陷 | 方法不当、样本不足、分析错误 | 必须修复 |
| 🟡 可修改缺陷 | 表述不清、缺少引用、图表问题 | 建议修复 |
| 🟢 补救方案 | 具体修改建议 | 参考执行 |

## 硬性约束

- ❌ 不写鼓励性总结
- ❌ 不给虚假安全感
- ❌ AI 模拟审稿不得写成真实审稿（必须标注 REVIEW_SIMULATION）
- ❌ 不编造审稿人身份
- ❌ 不编造审稿意见

## 前置条件

- [ ] 论文完整稿已就绪
- [ ] 引用核查已通过
- [ ] 反造假检查已通过

## 输出

```
reports/redteam/
├── fatal_defects.md
├── major_defects.md
├── minor_defects.md
├── remediation_plan.md
└── go_no_go.md                # 是否适合继续推进
```

## 依赖 Skills

- academic-paper-reviewer
- reviewer-red-team-auditor
