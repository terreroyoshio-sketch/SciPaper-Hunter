---
name: nature-citation-wrapper
description: Use Yuan1z0825/nature-skills nature-citation for adding strict Nature/CNS citations and reference management.
---

When this skill is invoked, first read the real skill files from:

`C:\Users\张涵\.agent-skills\nature-skills\skills\nature-citation\SKILL.md`
`C:\Users\张涵\.agent-skills\nature-skills\skills\nature-citation\README.md`

Also inspect supporting files under:

`C:\Users\张涵\.agent-skills\nature-skills\skills\nature-citation\`
`C:\Users\张涵\.agent-skills\nature-skills\skills\_shared\`

Rules:

1. Only cite papers provided by the user or from verified real sources.
2. Do not invent DOIs, authors, years, journal names, or page numbers.
3. Split long text passages into citable segments according to Nature citation style.
4. Verify journal names against the Nature Portfolio accepted title list.
5. Never fabricate a citation or reference entry.
6. When the user provides a DOI, verify the metadata before citing.
7. Flag any citation that appears unverifiable.
8. Maintain consistent citation format throughout the manuscript.
9. For missing citation details, mark as [CITATION NEEDED].
10. Output a reference list in the target journal format.
