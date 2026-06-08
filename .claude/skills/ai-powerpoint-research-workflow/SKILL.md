---
name: ai-powerpoint-research-workflow
description: Build, audit, and refine research PowerPoint presentations using ChatGPT for PowerPoint, local PPTX generation, nature-paper2ppt, ppt-master, and strict research integrity and layout checks.
---

# AI PowerPoint Research Workflow

## When to use

Use this skill for:

- Research group meeting PPT
- Thesis defense PPT
- Fund/proposal defense PPT
- Academic conference talk
- Paper-to-PPT conversion
- Project presentation
- Course report slides
- Competition roadshow PPT

Do not use this skill for purely decorative slide decks, non-scientific marketing pitches, or when the only goal is applying animations and transitions.

## Core principle

**Do not generate slides before understanding the scientific story.**

A research PPT is not a compressed Word document. It is a sequence of claims supported by evidence.

## ChatGPT for PowerPoint — capability summary

**Status**: Beta (launched May 2026). Available globally across all ChatGPT tiers (Free, Plus, Pro, Business, Enterprise, Edu).

**Installation**: PowerPoint Home → Add-ins → Search "ChatGPT" → Sign in with OpenAI account.

**What it can do**:
- Create presentations from prompts, notes, documents, spreadsheets, images, or existing decks
- Edit and refine existing slides (rewrite titles, compress text, reorganize hierarchy)
- Review decks for narrative gaps and logic issues
- Pull data from connected services (Gmail, Outlook, SharePoint)
- All output is fully editable in PowerPoint

**Beta limitations**:
- Complex formatting, template handling, and custom fonts may not work reliably
- ChatGPT can make mistakes — always review numbers, claims, and formatting
- No ChatGPT add-in for Word yet (Excel and PowerPoint only)
- Enterprise/Edu accounts: data not used for training by default; workspace admins can control access

**See**: `references/chatgpt_powerpoint_official_notes.md` for full details.

## Tool routes

### Route A: ChatGPT for PowerPoint

Use when the user has PowerPoint and the ChatGPT add-in.

1. User opens PowerPoint and the add-in.
2. User provides materials (notes, paper, data).
3. ChatGPT generates or edits slides inside PowerPoint.
4. User reviews every slide, number, and claim.
5. User saves as a new file (do not overwrite original).

### Route B: Local PPTX generation

Use when the task should be done by Claude Code with local files.

Recommended tools:
- **python-pptx** — programmatic PPTX creation
- **ppt-master** — AI-driven SVG content generation
- **nature-paper2ppt** — paper-to-PPTX conversion
- Markdown → PPTX via python-pptx workflow

### Route C: Visual PNG to editable PPTX

Use only when visual design is needed first.

Rules:
- PNG drafts guide layout only
- Final PPTX must have editable text boxes, not flattened images
- Shapes should be native PPT shapes
- Do not turn the whole deck into screenshots

## Research integrity rules

1. Back up the original PPT before any edit.
2. Do not overwrite original files.
3. Do not upload unauthorized papers, unpublished data, proposals, personal privacy data, commercial materials, or account credentials.
4. Do not read cookies, tokens, passwords, or keys.
5. Do not pass AI-generated images off as real research figures.
6. Do not present simulated data as real data.
7. Do not fabricate references, DOIs, authors, journals, years, or page numbers.
8. Do not fabricate experimental results, p-values, sample sizes, or model metrics.
9. For defense and submission materials, every claim must have a source.
10. The final PPT must be reviewed by the user before submission or presentation.

## 6-stage workflow

### Stage 1: Read materials — do not rush to make slides

Input may include: Word papers, PDFs, Excel data, Markdown notes, proposals, experiment logs, images, old PPTs, draft scripts.

First output:
1. Research background
2. Core question
3. Method route
4. Data source
5. Results
6. Innovation/contribution
7. Limitations
8. Target audience
9. Presentation duration
10. Recommended page count

### Stage 2: Build structure

One core message per slide.

Common structure: Cover → Background → Problem → Gap → Objective → Method → Data → Architecture → Experiment → Results (multiple pages) → Comparison → Innovation → Value → Limitations → Summary → Acknowledgments.

Adjust for scenario:
- **Group meeting**: shorter, more results-focused
- **Thesis defense**: emphasize research question, technical route, evidence, workload
- **Fund defense**: emphasize scientific question, innovation, feasibility, preliminary work

### Stage 3: Slide content design

Each slide must have:
1. Slide title
2. Core conclusion (one sentence)
3. Supporting figure, table, or diagram
4. 3–5 bullet points max
5. Data source or figure note if needed
6. Speaker notes

Do not paste Word paragraphs into PPT.

### Stage 4: Figure and evidence audit

Every research figure must be checked:
1. Is the data real?
2. Is the figure generated from real data?
3. Is the original data path preserved?
4. Is the plotting script preserved?
5. Is there a figure caption?
6. Are there units on axes?
7. Does the legend overlap data?
8. Is the resolution sufficient?
9. Have curve/scatter/position/statistical values been altered?
10. Is there a source note?

### Stage 5: Generate PPT

Choose the appropriate route (A, B, or C above).

### Stage 6: Final checklist

Check:
1. PPTX opens correctly
2. 16:9 ratio
3. No font substitution
4. No text overflow
5. No missing images
6. No formula rendering errors
7. No blurred figures
8. Consistent page style
9. No unverified data
10. No unsourced images
11. No missing citations
12. No page number or title errors
13. No AI-generated empty clichés
14. No excessive bullet points
15. No dark blue table backgrounds or overly decorative colors

## Combination with existing skills

### Paper → PPT
ai-powerpoint-research-workflow → nature-paper2ppt → paper-reading → academic-abstract-pipeline

### Group meeting PPT
ai-powerpoint-research-workflow → nature-figure-wrapper → scientific-visualization

### Fund defense PPT
ai-powerpoint-research-workflow → nsfc-proposal-architecture-pipeline → objective-innovation-auditor-pipeline → reviewer-red-team-auditor

### Competition roadshow
ai-powerpoint-research-workflow → ppt-master → frontend-design

### Figures for PPT
nature-figure-wrapper → scientific-visualization → figure-table-caption-formatter → ai-powerpoint-research-workflow

## Output rules

For every PPT task, deliver:
1. PPT structure table
2. Draft PPTX path
3. Final PPTX path
4. Optional PDF export
5. Source file list
6. Figure source list
7. Final audit report
