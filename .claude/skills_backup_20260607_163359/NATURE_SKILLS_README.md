# Nature Skills — 总说明

## 来源

仓库：Yuan1z0825/nature-skills (MIT License)

## 新增 Skills

| Skill | 用途 | 依赖 |
|-------|------|------|
| nature-figure | Nature 风格科研图件生成 | Python + matplotlib |
| nature-polishing | Nature 风格学术英文润色 | 无 |
| nature-citation | 引用检索与支持度判断 | Python + Crossref API |
| nature-data | 数据可用性声明与 FAIR 检查 | 无 |
| nature-paper2ppt | 论文转学术汇报PPT | python-pptx, pillow |

## 风险边界

- nature-citation 会调用 Crossref API 检索文献，必须与 literature-boundary-lock 配合，防止引用幻觉
- nature-data 不得编造 accession number 或仓库地址
- nature-paper2ppt 不得上传未公开论文
- 其余 skills 均为纯 Markdown 指南，无安全风险

## 组合方式

详见 `NATURE_SKILLS_COMBINED_WORKFLOWS.md`。
