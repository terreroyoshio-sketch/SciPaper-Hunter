# figure_evidence_package_20260928_r3 — 视觉质量升级证据包

范围：四项横向能力（scientific-typography / collision-aware-layout / publication-table-layout / visual-aesthetic-critic）+ 基准与表格验证。
未安装任何新依赖 · 未 commit · 未 push · 未更新 registry。工作区保持 dirty，`reports/final_git_diff_r3.patch` 为文本快照。

## 本包内容

| 目录 | 内容 |
|---|---|
| `skills/` | 4 个新 skill 全文 + 被修改的 figure-quality-gate、technical-route-diagram |
| `benchmarks/figure_families/` | b01–b14 全部源码 + out（每图 png + gate.md/json + summary + contact_sheet） |
| `benchmarks/visual_quality/` | T01–T04 源码 + out（before/after 全部图像与 summary；t01_fonts 含 font_smoke_test） |
| `benchmarks/table_family/` | TABLE01–05 构造脚本 + out（docx + pdf + qa.json + table_layout_report.json） |
| `benchmarks/verify_artifacts.py` | 产物核验脚本（存在/零字节/PNG 尺寸/sha256） |
| `outputs/visual_quality_smoke/` | 字体 smoke 的 pdf/png |
| `references/` | 审美规则库、审美参考矩阵（含学习来源分级与 do_not_copy） |
| `reports/` | 升级总报告、审美审查报告、缺口审计 A–P、视觉指标 JSON、产物清单 CSV（现行态）、`acceptance_recheck_r3_20260928.csv`（独立验收在重跑前对该清单的逐行复核，0 差异，同时保留重跑前哈希）、r3 patch |

## 如何复核（可复制命令）

```bash
# 1) 图件 14 基准全量重跑（重建 out/ 与统一 contact sheet）
python benchmarks/figure_families/run_all.py

# 2) 视觉质量 T 套件（before=FAIL / after=PASS 期望）
python benchmarks/visual_quality/run_visual_quality.py

# 3) 三线表 5 件（docx→pdf→渲染度量；需 LibreOffice `soffice` 在 PATH）
python benchmarks/table_family/make_tables.py

# 4) 门禁单元测试
pytest .claude/skills/figure-quality-gate/scripts/test_figure_qa.py

# 5) 产物核验（对照 reports/benchmark_artifacts_manifest_r3_20260928.csv）
python benchmarks/verify_artifacts.py --out reports/manifest_recheck.csv
```

## 本包声称的预期结果（复核时应对齐）

- 图件：13 PASS + 1 PASS_WITH_LIMITATION（b12 "2 text extents unmeasurable (3D projection)"）
- T 套件：t01 PASS；t02/t03/t04 before=FAIL、after=PASS（7/7 预期命中）
- 三线表：TABLE01–05 全部 PASS，rendered center_error ≤0.02mm（门槛 1.0mm）
- pytest：7/7 PASS
- 字体 smoke：clean_ok=True · detector_caught_gap=True · fallback=NOT USED

## 边界与限制（诚实声明）

- rougier 书代码、SciencePlots 样式文件**已文件级读取**（2026-09-28 补读：深克隆 `~/.claude/reference/` 读 13 文件；早期 403/404 的"原则级"标注已升级，见参考矩阵）。
- 本批次基线：HEAD=f65b117a（同日技术路线图批次），本批次**零 commit**、0 staged；staged 快照 `FINAL_EVIDENCE_FREEZE_20260928.md` 为更早批次的历史快照，与当前树状态不一致属预期。
- **重跑语义**：独立验收重跑全部基准后，仅 53 个"日期内嵌"文件（27 pdf / 21 svg / 5 docx）字节变化；全部 PNG/JSON/MD 字节稳定。现行产物清单（`benchmark_artifacts_manifest_r3_20260928.csv`）对应重跑后态；重跑前态哈希见 `acceptance_recheck_r3_20260928.csv`。
- text_image 碰撞为 LIMITATION（只判边界越界，ROI 需人工目检）；b12 3D 文本目检兜底。
- 表 QA 的渲染链依赖本机 LibreOffice headless；无 LibreOffice 时仅 XML 链可跑，渲染度量会标记跳过。
- `PACKAGE_MANIFEST.sha256` 覆盖本包全部文件（含本 README），不含 manifest 自身。
