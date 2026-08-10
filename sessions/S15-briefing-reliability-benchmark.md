---
session: 15
date:
system: research-briefing-agent
branch: feat/s15-reliability-benchmark
pr:
status: todo
---

# S15 · Reliability benchmark and ship

**System 02 · Research Briefing Agent**

**Goal.** Live sources, every call recorded with **cause** on failure: timeout / rate limit / malformed / empty. Latency definition stated explicitly. Envelope measured row filled, ~20 and ~50 marked `not measured`. Deploy, demo, tag v1.0. Write **ADR-001**.

**Commit.** `feat(research-agent): add reliability harness measuring tool-call success and latency percentiles — System 02 complete`

**Evidence.** `evidence/reliability_run.json · metrics.json · adr/001-measure-tool-calls.md`

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

## Next (S16)
Shared state shapes fixed, then the coverage matrix materialised before any retrieval.

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
