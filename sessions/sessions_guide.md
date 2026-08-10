# How to use this bundle

**One file per session, 34 of them.** Drop `sessions/` and `tools/` into the root of
`Dokist-ai/core`. Edit one file per evening. `SESSIONS.md` is generated, not hand-written.

```
core/
├── SESSIONS.md              ← GENERATED · the file a stranger reads
├── sessions/
│   ├── _TEMPLATE.md         ← for unplanned sessions
│   ├── S00-repository-triage.md   ← filled in, as a worked example
│   ├── S01-engine-ingestion.md
│   └── … S33-scope2-release.md
└── tools/
    └── build_sessions.py    ← concatenates sessions/*.md → SESSIONS.md
```

---

## Why split, and why still generate one file

Two audiences want opposite things.

**You**, writing on a tired Tuesday, want one small file with the goal already written, no
scrolling past thirty other entries, and no merge conflict when a session's PR touches only its
own file. That is `sessions/`.

**A CTO**, eight seconds in, wants to scroll one document top to bottom and watch a system get
built. Thirty-four clicks is thirty-four chances to stop. That is `SESSIONS.md`.

So the per-session files are the source of truth and `SESSIONS.md` is built from them.

```bash
python tools/build_sessions.py
```

Run it at the end of every session, in the same commit as the entry. The generated file carries a
progress line — *"7 / 21 core sessions"* — and an index table linking to each entry.

---

## The evening loop

1. **0:00** — open `sessions/S{NN}-*.md`. The **Goal** is already written; it is tonight's
   definition of done. Do not rewrite it.
2. **2:30** — fill **What happened**, **The number**, **Blocker hit**. Paste the *verbatim* error.
3. **3:15** — fill **Decision made** and confirm **Next session, single goal** still holds.
4. Set `status: done` and `date:` in the frontmatter, add the PR number.
5. `python tools/build_sessions.py`, commit both the entry and the regenerated `SESSIONS.md`.

---

## The four fields that must never be blank

- **The number carries its `n`.** No sample size, no number. If the session produced none, write
  "no number this session" — a blank reads as an omission, a sentence reads as a fact.
- **The blocker has the verbatim error.** A paraphrase is worth nothing in six weeks, and the
  exact string is what you will search for.
- **The decision names what you rejected.** *"Chose X over Y because [measurement]"* — this is
  the raw material every ADR is written from, and it is the answer to "what did you choose it
  over?" in the skills ledger.
- **The next goal is one sentence.** If it needs two, next session is scoped too large.

---

## Frontmatter

```yaml
session: 4                        # integer, drives ordering
date: 2026-09-01                  # fill on completion
system: legal-intelligence-engine
branch: feat/s04-ragas-harness
pr: 61
status: not-started               # not-started | in-progress | done
```

GitHub renders this as a small table at the top of each file. `status` and `session` are what the
build script reads for the progress line and the index.

---

## What does **not** go in here

| Belongs elsewhere | Where |
|---|---|
| Roadmap items, future ideas | GitHub Issues |
| API documentation, usage | `README.md`, `docs/` |
| How a number was produced | `docs/METHODOLOGY.md` |
| A decision's full record | `<system>/adr/` |
| Raw brainstorming | a scratchpad, not the repo |

This log is for **completed work** and **confirmed decisions**. The moment it becomes a to-do
list it stops being evidence and starts being a wish list.

---

## Session map

| Sessions | System | Files |
|---|---|---|
| 01 → 09 | Legal Intelligence Engine — retrieval core + MCP server | `S01`–`S09-engine-*` |
| 10 → 15 | Research Briefing Agent — production + reliability | `S10`–`S15-briefing-*` |
| 16 → 21 | Due Diligence Agent — flagship | `S16`–`S21-diligence-*` |
| 22 → 33 | Scope 2 — Arabic & French benchmark | `S22`–`S33-scope2-*` |

**21 core sessions, not 18.** The engine carries nine because it absorbed the Contract Q&A
Assistant. Three recovery weeks sit after Sessions 09, 15 and 21 — spend them on missed weeks,
never on extended scope.

---

## Optional: keep the generated file honest in CI

Add to your lint workflow so a hand-edited `SESSIONS.md` cannot drift from its sources:

```yaml
- name: SESSIONS.md is up to date
  run: |
    python tools/build_sessions.py
    git diff --exit-code SESSIONS.md
```

*Built with intention. Measured before it ships.*
