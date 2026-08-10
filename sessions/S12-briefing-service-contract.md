---
session: 12
date:
system: research-briefing-agent
branch: feat/s12-service-contract
pr:
status: todo
---

# S12 · FastAPI layer and the three-status contract

**System 02 · Research Briefing Agent**

**Goal.** `complete` / `degraded` / `failed`. No raw dictionaries at the boundary. `tool_calls` emitted on **every** response, not only on failure. Typed errors, health endpoint, request ID per log line.

**Commit.** `feat(research-agent): add FastAPI service layer with typed models and three-status response contract`

**Evidence.** `OpenAPI schema committed`

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

## Next (S13)
ARM64 container with a cached dependency layer, running from an env file, no secrets in the image.

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
