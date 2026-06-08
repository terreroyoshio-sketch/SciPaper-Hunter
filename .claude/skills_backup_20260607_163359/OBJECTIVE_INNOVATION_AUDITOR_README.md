# 创新点客观审计流水线 Skills — 总说明

## 一、背景

本组 skills 的核心目标：让 Claude Code 在写论文创新点、基金申请书创新性说明、项目申报书创新之处、SCI Cover Letter、答辩材料时，能够基于用户提供的**原始数据、实验结果、对比文献和项目材料**进行客观审计，**避免虚假创新、表面创新、夸大创新和证据不足的创新主张**。

**核心禁止：禁止 AI 凭空构思创新点。所有创新主张必须有数据支撑。**

---

## 二、新增 Skills 清单

| 序号 | 文件夹名称 | 用途 | 输入 | 输出 |
|------|-----------|------|------|------|
| 1 | `surface-innovation-auditor` | 表面创新审查，驳回低强度主张 | 创新点草稿 + 结果 | 被驳回的主张 + 需补充证据 |
| 2 | `theoretical-paradigm-extractor` | 理论范式提炼 | 研究结果 + 讨论 | 理论贡献类型 + 表述 |
| 3 | `methodological-breakthrough-quantifier` | 方法学突破量化 | 新方法 + 基准数据 | Δ指标表 + 量化陈述 |
| 4 | `translation-application-anchor` | 转化应用价值锚定 | 结论 + 应用场景 | 应用价值 + 转化路径 |
| 5 | `interdisciplinary-fusion-auditor` | 跨学科融合审计 | 领域AB方法 + 结果 | 融合价值 + 拼接风险 |
| 6 | `benchmark-comparison-defender` | 基准对比与防御 | 创新主张 + 对比论文 | 对比表 + 可防御陈述 |
| 7 | `generality-extension-mapper` | 普适性与外延价值 | 研究发现 + 验证场景 | 外延价值 + 边界约束 |
| 8 | `hype-language-cleaner` | 夸大词汇净化 | 创新点文本 | 净化后文本 + 删除清单 |
| 9 | `three-point-innovation-packager` | 三点式创新封装 | 理论/方法/应用主张 | 三点式列表 + 证据提示 |
| 10 | `reviewer-red-team-auditor` | 审稿人红队审查 | 三点式创新点 | 漏洞报告 + 风险等级 |
| 11 | `objective-innovation-auditor-pipeline` | 完整审计流水线 | 全部原始材料 | 最终创新点 + 风险报告 |

---

## 三、流水线调用流程

调用 `objective-innovation-auditor-pipeline` 时，自动依次执行：

```
  Step  1: surface-innovation-auditor      → 剔除表面创新
  Step  2: theoretical-paradigm-extractor  → 理论贡献提炼
  Step  3: methodological-breakthrough-quantifier → 方法学量化
  Step  4: translation-application-anchor  → 应用价值锚定
  Step  5: interdisciplinary-fusion-auditor → 跨学科审计
  Step  6: benchmark-comparison-defender   → 基准对比防御
  Step  7: generality-extension-mapper     → 外延价值评估
  Step  8: hype-language-cleaner           → 语言净化
  Step  9: three-point-innovation-packager → 三点式封装
  Step 10: reviewer-red-team-auditor       → 红队检验
```

---

## 四、为什么不能让 AI 凭空写创新点

直接要求 AI"写出本研究的三个创新点"会触发以下风险：

| 风险 | 后果 |
|------|------|
| 虚构创新点 | 生成不存在的理论贡献或性能提升 |
| 夸大差异 | 把微小改进包装成"重大突破" |
| 虚构对比 | 编造不存在的文献对比 |
| 杜撰数据 | 编造不存在的性能指标 |
| 表面创新 | 把"首次将 A 用于 B"包装成创新 |
| 套话堆砌 | 使用"填补国内空白""达到国际先进水平"等空话 |

**正确的做法**：
1. 先完成实验和数据验证。
2. 整理原始创新点草稿。
3. 使用本组 skills 进行客观审计和提炼。

---

## 五、为什么"据我们所知，本研究首次……"通常有风险

1. **无法验证** — AI 不可能真正知道是否"首次"。
2. **容易被审稿人驳回** — 审稿人可能立即举出反例。
3. **可用更准确的表述替代**：改为"据现有文献检索结果，尚未发现……"

---

## 六、为什么样本量更大、测试场景更多、方法简单迁移通常不足以构成强创新

- **样本量更大**：只是量变，不是质变。审稿人会问"更大样本量是否带来了新发现？"
- **测试场景更多**：算力或资源的堆砌，不是方法论创新。
- **把方法 A 用到领域 B**（无实质改造）：学科拼接不是创新，除非解决了领域 A 的核心盲区。

本组 skills 中的 `surface-innovation-auditor` 会直接驳回这类主张，要求你补充机制价值、理论意义或实际应用证据。

---

## 七、与已有 Skills 的组合方式

### A. 写基金申请书创新点时

```
1. using-superpowers                   → 确认申请类型、学科口径、评审标准
2. brainstorming                        → 初步梳理创新方向（不直接定稿）
3. literature-review-closed-loop-pipeline → 判断现有范式、争议和空白
4. objective-innovation-auditor-pipeline  → 基于原始数据和对比文献审计创新点
5. hype-language-cleaner                → 删除夸张表达
6. reviewer-red-team-auditor            → 模拟基金评审质疑
```

### B. 写 SCI 论文 Cover Letter 时

```
1. literature-boundary-lock            → 锁定对比文献边界
2. benchmark-comparison-defender        → 写与现有代表性工作的客观差异
3. three-point-innovation-packager      → 封装为三条贡献
4. disciplinary-tone-auditor            → 调整为克制、客观语气
5. citation-syntax-auditor              → 检查引用句法
```

### C. 写论文讨论部分时

```
1. empirical-result-extraction-auditor  → 从结果中提取真实发现
2. theoretical-paradigm-extractor       → 提炼理论或机制贡献
3. generality-extension-mapper           → 谨慎扩展外延意义
4. hype-language-cleaner                 → 避免过度解释
```

### D. 写项目申报书创新之处时

```
1. research-gap-synthesizer             → 从不足推出项目必要性
2. methodological-breakthrough-quantifier → 量化技术方案优势
3. translation-application-anchor       → 锚定工程或产业应用价值
4. three-point-innovation-packager      → 整理成三点式创新
```

### E. 写提示词时

以后在生成 Claude Code 提示词时，优先综合调用：
- using-superpowers
- brainstorming
- keyword-literature-download
- markitdown
- academic-abstract-pipeline
- literature-review-closed-loop-pipeline
- objective-innovation-auditor-pipeline
- reviewer-red-team-auditor
- hype-language-cleaner

---

## 八、安全性说明

1. 所有 skills 均为本地 SKILL.md 文件，不执行代码。
2. 不连接外部网络或 API。
3. 不修改系统级配置。
4. 不读取或写入用户文件以外的数据。
5. 原始 skills 已在安装前备份到 `skills_backup_objective_auditor_*`。

---

## 九、维护说明

- 编辑对应文件夹下的 `SKILL.md` 即可修改 skill。
- 修改后无需重启 Claude Code，下次调用自动载入最新版本。
- 删除对应文件夹即可移除不需要的 skill。
- 不要删除旧 skills 或覆盖其他用户的 skills。
