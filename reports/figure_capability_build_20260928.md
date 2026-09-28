# 科研制图能力体系建设报告

- 日期：2026-09-28 · 分支：`claude/jolly-austin-91e98e` · 基线 HEAD：`f65b117a`（本轮**未 commit、未推送**）
- 执行方式：只读审计 → 能力地图 → 参考图分类 → GitHub 审计 → 缺口分析 → Skill 最小实现 → benchmark → QA → 报告（连续执行，未跳过阶段）
- 状态：**BUILD_COMPLETE → 待人工验收**；两项安装请求待授权；docx 补丁与注册表更新待确认

## 1. 交付物对照（任务清单 18 项）

| # | 要求 | 产物 | 状态 |
|---|---|---|---|
| 1 | 现有能力地图 | `reports/existing_figure_capabilities.md` | ✓ |
| 2 | 参考图分类目录 | `references/figure_style_catalog.md`（含修正版方框规则 §3） | ✓ |
| 3 | GitHub 审计 | `references/github_visualization_audit.md`（14+6 仓库） | ✓ |
| 4 | 新增/修改 Skill 清单 | §2 下表（11 新增 + 1 扩展） | ✓ |
| 5 | renderer decision tree | `scientific-figure-router/SKILL.md` | ✓ |
| 6 | figure primitives | 复用 `trd_kit.py` + 新增 `figure_qa.py`（通用验收） | ✓ |
| 7 | benchmark 源码 | `benchmarks/figure_families/`（14 文件，全合成数据+固定种子） | ✓ |
| 8–11 | PDF/PNG/缩印/灰度 | 每图 5 产物（pdf/svg/png/grayscale/print89mm） | ✓ |
| 12 | Figure QA report | 每图 `*_gate.md/.json` + `out/summary.md` + `out/contact_sheet.png` | ✓ |
| 13 | 运行命令与输出 | §5 | ✓ |
| 14 | 测试输出 | §3/§4 | ✓ |
| 15 | Git diff | §7（未提交） | ✓ |
| 16 | 未解决风险 | §6 | ✓ |

## 2. Skill 清单

**新增 11（本项目级 `.claude/skills/`，已注册生效）**：
`scientific-figure-router`（总路由）· `figure-quality-gate`（统一验收门 + `scripts/figure_qa.py`）· `scientific-method-framework` · `scientific-flowchart` · `mechanism-schematic` · `graphical-abstract` · `geospatial-figure` · `network-topology` · `engineering-schematic` · `scientific-3d` · `multipanel-compositor`

**扩展 1**：`technical-route-diagram`（写入 2026-09-28 修正版方框规则 + 路由/门禁衔接）

**不新建（按"优先扩展"路由到现有）**：technical-roadmap → technical-route-diagram；publication-data-plot → figurelab-publish / academic-figure-skill / scientific-visualization；statistical-figure → seaborn / matplotlib。

**"方框+箭头"绝对规则修正（三处落地）**：
1. 新技能与目录文档（`figure_style_catalog.md` §3）写入修正版规则；
2. 自动记忆 `figure_qa_protocol_advantages` 第 8 条已改（原绝对禁令废除，改分场景建议）；
3. 你的《制图提示词.docx》（源头 §17/18/22/44/52/54）**未动原件**——补丁副本待你确认后生成（不覆盖原件）。

## 3. Benchmark 结果（12 项，全部合成数据）

| key | 家族 | 状态 | 产物 |
|---|---|---|---|
| b01 | 数据图：时序+散点 | **PASS** | pdf/svg/png/灰度/缩印/gate |
| b02 | 统计图：分布三面板 | **PASS** | 同上 |
| b03 | 统计图：相关热力图 | **PASS** | 同上 |
| b04 | 方法框架（trd_kit） | **PASS** | 同上 |
| b05 | 技术路线图（trd_kit） | **PASS** | 同上 |
| b06 | 算法流程图（dot 布局→自绘） | **PASS** | 同上 |
| b07 | 机制示意图 | **PASS** | 同上 |
| b08 | GIS choropleth（geopandas） | **PASS** | 同上 |
| b09 | 网络图（networkx） | **PASS** | 同上 |
| b10 | 电路图（schemdraw） | **PASS** | 同上 |
| b11 | 多面板复合 2×3 | **PASS** | 同上 |
| b12 | 3D（mplot3d 兜底） | **PASS_WITH_LIMITATION**（2 个 3D 文字坐标不可测→目检强制） | 同上 |

- 每图均带可见 `BENCHMARK - synthetic data (not real research)` 标记；无可复现性隐患（固定种子）。
- 拼版总览：`benchmarks/figure_families/out/contact_sheet.png`

## 4. Gate 有效性证据（本轮抓到的真实缺陷，均已修复）

自动检查抓住的真问题（**其中 2 条是目检先发现、另 1 条自动抓到但初始修法不够、目检二次抓出**）：

1. b01 xlabel 与页脚标记重叠 → 标记移位
2. b03 colorbar 刻度与轴标签越界 → 右边距 0.99→0.88
3. b04 图例文字与页脚标记重叠 → 布局修正
4. b05 `\le` mathtext 解析失败（真错误）→ `\leq`
5. b07 顶部两条注释互压 → 移位
6. b08 来源注记越界且压 xlabel → 移入图内
7. b09 节点标签互撞 → 贪心避让
8. b11 面板标签与标记冲突、colorbar 压相邻 ylabel → 边距/间距
9. b12 z 轴标签压刻度 → labelpad（**目检 + gate 双确认**）
10. b05/全部图"贴边截字"（测量在界内、渲染裁尾字符）→ **目检发现**，留 1.5% 边距

伪影三类（已加结构性护栏，防误报）：`axis("off")`/视野外刻度的幽灵文字对象（无 `.axes` 属性，需按轴枚举识别）、mplot3d 投影坐标不可测、重复绘制对象。

## 5. 运行命令与测试输出（可复算）

```bash
# 全量（12 图 → 每图 7 产物 + contact sheet + summary）
python benchmarks/figure_families/run_all.py            # EXIT=0，11 PASS + 1 PASS_WITH_LIMITATION
# 子集
python benchmarks/figure_families/run_all.py --only b04 b05
# 单图过门（任意暴露 build() 的模块）
python .claude/skills/figure-quality-gate/scripts/figure_qa.py --builder <module.py> --out <dir>
```
目检记录：contact sheet 全览 1 次 + 单图 6 张（b01/b02/b04/b05/b12 + 修复前后对照），共 3 轮"发现→修复→重验"迭代。

## 6. 未解决风险与限制

1. **自动检查为启发式**：贴边裁剪（渲染宽度略大于测量）无法 100% 自动；箭头压字/数据遮挡为已知盲区 → 目检强制（已写入 SKILL.md）。
2. **3D 文字不可测**（mplot3d 投影）→ 以目检为准；根治需 pyvista。
3. **cartopy 未装** → GIS 无真实海岸线底图/经纬网工具；投影地图可用 `.to_crs(投影CRS)` 变通（b08 已证）。
4. **docx 补丁未生成**（不覆盖原件，待确认）；主仓库 `research-stack-index` 注册表未更新（属另一检出，待确认）。
5. **未 commit/推送**；`benchmarks/out/` 含二进制产物（约几 MB），提交策略待定（建议源码与产物分开决定）。
6. 无许可参考包（sci-box / research-drawio-skill）仅提取模式、未复制代码；《制图提示词》修订副本尚未与 docx 对齐。

## 7. 待授权清单（安装请求，按规范格式）

| 包 | 现状 | 请求 | 原因/收益 | 风险 | Windows | 回滚 |
|---|---|---|---|---|---|---|
| **cartopy** | 未装 | 按 pip 最新兼容版 | 真实地图投影/底图/经纬网（GIS 箭头家族缺口） | 依赖 GEOS/PROJ——本机 geopandas/pyproj 链路已在，风险低 | 有官方 wheel | `pip uninstall cartopy`（不影响现有链路） |
| **pyvista** | 未装 | 按 pip 最新兼容版 | 3D mesh/volume/headless（scientific-3d 首选） | 依赖 VTK（体积大，~百 MB 级），安装耗时；纯新增不影响现有环境 | 有官方 wheel | `pip uninstall pyvista vtk` |

OPTIONAL（不请求，思想已吸收）：plotnine / adjustText / pytest-mpl / SciencePlots。

## 8. 验收自查（对照任务验收标准）

- [x] GitHub 来源真实（API + raw LICENSE 逐条核验）；许可记录完整
- [x] 未伪造 MCP 调用（本轮仅用 WebFetch/WebSearch/本地工具）
- [x] 未伪造测试结果（全部命令与输出见 §5，退出码可复算）
- [x] 未修改原始科研数据；未动主仓库与用户级技能
- [x] 不同 Figure 类型有明确路由（router 表 + decision tree）
- [x] 技术路线图能力独立（technical-route-diagram 扩展）
- [x] 流程图不再被绝对限制（规则修正三处）
- [x] Graphviz 只算布局（b06 管线：dot -Tplain → 自绘）
- [x] 矢量 PDF / 单栏缩印（print89mm）/ 灰度 / 无文本遮挡（12/12）
- [x] benchmark 可重复生成（固定种子 + 单一入口命令）
- [ ] Git diff 人工复核 —— **待你复核**（本轮不 commit）
- [ ] 两项安装授权 —— **已完成（见 §9）**

## 9. 后续更新（2026-09-28，授权后执行）

- **cartopy 0.26.0 / pyvista 0.49.0（+VTK 9.7.0）已安装**并冒烟测试通过：cartopy Robinson 投影 + gridlines 渲染 ✓；pyvista off-screen 球体渲染 ✓（产物在 `outputs/install_smoke_20260928/`）。相关 SKILL.md（`geospatial-figure` / `scientific-3d` / `scientific-figure-router`）的"未装"状态已同步为已装。
- **docx 补丁副本已生成**：`C:\Users\张涵\Desktop\制图提示词.patched_20260928.docx`（17 处变更、0 未命中：技能列表同步 + §17/§18/§52/§54 规则修正 + 文档头修订说明）；变更明细 `reports/docx_patch_log_20260928.md`；复现脚本 `reports/docx_patch_20260928.py`；**源文件 SHA-256 前后一致**（`df979a4f…`，原件零改动）。
- 仍未做：commit（本轮未授权）；主仓库 `research-stack-index` 注册表更新（待确认）。
