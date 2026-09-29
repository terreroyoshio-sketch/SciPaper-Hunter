# 科研写作 Skill Top 10 — 第三方仓库只读审计

- 日期：2026-09-18
- 触发：用户提供一份"2026 科研写作 Skill 排行榜 Top 10"清单，要求只读审计 + 增量吸收
- 落盘位置（只读参考）：`C:\Users\张涵\.claude\reference\sciwriting-top10-20260918\`
- 方法：`git clone --depth 1` → 元数据核验 → 静态扫描 → 与已装技能比对
- **边界：全程只读。未运行任何仓库脚本，未安装任何依赖，未改动现有技能库。**

---

## 1. 核验表（真实数据）

| # | 仓库 | 榜单★ | 实测★ | 许可 | 最后提交 | 技能数 | 判定 |
|---|------|------|------|------|----------|--------|------|
| 1 | K-Dense-AI/claude-scientific-writer | 2.4k | 2.4k | MIT | 2026-08-18 | 26（去重后） | **全冗余** |
| 2 | appautomaton/latex-arxiv-SKILL | 433 | 433 | MIT | 2026-09-13 | 4 | LaTeX 主线，本机不可执行 |
| 3 | yunshenwuchuxun/latex-paper-skills | 260 | 262 | MIT | **2026-03-25** | 8 | 与 #2 同源，停更 6 个月 |
| 4 | WenyuChiou/academic-writing-skills | 54 | 56 | MIT | 2026-09-17 | 2 | 质量高，重叠大，有局部增量 |
| 5 | ShaishavMaisuria/research-paper-lifecycle-skills | 45 | 45 | Apache-2.0 | 2026-06-27 | 42 | **有真增量** |
| 6 | jin-s13/ai-research-writing-skill | 26 | 26 | MIT | 2026-07-16 | 1 | 有局部增量 |
| 7 | Rezenders/scientific_writing_agent | 12 | 12 | Apache-2.0 | 2026-04-04 | 13 | 与已装重叠 |
| 8 | PoseZhaoyutao/research-paper-writer-skill | 3 | 3 | **无许可** | 2026-05-19 | 2 | **不采用** |
| 9 | Hiro-Inagawa/paper-audit-skill | 1 | 1 | MIT | 2026-04-16 | 1 | 小而有料，见 §4 |
| 10 | Odinary-AI/research-writing-skill | 1 | 1 | MIT | 2026-07-29 | 1 | LaTeX 单技能，无增量 |

**榜单真实性**：10 个仓库全部存在，star 数与榜单吻合（#3、#4 各有 ±2 偏差）。**这份榜单不是编造的。**

---

## 2. 静态扫描结果（装前风险检查）

| 检查项 | 结果 |
|--------|------|
| npm 生命周期钩子（postinstall / preinstall） | **无**（10 仓均无 package.json 钩子） |
| Python 安装期执行 | 仅 K-Dense 有 `[project.scripts]`（CLI 入口），非安装期执行 |
| `eval(` / `exec(` / `Invoke-Expression` | 无恶意用法（命中项为 PyTorch `model.eval()` 误报） |
| `base64.b64decode` | 命中均在 AI 生图脚本，解码 API 返回的图片，非混淆 |
| `subprocess` | 均为编译/格式转换/测试用途（pdflatex、soffice） |
| 出站域名 | api.crossref.org、api.semanticscholar.org、api.datacite.org、export.arxiv.org、api.openalex.org — 均为正规学术 API |
| 硬编码密钥 / 私钥 | **无** |
| 唯一 shell 脚本 install.sh（#9） | 良性：clone 到临时目录 → 拷贝 skills → 删除临时目录，无外传 |

**结论：未发现供应链风险。** 主要依赖为 claude-agent-sdk / requests / pymupdf / markitdown / openai（#1 的 office 扩展）。

---

## 3. 三个决定性发现

### 3.1 #1 的 26 个技能本机已全部安装
逐个比对 `~/.claude/skills/`：scientific-writing、citation-management、peer-review、xlsx、docx、pptx、pdf、venue-templates、scientific-slides、scientific-schematics、research-grants、literature-review 等 **26/26 全部存在**。
→ 该仓对本地工作台**零增量**，无需吸收。

### 3.2 #2 与 #3 是同一套技能
两者技能名完全一致：`arxiv-paper-writer`、`latex-rhythm-refiner`、`collaborating-with-claude`、`collaborating-with-gemini`。榜单把它们当作两个独立项目排名，属于重复计数。

### 3.3 LaTeX 工具链在本机不存在
```
pdflatex / xelatex / lualatex / latexmk / bibtex / biber  →  全部 ABSENT
typst → OK    pandoc → OK
```
#2、#3、#10 的核心交付物是 `.tex → PDF → arXiv 提交`，**在本机无法跑通**。吸收其工作流等于得到一套"编译不了"的论文技能。若要启用，前置动作是安装 MiKTeX/TeX Live（需单独授权）。

---

## 4. 真正的增量清单

| 增量 | 来源 | 许可 | 价值 | 与本机现状的关系 |
|------|------|------|------|------------------|
| **机器可读 venue profile + 确定性 venue diff + 强制回源核验 CFP** | #5 | Apache-2.0 | 高 | 本机 `venue-templates` 只是模板文件，**没有"投稿要求档案库"这一层** |
| **Paper-type × Venue 分级语气规则 + 引文"承重"检验 + Swales moves** | #9 | MIT | 中 | 现有写作技能无"按目标期刊分级禁用语"机制 |
| **段落写作契约（function / claim / evidence / development / bridge）+ 上下双向对齐** | #4 | MIT | 中 | 与 academic-paper 重叠，但契约形式更可执行 |
| **claim→evidence 溯源 + build hash 门控（paper_state.json / citation_lock）** | #6 | MIT | 中低 | 与既有 `research-execution-provenance` 职责重叠 |
| LaTeX 门控工作流（Gate 0 快照 → plan → issues CSV 契约 → 引文逐条核验 → 编译） | #2 | MIT | 待定 | **被 LaTeX 缺失阻塞** |

---

## 5. 局限与未验证项

1. **未运行任何代码**。全部结论来自静态阅读，不构成"功能可用"判断。
2. **未验证 README 宣传语**，例如 #2 的"verified BibTeX citations"、#1 的"real-time literature search"。
3. **未做依赖解析**：未尝试 `pip install`，未检查依赖树冲突。
4. **未测运行期行为**：脚本是否会触网、是否写出预期文件，均未实测。
5. `openai>=2.47.0`（#1 office 扩展）表明部分生图技能依赖 OpenAI API —— 需 API key，且会把内容发往第三方。

---

## 6. 建议

1. **不采纳**：#1（全冗余）、#8（无许可）、#10（无增量）。
2. **不采纳但记录**：#3（#2 同源且停更）。
3. **优先吸收**：#5 的 venue profile 机制 —— 缺的是"投稿要求档案"这一层，且不在用户已叫停的"审计族"范围内，属规划/产出工具。
4. **按需吸收**：#9 的分级语气规则（建议折进现有写作技能作 reference，而非新装一个 auditor）、#4 的写作契约。
5. **暂缓**：#2/#6 的 LaTeX 链路 —— 待确认是否安装 LaTeX。用户当前主线是 Word。

**注**：用户 2026-09-06 已明确"停止审计族、转产出型"。本报告的吸收建议据此排除了新增 auditor 类技能。

---

## 7. 执行结果（2026-09-18 用户决策后）

### 7.1 已落地：`~/.claude/skills/venue-profile/`（用户级，Apache-2.0）

来源 #5，取 `tailor-to-venue` + `select-venue` + `add-venue-profile` 三技能的脚本与参考文档，
已保留上游 `LICENSE` 与 `NOTICE`。

**上游不发布档案库**：`venues/schema.yml`、`venues/families/`、`venues/conferences/` 在
`ShaishavMaisuria/research-paper-lifecycle-skills` 中**不存在**（非子模块、非其他分支，
已用 `git branch -a` + `.gitmodules` + 全树 `find` 三方确认）。脚本靠向上查找
`venues/schema.yml` 这个**哨兵文件**定位根目录；实际校验规则硬编码在 `validate_profile.py`，
`schema.yml` 本体不被解析。因此本地的 `schema.yml` 与 7 个 family 文件（acm-sigconf /
acm-manuscript-chi / acm-journal / ieee-conf / ieee-journal / neurips-style / lncs）为**自撰**，
`venues/conferences/` **按用户决策留空**——上游 Rule zero 要求每个数字来自当场抓取的 CFP，
预置档案必然速造且会过期。

**端到端验证（实际运行，非静态检查）**：

| 步骤 | 命令 | 结果 |
|------|------|------|
| 脚手架 | `init_profile.py demo-2026 --family acm-sigconf` | 写出骨架，family 解析成功 |
| 校验 | `validate_profile.py venues/conferences/demo-2026.yml` | `0 errors, 1 warning`（仅 aliases 全 null，符合未填骨架预期） |
| 列表 | `list_venues.py` | 正确读出档案并排序 |
| 差分 | `venue_diff.py main.tex --venue ... --track Research` | 正确识别 documentclass 匹配、页数限制未填、blind 未指定；顶部打印 `VERIFY BEFORE TRUSTING` + `needs-verification` |

验证后已删除 `demo-2026.yml` 测试骨架，`venues/conferences/` 仅留 README 说明。

### 7.2 环境变更：LaTeX 链路打通

- **安装**：`winget install MiKTeX.MiKTeX` → MiKTeX 25.12，装于
  `%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64`，**即原死链 PATH 指向处，死链自动复活**。
- **实测通过**：`pdflatex` exit 0；`pdflatex→bibtex→pdflatex×2` 往返 exit 0 且 `.bbl` 条目正确；
  `xelatex` + `ctexart` 中文 exit 0，SimSun/SimHei 真嵌入。
- **清理**：`C:\texlive` 空壳（164 MB / 4607 文件 / 零 TeX 二进制）已删除。
  `2026/` 子树普通权限可删；`2025/` 的 ACL 为 `Users:(RX)`，需提权 PowerShell（UAC）完成。
  已记入 `logs/deletion_log.md`。
- 验证产物保留在 `~/.claude/reference/sciwriting-top10-20260918/_latex_smoke/`。

### 7.3 未做

- #2/#3 的 LaTeX 门控工作流**未吸收**：LaTeX 现在虽已可用，但用户未要求吸收该工作流，
  且其与 #3 同源、#3 已停更。
- #4 写作契约、#6 claim-evidence、#9 分级语气规则：用户选择本轮不做。
- 全部 10 仓**未运行任何脚本、未安装任何依赖**（静态扫描与文档阅读为限），
  唯一例外的实际执行是上述 4 条验证命令与 MiKTeX 安装。
