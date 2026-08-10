---
session: 17
date:
system: due-diligence-agent
branch: feat/s17-mcp-research
pr:
status: todo
---

# S17 · Ingestion and retrieval over MCP

**System 03 · Due Diligence Agent · flagship**

**Goal.** One entry point serves an NDA **and** a loan application — reuse System 01's pipeline, do not rewrite it. Retrieval through MCP, not a function call. `insufficient_evidence` recorded as a gap, never retried blindly.

**Commit.** `feat(due-diligence): add ingestion agent and route retrieval through the Legal Intelligence Engine over MCP`

**Evidence.** `Both document types ingested · trace showing the MCP call inside the agent run`

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

## Next (S18)
Evidence pool with claim-to-span bindings, and a memo whose structure is identical across ten runs.

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
