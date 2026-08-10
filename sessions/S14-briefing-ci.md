---
session: 14
date:
system: research-briefing-agent
branch: test/s14-ci
pr:
status: todo
---

# S14 · Fourteen mocked tests and CI

**System 02 · Research Briefing Agent**

**Goal.** Patch **at the call site**, not the definition site. **Deliberately break one function and confirm the relevant test goes red.** Lint → test → deploy gated on main. Write **ADR-003**. CI badge only after this merges green.

**Commit.** `test(research-agent): add 14 pytest tests with mocked LLM and search calls, wire GitHub Actions CI`

**Evidence.** `Green CI run URL · test output · adr/003-mock-every-external-call.md`

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

## Next (S15)
Reliability harness over a fixed topic set: every tool call recorded with outcome, cause and latency.
