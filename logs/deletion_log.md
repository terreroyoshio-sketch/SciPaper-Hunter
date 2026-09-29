# Deletion Log

> 任何删除都必须记录。每次删除操作追加一条记录。

## 格式

每条记录包含：
- **删除时间:** YYYY-MM-DD HH:MM:SS
- **删除路径:**
- **删除原因:**
- **是否备份:** 是/否
- **是否可恢复:** 是/否
- **执行者:**
- **风险说明:**

---

## 2026-09-18 — 删除 C:\texlive（TeX Live 半装残骸）

- **删除时间:** 2026-09-18
- **删除路径:** `C:\texlive`（含 `2025/`、`2026/`、`texmf-local/`）
- **删除原因:** 两次中途失败的 TeX Live 安装残骸。共 164 MB、4607 个文件、1042 个目录，
  **不含任何 TeX 二进制**（无 pdflatex.exe / xelatex.exe / latex.exe / tex.exe，无 `bin/` 目录），
  仅有 `texmf-dist` 文档与字体数据、`texmf-config` 及 tlmgr 的 perl 脚本。
  不在 PATH 上，不可用；已由 winget 安装的 MiKTeX 25.12 取代（pdflatex/bibtex/xelatex+ctex 实测通过）。
- **是否备份:** 否（用户明确选择直接删除）
- **是否可恢复:** 否
- **执行者:** Claude Code（用户 2026-09-18 明确授权）
- **风险说明:** 该目录无任何可用工具链，删除不影响已安装的 MiKTeX。
  理论风险：若日后想恢复 TeX Live 2025/2026 的 texmf 数据需重新下载，但该数据本身不完整、无价值。
  附带修复：PATH 中原指向 MiKTeX 的死链条目因 MiKTeX 安装到位而自动恢复有效。

## 2026-09-19 — 删除 C:\Users\张涵\.agent-skills\nature-skills（陈旧克隆）

- **删除时间:** 2026-09-19
- **删除路径:** `C:\Users\张涵\.agent-skills\nature-skills`（含 `.git`）
- **删除原因:** Yuan1z0825/nature-skills 的旧 git clone，停在 commit `2a3dfff`（2026-06-01），
  比上游落后约 3.5 个月；且只含 10 个技能（上游现为 19 + nature-shared），目录命名还是旧的
  `_shared`（上游已改名 `nature-shared`）。
  本机当时共有三份 nature-skills 副本，10 个 `nature-*-wrapper` 技能原先读的是这一份；
  2026-09-19 已把 wrapper 全部改指向 `~/.claude/skills/nature-*`，
  **删除前实测指向该目录的引用数 = 0**。保留它只会让人误以为还存在第三个入口。
- **是否备份:** 是 → `backups/agent-skills-nature_20260919/nature-skills`（680 文件 / 76 MB，
  与源逐文件核对数量一致）
- **是否可恢复:** 是（可从备份恢复，或重新 clone 上游）
- **执行者:** Claude Code（用户 2026-09-19 明确授权"先备份再删"）
- **风险说明:** 已确认无引用方；`~/.codex/skills` 与 `~/.claude/skills` 两份 live 副本不受影响。
  注：删除前该克隆内仍有 nature-citation 的 XSS sink，已在删前打过补丁并同步进本备份。
- **执行过程备注:** `2026/` 子树（62 MB）由普通权限删除；`2025/` 子树与 `texmf-local/` 的 ACL 为
  `BUILTIN\Users:(RX)` / `Administrators:(F)`，普通用户无删除权，因此改用提权 PowerShell
  （UAC 授权后）完成。删除后复核：`C:\texlive` 已不存在，`pdflatex` 为 MiKTeX-pdfTeX 4.23
  (MiKTeX 25.12)，示例文档重新编译 exit 0。临时提权脚本已清理。
