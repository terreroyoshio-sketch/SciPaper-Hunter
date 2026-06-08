# Science-style Narrative Rules

## What is scientific narrative?

Scientific narrative is not the same as "telling a story" in the literary sense. It is a structured logical argument where each section serves a defined function, and every paragraph answers the question: **"Why must this paragraph exist?"**

---

## Weak manuscript pattern (experimental report style)

Recognize these symptoms:

1. **Data-first ordering**: Results are presented in the order experiments were run, not in the order of logical argument.
2. **Diffuse Introduction**: Background is long, but no specific gap is identified.
3. **Figure-led Results**: Paragraphs start with "Figure X shows..." before stating any conclusion.
4. **Circular Discussion**: Discussion only restates results in different words.
5. **Claim-evidence mismatch**: Claims are stronger than the evidence presented.
6. **No central question**: The reader cannot state the paper's core scientific question in one sentence.
7. **Chronological ≠ logical**: "First we did A, then we did B, then we did C" replaces "Why A → B → C is the necessary logical sequence."

---

## Strong manuscript pattern (science narrative style)

1. **One central scientific question** that drives the entire manuscript.
2. **Introduction** narrows from field value → existing progress → specific gap → present contribution.
3. **Methods** serve the question; they do not just display workload.
4. **Results** paragraphs state the conclusion first, then provide evidence.
5. **Discussion** returns to field-level meaning, mechanisms, comparison, and limitations.
6. **Every paragraph** has one function and one main message.

---

## Paragraph-level rule

Each paragraph must satisfy:

| Property | Question |
|----------|----------|
| Function | What is this paragraph's job? (Background / Gap / Method / Result / Mechanism / Limitation / Implication) |
| Message | What one thing should the reader remember? |
| Evidence | Is the claim supported by data, figure, table, calculation, or citation? |
| Position | Does this paragraph need to be before or after the adjacent paragraphs? |

If a paragraph does not answer all four, rewrite or remove it.

---

## Introduction narrative arc

```
Field value (broad, fast)
       ↓
Existing progress (thematic clusters, not one-paper-per-sentence)
       ↓
Key gap (specific, non-vague, addressable)
       ↓
Present contribution (maps to gap above)
```

---

## Results narrative arc per paragraph

```
Core conclusion (one sentence)
       ↓
Supporting evidence (figure, table, statistic)
       ↓
Explanation (why this result matters or what it means)
       ↓
Optional: robustness check / control / ablation
```

---

## Discussion narrative arc

```
Answer the central question
       ↓
Explain underlying mechanism
       ↓
Compare with prior studies
       ↓
State limitations (objectively, not defensively)
       ↓
Field-level implications and future work
```

---

## Common narrative flaws

| Flaw | Symptom | Fix |
|------|---------|-----|
| No central question | Reader cannot summarize the paper in one sentence. | Identify and state the core question in the Introduction. |
| Gap too vague | "However, few studies have investigated this." | Specify exactly what is missing and why it matters. |
| Results = figure captions | "Figure 1 shows..." without a claim. | Lead with the conclusion, cite the figure as evidence. |
| Discussion = Results | Discussion mostly repeats the Results section. | Discuss mechanism, comparison, limitation, implication. |
| Overclaim | "This work solves the problem." | Calibrate claim strength to actual evidence. |
| Buried lede | Main finding appears in the middle of a paragraph. | Move the main finding to the start of its paragraph. |

---

## Evidence quality check

| Evidence type | Must have |
|---------------|-----------|
| Quantitative result | Exact values, units, uncertainty or confidence interval |
| Statistical claim | Test name, test statistic, p-value or effect size, sample size |
| Comparison | Baseline name, condition match, metric name |
| Figure | Clear axis labels, units, legend, readable font size |
| Table | Column headers defined, units, consistent precision |
| Citation | Real DOI or verifiable source, relevant to the claim |
