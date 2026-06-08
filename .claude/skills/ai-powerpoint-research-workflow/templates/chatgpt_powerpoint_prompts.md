# ChatGPT for PowerPoint — Prompt Templates

Use these prompts inside the ChatGPT for PowerPoint add-in (PowerPoint ribbon → ChatGPT).

---

## Template 1: Read material first, do not rush to slides

```
Please read the uploaded material carefully. Do NOT generate slides yet.

First summarize:
1. Research background
2. Core question
3. Method route
4. Data source
5. Experimental results
6. Innovation points
7. Limitations
8. Target audience
9. Recommended page count
10. One core message per proposed slide

Rules:
- Do not fabricate data
- Do not fabricate citations
- Do not rewrite experimental conclusions
- Mark missing information as "需补充"
- Output a slide structure table at the end
```

---

## Template 2: Generate research PPT structure

```
Based on the material above, design a research presentation structure.

Requirements:
1. One core message per slide
2. Slide order must follow scientific narrative logic
3. Narrow from background to core problem
4. Method slides must explain the technical route clearly
5. Results slides: state the conclusion first, then show data evidence
6. Innovation points must include comparison with prior work
7. Limitations must be stated objectively
8. Do not stack text
9. Do not fabricate figures
10. Output: page number, title, core conclusion, suggested visual element, speaker notes
```

---

## Template 3: Revise an existing half-finished PPT

```
Please review this existing presentation.
Do NOT delete large amounts of content directly. First output a problem list, then propose revisions.

Focus on:
1. Does each slide have one core message?
2. Is any slide text-dense?
3. Are there logic gaps between slides?
4. Are there unsupported claims?
5. Are figures clear and sourced?
6. Do images and data have source notes?
7. Is the font large enough for projection?
8. Is there text overflow?
9. Is the slide style consistent?
10. Which content can be compressed, and which must not be removed?
```

---

## Template 4: Generate slide visual style (for design reference)

```
Based on the content of each slide, create a visual design scheme for an academic presentation.

Important: This is a visual design reference, not the final research evidence.

Requirements:
1. 16:9 ratio
2. Clean academic style
3. White or very light gray background
4. Dark gray text
5. One unified accent color
6. Clear information hierarchy
7. Mainly use structure diagrams, charts, color blocks, and minimal text
8. No flashy animations
9. No complex decorative fonts
10. Do not replace data charts with fictional illustrations
```

---

## Template 5: Convert PNG visuals back to editable PPTX

```
Based on all the generated PNG slide visuals, reconstruct the deck as an editable PPTX.

Requirements:
1. One PNG per slide
2. 16:9 ratio
3. All text must be independent editable text boxes
4. Color blocks, lines, and shapes should use native PPT objects where possible
5. Images must keep original aspect ratio and position
6. Do NOT turn entire pages into non-editable images
7. Keep real data figures as original images — do not redraw them as fictional data
8. Output as .pptx file
9. Final check: text overflow, fonts, figure clarity, slide style consistency
```
