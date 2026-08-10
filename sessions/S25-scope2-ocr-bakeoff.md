---
session: 25
date:
system: ma-ocr
branch: feat/s25-ocr-bakeoff
pr:
status: todo
---

# S25 · Five-system OCR bake-off

**Scope 2 · Arabic & French**

**Goal.** Tesseract, an open pipeline model, a self-hosted VLM, an Arabic-specific fine-tune, one commercial API. Same 200 pages, same metrics. **Broken down by page type, never averaged into one figure.**

**Commit.** `feat(ma-ocr): run five-system Arabic OCR bake-off with CER and cost per page`

**Evidence.** `evidence/ocr_bakeoff.json + results table`

---

## What happened
-

## The number
`____` · n = `____` · definition:

## Cost
$

## Blocker
```
```
Cause:

## Dead end

## Decision

## Next (S26)
Three-tier routing layer with per-page confidence and cost accounting.

---

<details>
<summary><b>How to fill this in</b></summary>

<br>

Each entry answers four questions, in this order.

| Question | Field | Why it matters |
|---|---|---|
| **What did you try to do?** | `Goal` | Context for the session — pre-written above, do not rewrite it |
| **What actually happened?** | `What happened` · `The number` · `Blocker` | The result: success, failure, or partial |
| **What decision did you make?** | `Decision` · `Dead end` | The *why* behind the code — this is what you will need in an interview |
| **What is the next unknown?** | `Next` | Prevents cold-start anxiety next week |

**Five rules that keep it useful.**

1. **One session, one file.** A log of completed work, not a to-do list.
2. **Write it during or immediately after the session.** Memory decays inside a day.
3. **Paste the exact error.** Not "had a Docker problem" — the actual message. You will search for it again.
4. **Tag dead ends explicitly.** *"Tried Pinecone → too expensive at this stage, switched to Chroma."* This is what stops you re-entering the same rabbit hole in six weeks.
5. **Link the PR.** Set `pr:` in the frontmatter so a reader can trace the log to the diff.

**Every number carries its `n`.** A metric without a sample size is a decoration, and this log is
where the habit is enforced before the number reaches a README. No number this session? Write
"no number this session" — a blank reads as an omission, a sentence reads as a fact.

**Not here:** roadmap (→ Issues) · API docs (→ `README.md`) · how a number was produced
(→ `docs/METHODOLOGY.md`) · a decision's full record (→ `<system>/adr/`).

</details>
