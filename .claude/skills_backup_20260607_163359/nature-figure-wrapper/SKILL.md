---
name: nature-figure-wrapper
description: Use Yuan1z0825/nature-skills nature-figure to create submission-grade scientific figures from real user-provided data, with strict source-data traceability and export checks.
---

When this skill is invoked, first read the real skill files from:

`C:\Users\张涵\.agent-skills\nature-skills\skills\nature-figure\SKILL.md`
`C:\Users\张涵\.agent-skills\nature-skills\skills\nature-figure\README.md`

Also inspect supporting files under:

`C:\Users\张涵\.agent-skills\nature-skills\skills\nature-figure\`
`C:\Users\张涵\.agent-skills\nature-skills\skills\_shared\`

Rules:

1. Use real user-provided data only.
2. Do not invent data.
3. Do not change curve values, scatter positions, station coordinates, sample sizes, model metrics, p-values, confidence intervals, or statistical conclusions.
4. Before plotting, create a figure contract containing:
   - research question
   - core conclusion
   - evidence hierarchy
   - figure type
   - data source
   - statistical method
   - journal or document target
   - required export formats
5. Prefer editable SVG and PDF for manuscripts.
6. Export PNG at high resolution for Word and PPT preview.
7. For Word/PDF/PPT insertion, check font, size, legend, caption, panel label, axis label, unit, resolution, and page fit.
8. Use restrained academic color palettes.
9. Avoid crowded legends, over-decorated colors, 3D effects, chart junk, unreadable text, and AI poster style.
10. Generate a reproducible plotting script and a figure audit report.
