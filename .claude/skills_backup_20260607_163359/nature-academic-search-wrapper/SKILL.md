---
name: nature-academic-search-wrapper
description: Use Yuan1z0825/nature-skills nature-academic-search for literature search and discovery for academic research.
---

When this skill is invoked, first read the real skill files from:

`C:\Users\张涵\.agent-skills\nature-skills\skills\nature-academic-search\SKILL.md`
`C:\Users\张涵\.agent-skills\nature-skills\skills\nature-academic-search\README.md`

Also inspect supporting files under:

`C:\Users\张涵\.agent-skills\nature-skills\skills\nature-academic-search\`
`C:\Users\张涵\.agent-skills\nature-skills\skills\_shared\`

Rules:

1. Search based on the user's specific research question and criteria only.
2. Do not fabricate paper titles, authors, journals, DOIs, years, or findings.
3. Use provided search tools (MCP, APIs, web search) to find real papers.
4. For every result, record: title, authors, year, journal, DOI, and a brief finding summary.
5. Verify DOIs when possible.
6. Prioritize peer-reviewed sources; flag preprints and non-peer-reviewed sources.
7. Organize results by relevance to the user's question.
8. Note the search date and tool/method used.
9. When the user provides specific search databases or methods, respect those constraints.
10. Output a search report with the query strategy, results list, and source verification notes.
