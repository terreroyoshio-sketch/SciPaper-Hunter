# Experiment Integrity Rules

**文件:** `references/experiment_integrity_rules.md`
**用途:** 只有涉及真实代码/实验的论文才启用。

---

## 激活条件

以下条件全部满足时才启用实验模块:
1. 用户明确要跑真实代码实验
2. 已有可用数据集
3. 已有 baseline 方法
4. 有 GPU 或可用计算环境
5. 有明确评价指标
6. 能保存日志和模型权重

## 核心规则

1. **每轮实验必须有 hypothesis**
2. **每轮实验必须有 config 记录**
3. **每轮实验必须有日志** (stdout + stderr + metrics)
4. **每轮实验必须有指标记录** (loss, accuracy, etc.)
5. **每轮实验必须保存失败原因**
6. **不得把失败实验删除** — 失败也是有效结果
7. **不得只报告好看的结果** — 必须报告全部结果
8. **不得用 AI 编造曲线** — 图表必须来自真实日志
9. **不得用 AI 编造消融实验** — 必须真实运行
10. **不得把未完成实验写进论文结果**

## 实验日志格式

```
experiments/
  exp_001/
    config.yaml
    run.sh
    stdout.log
    stderr.log
    metrics.json
    summary.md
  exp_002/
    ...
```

## 禁止行为

- ❌ 用 GPT 生成"假"实验结果
- ❌ 修改种子只报告最好结果
- ❌ 删除失败的实验记录
- ❌ 声称"实验表明"但实际没有运行
- ❌ 用 AI 画不存在的数据点
