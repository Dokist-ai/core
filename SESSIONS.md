# Engineering Log — DOKIST
 
> The running record of how this repository came to be: what was attempted each session, what
> actually happened, which decisions were made and why, and what was still unknown at the end.
> Written the same evening, every evening. Never "tomorrow."
 
**Why this file exists.** It solves two problems at once. First, re-entry: seven days between
sessions is long enough to forget exactly where you were, and fifteen minutes of writing here
saves forty-five minutes of re-orientation next week. Second, and less obviously, it is the most
persuasive document in the repository — a log that records a twenty-minute dead end, names the
cause precisely and moves on reads as engineering, where a log of only successes reads as marketing.
 
**Programme:** 33 sessions across 36 weeks · one evening a week · three declared recovery weeks
after Sessions 09, 15 and 21.
 
| Build | System | Sessions |
|---|---|---|
| 01 | Legal Intelligence Engine — retrieval core + MCP server | 01 → 09 |
| 02 | Research Briefing Agent — production + reliability | 10 → 15 |
| 03 | Due Diligence Agent — flagship, composes the other two | 16 → 21 |
| — | Scope 2 — Arabic & French benchmark | 22 → 33 |
 
---
 
## How to fill an entry
 
Each entry answers four questions, in this order:
 
| Question | Field | Why it matters |
|---|---|---|
| What did you try to do? | **Goal** | Context for the session — pre-written below, do not rewrite it |
| What actually happened? | **What happened** / **The number** / **Blocker hit** | The result: success, failure, or partial |
| What decision did you make? | **Decision made** / **Dead end** | The *why* behind the code — this is what you will need in an interview |
| What is the next unknown? | **Next session, single goal** | Prevents cold-start anxiety next week |
 
**Five rules that keep it useful.**
 
1. **One session, one heading.** This is a log of completed work, not a to-do list.
2. **Write it during or immediately after the session.** Memory decays inside a day.
3. **Paste the exact error.** Not "had a Docker problem" — the actual message. You will search for it again.
4. **Tag dead ends explicitly.** *"Tried Pinecone → too expensive at this stage, switched to Chroma."* This is what stops you re-entering the same rabbit hole in six weeks.
5. **Link the PR.** Every entry should carry `#NN` so a reader can trace the log to the diff.
**Never put here:** roadmap items (→ GitHub Issues), API documentation (→ `README.md` / `docs/`),
or raw brainstorming (→ a scratchpad). This file is for *completed work* and *confirmed decisions*.
 
**Every number written here carries its `n`.** A metric without a sample size is a decoration,
and this log is where the habit is enforced before the number reaches a README.



## 2026-08-10 — Docker build fixed, CITATION.cff added
**Goal:** Fix the CI build blocking PR #52 and add proper citation metadata.  
**What happened:**  
- Build failed because `legal-intelligence-engine/requirements.txt` was missing. Added empty file to satisfy Dockerfile COPY.
- Build succeeded but cache export is slow (~15 min). Decided to keep `cache-to: type=gha` for now.
- Added `CITATION.cff` for GitHub's native citation button. Kept README section as a short pointer.
- Learned: `COPY` in Docker is relative to build context, not filesystem root.

**Decisions:**  
- Will skip `push: true` on PR builds later to save time. Not urgent now.
- Will add `version` and `doi` to CFF only after first stable release tag.

**Next unknown:**  
- How to reduce Docker image size? Currently pulling heavy LangChain deps. Maybe slim base image or multi-stage build?

do this every sunday.
 
---

