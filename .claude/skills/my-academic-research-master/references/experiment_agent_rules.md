# Experiment Agent Rules

**文件:** `references/experiment_agent_rules.md`
**用途:** 只有在需要跑深度学习实验时才启用此模块。

---

## 激活条件（全部必须满足才启用）

- [ ] 用户明确要跑真实代码实验
- [ ] 已有可用数据集
- [ ] 已有 baseline 方法/模型
- [ ] 有 GPU 或可用计算环境
- [ ] 有明确评价指标
- [ ] 能保存日志和模型权重

---

## 实验循环

```
每轮实验:
  1. THINK: 阅读 PROJECT_BRIEF.md + 历史实验日志
  2. PLAN: 确定本轮 hypothesis + config
  3. EXECUTE: 修改代码/配置，启动训练
  4. MONITOR: 零成本监控 (kill -0 + nvidia-smi)
  5. REFLECT: 分析结果，记录日志
  6. 决定: PROCEED / REFINE / PIVOT
```

## 禁止行为

1. 不得把失败实验删除
2. 不得只报告好看的结果
3. 不得用 AI 编造曲线
4. 不得用 AI 编造消融实验
5. 不得把未完成实验写进论文结果
6. 不得修改种子只报告最好结果
7. 不得声称"实验表明"但实际没有运行

## 日志要求

```
experiments/
  exp_001/
    config.yaml        # 配置
    hypothesis.md      # 假设
    run.sh             # 执行脚本
    stdout.log         # 标准输出
    metrics.json       # 指标数据
    summary.md         # 结果摘要
```

## 参考实现

如果需要实验自动化，参考:
- `auto-deep-researcher-24x7` 的 Leader-Worker 架构
- 恒定大小内存 (PROJECT_BRIEF.md 3000字 + MEMORY_LOG.md 2000字)
- 零成本监控 (kill -0 $PID + nvidia-smi)
- 实验账本 (experiments.jsonl)

**安装方式（仅需要时）:**
```bash
git clone https://github.com/Xiangyue-Zhang/auto-deep-researcher-24x7.git external/auto-deep-researcher
pip install -r external/auto-deep-researcher/requirements.txt
```
