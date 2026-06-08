# Passive and Active Voice Rules for SCI Writing

## Overview

Correct use of passive and active voice is one of the most visible markers of mature SCI writing. Non-native speakers tend to either overuse passive everywhere (making text heavy) or overuse active with "we" (making text sound like a lab notebook). This reference provides rule-level guidance.

---

## 1. "We" — author team only

**Rule**: Use *we* only for the actions and decisions of the author(s) or research team.

| ✓ Correct (author action) | ✗ Incorrect (general) |
|---------------------------|----------------------|
| We measured the absorbance at 450 nm. | We know that climate change affects crop yield. |
| We developed a prediction model. | We think that deep learning is powerful. |
| We evaluated the robustness of the method. | We can see that this problem is important. |
| We collected data from 120 participants. | We all understand that water freezes at 0 °C. |

**Why**: Using *we* for general knowledge confuses the reader about what is the author's own contribution vs. what is established knowledge.

---

## 2. General knowledge — no "we"

**Rule**: Express domain常识, established findings, or公共认知 using objective constructions.

Use:
- It is known that ...
- It is generally accepted that ...
- It has been reported that ...
- Previous studies have shown that ...
- Prior work suggests that ...
- There is growing evidence that ...
- It is well established that ...
- It is widely recognized that ...

**Constraint**: Only use these when the claim is supported by real literature. If a citation is needed, add `[需补充引用]`.

---

## 3. Methods — passive voice is standard

**Rule**: In Methods sections, passive voice is the default for reporting procedures.

Examples:
- The sample was measured at room temperature.
- The solution was added dropwise.
- The dataset was split into training (80%), validation (10%), and test (10%) sets.
- Statistical significance was assessed using a two-tailed t-test.
- The model was trained for 100 epochs with a batch size of 32.

**Exception**: When the method involves a novel procedure developed by the authors, *we* + active is acceptable:
- We designed a custom loss function to address class imbalance.

---

## 4. Results — active preferred for claims

**Rule**: Results sections should state conclusions using active voice, with supporting evidence in parentheses or following the claim.

| Weaker (passive) | Stronger (active) |
|------------------|-------------------|
| It was observed that the accuracy was higher. | The proposed model achieved higher accuracy (92.3%) than the baseline (87.1%). |
| A significant difference was found between the two groups. | Group A outperformed Group B by 12.5% (p < 0.01). |

---

## 5. Here / In this study / This article / The present paper

| Phrase | Function | Example |
|--------|----------|---------|
| Here, | Concise finding introduction | Here, we show that ... |
| In this study, | Scope of research | In this study, we investigate ... |
| This article | Dummy subject for Introduction | This article presents a framework for ... |
| The present paper | Formal self-reference | The present paper examines ... |

**Avoid** repeating the same phrase in consecutive sentences.

---

## 6. Never use "by me" or "by other researchers"

| ✗ Incorrect | ✓ Correct |
|-------------|-----------|
| The experiment was conducted by me. | The experiment was conducted under controlled conditions. |
| This was confirmed by us. | These results were confirmed through independent validation. |
| This problem was studied by other researchers. | This problem has been examined in prior work [ref]. |

When attribution is needed, use specific citations, not "other researchers".

---

## 7. Dummy subjects for clarity

In the Introduction, using *this study / this article / the present paper* as a subject is often clearer than an agentless passive:

| Unclear | Clearer |
|---------|---------|
| A new method is proposed. | This study proposes a new method. |
| The mechanism is explained. | The present paper explains the mechanism. |
| Three experiments were conducted. | In this study, three experiments were conducted. |

Maintain variety. Not every sentence should start with "This study".

---

## 8. Common mistake patterns

| Mistake | Problem | Fix |
|---------|---------|-----|
| We know that X is important. | we used for general fact | It is known that X is important. |
| The experiment was conducted by us. | by us is redundant | The experiment was conducted... (or We conducted...) |
| In this paper, this paper proposes... | repetitive | This paper proposes... (drop the first "in this paper") |
| A model was developed. The model was trained. The model was tested. | three passives in a row | We developed a model, trained it on ..., and tested it on ... |
| It was found that the result was significant. | vague, heavy | The result was significant (p < 0.05). |
