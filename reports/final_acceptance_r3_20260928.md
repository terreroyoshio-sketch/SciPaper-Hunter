# 独立验收记录 — 视觉质量升级批次 r3（Final Acceptance Record）

2026-09-28 · 验收方：独立 final-acceptance-reviewer（无实现过程上下文，独立复算，不采信实现者自报）
**总评：ACCEPT（功能声称全过；2 个文档级条件已关闭；重新冻结自洽）**
本记录为**冻结后**产物（不在 r3 patch / r3 zip 内，避免自引用）。

---

## 1. 流程

```
实现者冻结 r3（patch + manifest + ZIP）
→ 独立验收（9 项声称全量复核，含重跑三套基准）        → CONDITIONAL_ACCEPT（2 文档条件）
→ 修复 2 条件 + 重新冻结（清单刷新/ZIP 重建）          → 聚焦复验（7 项）→ 无新不一致 → ACCEPT
```

## 2. 第一轮全量复核（9 声称）

| # | 声称 | 判定 | 复核要点 |
|---|---|---|---|
| 1 | 图件 14/14（13 PASS + 1 PWM b12） | CONFIRMED | 重跑 run_all.py exit 0，判决与冻结 summary 一致 |
| 2 | T 套件 7/7 预期命中 | CONFIRMED | **对抗性反驳失败**：before 为真实构造重叠；after 保留全部标签与锚点、仅小幅偏移+引线（无删除/荒谬远移）；annotate 经 `Text` 计测非盲区 |
| 3 | TABLE 5/5，center_error ≤0.02mm | CONFIRMED | soffice headless 真实渲染链；TABLE05 两页 header_repeat=true |
| 4 | pytest 7/7 | CONFIRMED | 断言真实（fail-closed、8pt、无误报用例） |
| 5 | 字体 smoke 双断言 | CONFIRMED | clean/植入缺字两探针均来自真实 draw，**非写死返回值** |
| 6 | 清单 174 文件 0 空 0 缺 | CONFIRMED | 重跑前逐行 0 差异（复验 CSV 在包内） |
| 7 | ZIP 冻结自洽 | CONFIRMED | 整包 sha256、CRC、manifest 覆盖、patch 260 头 |
| 8 | 约束遵守 | (a)(c)(d) CONFIRMED；(b) **REFUTED→已更正** | (b) 实现者交底基线哈希笔误（写 3bf37c79，实为 HEAD=f65b117a，前者是父提交）；"本批次零 commit"不变量成立 |
| 9 | 对抗性抽查 | CONFIRMED | 无"静默零路径"（引擎异常显式报 limitation 并置空 counts 而非 0）；text_image 仅报边界越界（LIMITATION 设计属实） |

## 3. 条件项与关闭

| 条件 | 问题 | 修复 | 复验 |
|---|---|---|---|
| A | `README_PACKAGE_R3.md` 残留陈旧句"未达成文件级读取（403/404）" | 改为"已文件级读取"+基线声明（HEAD=f65b117a / 零 commit / 0 staged / FINAL_EVIDENCE_FREEZE 属更早批次） | CONFIRMED（工作区与 zip 内字节一致） |
| B | 参考矩阵分级段 2 处文件名简写（defaults-mystyle、rules-helper） | 全 10 条改精确相对路径（`defaults/mystyle.txt`、`rules/helper.py` 等） | CONFIRMED（zip 内 13/13 命中；磁盘实查 13/13 EXISTS） |

## 4. 重新冻结事实（验收后）

| 项 | 值 |
|---|---|
| `桌面\figure_evidence_package_20260928_r3.zip` | **sha256 `0c5d113416b89c60bf282be78d8092691123c363292ebeee68418f83645fb3c1`**（202 文件 + manifest；CRC 全过、双向 0 失配） |
| `reports/final_git_diff_r3.patch` | 260 文件 / sha256 `78da9dff…`；排除清单含验收类快照；0 个禁用 diff 头 |
| 产物清单 | 刷新为**重跑后态**（与工作区一致）；重跑前态完整保留于 `reports/acceptance_recheck_r3_20260928.csv`（在包内） |
| 重跑语义 | 独立验收重跑全部基准后：恰 **53 个日期内嵌文件**字节变化（27 pdf / 21 svg / 5 docx）；**全部 png/json/md 字节稳定**（判决级证据不变） |
| 基线 | HEAD=f65b117a；0 staged；树 dirty；本批次**零 commit** |

## 5. 验收覆盖边界（未验证清单，照录）

- 图件的科学语义与数据真实性（benchmark 明示为合成数据）；
- references/reports 全文逐字准确性（抽验关键段）；
- zip 其余约 180 个文件逐字节比对（抽验 18 个关键文件，全一致）；
- 未安装包（adjustText/SciencePlots/great-tables）的行为；其他 surface / 模型路由下的表现。

## 6. 结论与下一步

- 独立验收结论：**ACCEPT**（无条件关闭后无新不一致）。
- 仍待人工：用户侧外部验收（可选）→ 授权 commit（当前未 commit / 未 push / 未更新 registry）。
- 已知非阻断限制照旧：text_image=LIMITATION、b12 3D 文本目检兜底、渲染链依赖本机 LibreOffice。
