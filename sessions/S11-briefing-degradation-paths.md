---
session: 11
date:
system: research-briefing-agent
branch: feat/s11-degradation-paths
pr:
status: todo
---

# S11 · Synthesis node and the degradation paths

**System 02 · Research Briefing Agent**

**Goal.** Both nodes in a StateGraph. **Build the failure branches now, not later.** Verify by forcing a tool to fail and confirming the run terminates in `degraded` with a gap list. Tracing on, both nodes visible. Write **ADR-002**.

**Commit.** `feat(research-agent): add synthesis node and wire bounded backoff, fallback and degradation into the graph`

**Evidence.** `evidence/traces/ · forced-failure trace · adr/002-degrade-not-retry.md`

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

## Next (S12)
FastAPI layer with Pydantic models and the three-status contract; tool_calls on every response.
