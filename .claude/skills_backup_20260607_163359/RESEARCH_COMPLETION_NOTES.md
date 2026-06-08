# 科研 Skills 依赖补齐完成记录

## 1. web-search-exa — EXA_API_KEY 配置说明

**当前状态**: ❌ 未设置
**需要用户手动配置**:

### Windows PowerShell (临时)
```powershell
$env:EXA_API_KEY = "你的Exa API密钥"
```

### Windows (永久)
```powershell
[Environment]::SetEnvironmentVariable("EXA_API_KEY", "你的密钥", "User")
```

### macOS / Linux
```bash
export EXA_API_KEY="你的密钥"
```

获取密钥: https://exa.ai

## 2. academic-research-hub — Python 依赖

**已安装** ✅
- arxiv
- scholarly
- pubmed-parser
- semanticscholar

## 3. academic-deep-research — 已找到并安装

❌ `academic-deep-research` 不可用（ClawHub slug 不匹配）
✅ 替代方案: **academic-deep-research-pro** 已安装
路径: `~/.claude/skills/academic-deep-research-pro/`
