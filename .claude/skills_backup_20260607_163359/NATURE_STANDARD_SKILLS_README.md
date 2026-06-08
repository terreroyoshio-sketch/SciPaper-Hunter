# Nature Standard Skills — 总说明

## 来源

仓库：Yuan1z0825/nature-skills (MIT License)

## 已安装 Skills

| Skill | 用途 | 状态 |
|-------|------|------|
| nature-figure | Nature 风格科研图件生成 | ✅ 稳定版 |
| nature-polishing | Nature 风格学术英文润色 | ✅ 稳定版 |
| nature-citation | 引用检索与支持度判断 | ✅ Beta |
| nature-data | 数据可用性声明与 FAIR 检查 | ✅ Beta |
| nature-paper2ppt | 论文转学术汇报 PPT | ✅ Beta |
| nature-response | 审稿意见逐条回复 | ✅ Beta（本次新增） |

## 风险边界

- nature-citation 会调用 Crossref API，需配合 literature-boundary-lock
- nature-response 不得虚构审稿意见或修改内容
- 其余 skills 均为纯 Markdown 指南

## 组合方式

详见 `NATURE_STANDARD_COMBINED_WORKFLOWS.md`。
