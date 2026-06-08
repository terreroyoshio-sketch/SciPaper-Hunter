---
name: nature-paper2ppt-wrapper
description: Use Yuan1z0825/nature-skills nature-paper2ppt to convert scientific papers into Nature-style Chinese PPTX presentations.
---

When this skill is invoked, first read the real skill files from:

`C:\Users\张涵\.agent-skills\nature-skills\skills\nature-paper2ppt\SKILL.md`
`C:\Users\张涵\.agent-skills\nature-skills\skills\nature-paper2ppt\README.md`

Also inspect supporting files under:

`C:\Users\张涵\.agent-skills\nature-skills\skills\nature-paper2ppt\`
`C:\Users\张涵\.agent-skills\nature-skills\skills\_shared\`

Rules:

1. Base PPT content on the user's provided paper/PDF/text only.
2. Do not invent data, results, or citations for slide content.
3. Identify the paper type and argument structure before designing slides.
4. Select only the figures needed for the story — do not include every figure.
5. Write concise Chinese slide content and speaker notes.
6. Create the actual .pptx file using python-pptx.
7. Do not use flashy templates; keep a clean academic style.
8. Each slide should communicate one core message.
9. All figures/tables on slides must have source citations.
10. After creation, verify: file opens, no missing fonts, no text overflow.
