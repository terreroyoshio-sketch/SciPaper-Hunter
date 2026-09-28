# 纠正批次报告 — 2026-09-28（对应独立审查 `FAIL — CORRECTIVE PATCH REQUIRED` 的 7 项）

- **总体状态：`CORRECTIVE PASS COMPLETE` → 待重新独立验收**（未 commit、未 push、未更新 registry）
- 基线：HEAD `f65b117a` 未变 · 分支 `claude/jolly-austin-91e98e`
- 范围：仅修正审查点名的 7 项，**不扩功能**；全部结论附本机实际命令输出
- 关于 r1 包：`figure_evidence_package_20260928.zip` 已不在 Desktop/Downloads（已被取走审查）→ 本批 delta **无法与 r1 manifest 做哈希直比**；替代核验 = 本轮编辑记录 + **r2 全量 patch**（`final_git_diff_r2.patch`，可独立 diff 出全部修改）

---

## C1 · pdf_check 修复（fail-closed + 真回归测试）— `PASS`

**三个根因（第 3 个为修复过程中新发现）**
1. `for _, df in (fo.get("/DescendantFonts") or [])` 对 pypdf 引用对象错误解包 → `too many values to unpack (expected 2)`（审查所报）。已改为 `for df in (...)` 正确遍历。
2. 字体探测异常被静默忽略（fail-open）。已改 **fail-closed**：parser 错误 / font-entry 错误一律进入 `fails`（`font_errors` 字段随报告输出）。
3. **新发现**：matplotlib 默认 `pdf.fonttype=3` 生成 **Type3 字体**（字形程序内联于 `/CharProcs`，无 `/FontFile*`），旧检测误判"未嵌入"。已特判 `Type3 → embedded`；报告新增 `subtype` 字段。同时：非嵌入字体（Base14 除外）由 LIMITATION 升为 **FAIL**；Base14 保留 LIMITATION。

**回归测试**（新增 `figure-quality-gate/scripts/test_figure_qa.py`）：覆盖 Type3 与 TrueType42 双模式 PDF、坏文件 fail-closed、monkeypatch 驱动 `run_gate` 必须 FAIL、图例冲突检出/空角不误报、均衡检出、8pt 阈值强制。

```
$ python -m pytest test_figure_qa.py -q
.......                                                                  [100%]
7 passed in 2.56s
```

## C2 · 恢复 SCI 默认 8 pt（单一来源 + venue override）— `PASS`

- **单一来源**：`figure_qa.DEFAULT_MIN_PT = 8.0`；报告新增 `threshold_source`（`default-SCI-8pt` / `override`）。
- 已同步：`figure-quality-gate/SKILL.md` 阈值表；`scientific-figure-router` 硬规则 3；`scientific-method-framework`；`technical-route-diagram` 规则 5；`qa_layout.MIN_FONT_FAIL = 8.0`；benchmark runner 传参 `bc.DEFAULT_MIN_PT`。
- trd 模板与基元库（`trd_kit`）默认字号全部 ≥8 pt；**并顺带把模板的溢出检查从字符宽度启发式升级为真实渲染度量**（`qa_layout._make_line_counter`，用 renderer 实测换行）。
- 14 个 benchmark 全部在 8 pt 下重渲过门，**全部 `threshold_source=default-SCI-8pt`**（无 override 使用）；venue override 机制 = 显式 `--min-pt` + 报告记录依据。

## C3 · 补齐四项 QA 真检查（含修前 FAIL → 修后 PASS 回归）— `PASS`

**新增实现（`figure_qa.py`）**
| 检查 | 实现要点 |
|---|---|
| legend-data overlap | 图例框（缩 4%）内落入的不透明数据点：collection ≥5 点且占比 ≥2%，或 line ≥8 点；`alpha<0.5` 的半透明填充不计（防误差带误报） |
| clipping / 边距 | margin 检查：文字/图例距画布边 <0.5 mm → FAIL，<1.5 mm → LIMITATION；图例越界（负 margin）→ FAIL；与越界检查并列 |
| layout balance | 单轴数据点全幅/核心(5–95%)面积比 >4 → FAIL（稀疏外围/核心压缩）；3D 轴跳过 |

**回归证据（修改前，逐字）**
```
b08 | legend_conflicts = [{'ax': 0, 'points_collection': 10, 'points_line': 0, 'frac_of_sampled': 0.083}]   → FAIL
b09 | balance_issues   = [{'ax': 0, 'extent_ratio': 5.83, 'points': 171}]                                  → FAIL
```
**修复后**：b08 图例移至轴外右侧；b09 改 `kamada_kawai_layout`（确定性紧凑布局）→ 两项检查均归零（见 C7 终表）。未覆盖项仍如实标注为目检项（箭头压字/数据遮挡）与 3D LIMITATION。

## C4 · Benchmark 覆盖与缺陷修复 — `PASS`

1. **新增 b13（图形摘要）** —— 场景（几何山/树/太阳）+ 流程列 + 结果小图内嵌（复用 trd_kit）。**覆盖口径修正**：由"12 bench / 11 家族"改为 **14 bench / 12 家族全覆盖**。
2. **新增 b14（PyVista 主路径）** —— off-screen 渲染（`screenshot(return_img=True, scale=2)`）→ matplotlib 复合（8pt 标签+色条）→ 完整过 gate；b12 保留为 **mplot3d 兜底路径**并更新标记文本（"3D fallback path: mplot3d"）。
3. **PyVista API 表述按 0.49.0 运行时实测修正**：`screenshot` 签名**确实含 `scale` 参数**（introspect 核验）；`Plotter.image_scale` 是**属性**（非方法）；`save_graphic()` 存在 → `scientific-3d/SKILL.md` 已按实测改写并注明。
4. **b06**：G→D 回流边改**虚线**（回流虚线语义）；节点/层间距增至 0.45/0.55。
5. **b08**：图例移出地图（轴外右侧，"Quantile classes"）——legend-data 归零。
6. **b09**：KK 紧凑布局——balance 归零。
7. **b10**：`.tox(0)` 闭合回路 → **完整 RC 低通电路**（源-阻-节点-电容-底轨闭环；全尺寸目检确认，不再是 fragment 表述）。
8. 目检：统一格子 contact sheet（14 图）+ b10/b13/b14/trd demo 全尺寸目检。

## C5 · 补视觉学习证据（reference → family）— `PASS`（分层如实）

- 新增 `references/reference_family_mapping.md`：**19 类参考图全覆盖**（含审查点名的 GA、生态机制、多尺度路线、GIS+模型混合）。
- 证据分级：**4 类 SESSION-VISIBLE**（本会话直接分析）· 1 类 partial · **15 类 USER-LISTED**（图像本体不可见；结构要点按类型范式记录并标注"待图像核验"）——**不冒充已见**；升级路径（提供图像→升级核验）已写明。

## C6 · 证据一致性清理 — `PASS`

- `github_visualization_audit.md`：加 **`PRE-INSTALL AUDIT SNAPSHOT`** 头注 + 文末追加安装后状态（正文快照原样保留，消除"两个当前状态"矛盾）。
- ZIP 打包器：**README 纳入 manifest**（r2 包 `PACKAGE_MANIFEST.sha256` 覆盖 README_R2，仅自身除外并注明）。
- contact sheet：统一 letterbox 格子（540×700），消除纵横比空白。
- `__pycache__`：先 `git check-ignore` 取证（`.gitignore:2:__pycache__/`）→ 删除 3 个 `.pyc` / 2 个目录（现为 0）；未重跑全量 benchmark。

## C7 · 重新冻结 — `PASS`

```text
$ git rev-parse --short HEAD          → f65b117a
$ git status --porcelain | wc -l      → 32   （其中 M=9：trd 5 个源码/模板文件 + demo 4 个二进制输出）
$ git diff --stat（含 intent-to-add） → 148 files changed, 84253 insertions(+), 318 deletions(-)
$ python -m pytest test_figure_qa.py  → 7 passed
```
- **r2 patch**：`reports/final_git_diff_r2.patch` — **86,182 行 / 3,124,316 B / sha256 `645e8fe327c6da15cc7e5918fdabe13547584ed0a80b123fdd1e80584e44507a`**（索引生成后已 `git reset` 还原；工作树未动）。
- **产物核验（14 项，只验证不重画）**：`101/101` 文件（14×7 + contact + summary×2），**0 缺失 / 0 空文件 / 0 重复哈希**；PNG/灰度 = 设计 mm × 600 dpi（±2 px）；print89 宽 2102 px；**全部 margin ≥1.6 mm**；`threshold_source=default-SCI-8pt`（全部）。
- 逐项状态：**13 PASS + 1 PASS_WITH_LIMITATION（b12：2 个 3D 文字包围盒不可测 → 目检强制，已目检）**。
- 新 manifest：`reports/benchmark_artifacts_manifest_r2_20260928.csv`（101 行 path/bytes/sha256）。
- r2 证据包：`C:\Users\张涵\Desktop\figure_evidence_package_20260928_r2.zip`（delta 焦点：变更/新增源码 + 全部 14 份 gate 结果 + 新 contact sheet + 14 预览 + demo 更新 + r2 patch + 本报告 + 哈希清单）。

---

## 14 项终表（verbatim 摘录自核验输出）

```text
b01 PASS  margin=1.606  png=(4015,1417)     b08 PASS  margin=2.0  png=(2881,2220)
b02 PASS  margin=2.0    png=(4015,1370)     b09 PASS  margin=2.0  png=(2881,2267)
b03 PASS  margin=2.0    png=(2834,2409)     b10 PASS  margin=1.951 png=(3840,2880)
b04 PASS  margin=2.0    png=(4015,2456)     b11 PASS  margin=1.969 png=(4015,2551)
b05 PASS  margin=2.0    png=(4015,5102)     b12 PASS_WITH_LIMITATION  png=(2645,2125)
b06 PASS  margin=2.0    png=(2250,4819)     b13 PASS  margin=2.0  png=(4015,2362)
b07 PASS  margin=2.0    png=(3070,2007)     b14 PASS  margin=2.0  png=(3543,2362)
TOTAL out files: 101 (expect 101) | problems: none | dup groups: none
```

## 本批限制（如实，不回避）

1. b12（3D 兜底）2 个文字包围盒不可测（mplot3d 渲染器事实）→ LIMITATION，已目检；b14 为主路径取证。
2. contact sheet 全览目检为缩略级；全尺寸级证据 = 各图 gate（0 overlap）+ 单图目检。
3. 15 类 USER-LISTED 参考图未图像核验（见 C5 表）。
4. r1 包已被取走 → r1→r2 无哈希直比；以 r2 patch 全量 diff 为独立核验基础。
5. 全量 pdf/svg/灰度/缩印产物未入 r2 包（同 r1 理由）。
