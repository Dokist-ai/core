# Engineering log

One file per session — what was attempted, what actually happened, which decisions were made and
why, and what was still unknown at the end. Written the same evening, never "tomorrow."

It exists first to solve **re-entry**: seven days between sessions is long enough to forget exactly
where you were, and fifteen minutes of writing here saves forty-five minutes of re-orientation
next week. It exists second because it turns out to be the most persuasive document in the
repository — a log that records a twenty-minute dead end, names the cause precisely and moves on
reads as engineering, where a log of only successes reads as marketing.

## The programme

**33 sessions across 36 weeks** · one evening a week · three recovery weeks after S09, S15 and S21.

| Build | System | Sessions |
|---|---|---|
| 01 | **Legal Intelligence Engine** — retrieval core + MCP server | 01 → 09 |
| 02 | **Research Briefing Agent** — production + reliability | 10 → 15 |
| 03 | **Due Diligence Agent** — flagship, composes the other two | 16 → 21 |
| — | **Scope 2** — Arabic & French benchmark | 22 → 33 |

---

## How to fill an entry

Each entry answers four questions, in this order.

| Question | Field | Why it matters |
|---|---|---|
| **What did you try to do?** | `Goal` | Context for the session — **pre-written, do not rewrite it.** It is tonight's definition of done. |
| **What actually happened?** | `What happened` · `The number` · `Blocker` | The result: success, failure, or partial |
| **What decision did you make?** | `Decision` · `Dead end` | The *why* behind the code — this is what you will need in an interview |
| **What is the next unknown?** | `Next` | Prevents cold-start anxiety next week |

`Goal`, `Commit` and `Evidence` come pre-filled at the top of every file. Set `status: done`,
the `date:` and the `pr:` number in the frontmatter when the pull request merges.

---

## Five rules that keep it useful

1. **One session, one file.** This is a log of completed work, not a to-do list.
2. **Write it during or immediately after the session.** Memory decays inside a day.
3. **Paste the exact error.** Not "had a Docker problem" — the actual message. You will search for it again.
4. **Tag dead ends explicitly.** *"Tried Pinecone → too expensive at this stage, switched to Chroma."* This is what stops you re-entering the same rabbit hole in six weeks.
5. **Link the PR.** The `pr:` field in the frontmatter, so a reader can trace the log to the diff.

## Every number here carries its `n`

A metric without a sample size is not a claim, it is a decoration — and it is the first thing a
competent reviewer attacks. This log is where the habit is enforced **before** the number reaches
a README. If a session produced no number, write "no number this session" rather than leaving the
field blank: a blank reads as an omission, a sentence reads as a fact.

## What does not go here

| Belongs elsewhere | Where |
|---|---|
| Roadmap items, future ideas | GitHub Issues |
| API documentation, usage | `README.md`, `docs/` |
| How a number was produced | `docs/METHODOLOGY.md` |
| A decision's full record | `<system>/adr/` |
| Raw brainstorming | a scratchpad, not the repo |

Completed work and confirmed decisions only. The moment this becomes a to-do list it stops being
evidence and starts being a wish list.

---

## Sessions

| # | Session | System | Status |
|---|---|---|---|
| 00 | [Machine triage and repo identity](S00-repository-triage.md) | repository | done |
| 01 | [Clause-aware ingestion](S01-engine-ingestion.md) | legal-intelligence-engine | — |
| 02 | [Retrieval and the four-status response contract](S02-engine-response-contract.md) | legal-intelligence-engine | — |
| 03 | [The 40-question golden dataset](S03-engine-golden-set.md) | legal-intelligence-engine | — |
| 04 | [RAGAS harness and four-config comparison](S04-engine-ragas-harness.md) | legal-intelligence-engine | — |
| 05 | [Red team and the antonym probe set](S05-engine-red-team.md) | legal-intelligence-engine | — |
| 06 | [Training environment and the LoRA ablation](S06-engine-train-env-ablation.md) | legal-intelligence-engine | — |
| 07 | [Adapter evaluation and the null result](S07-engine-adapter-eval.md) | legal-intelligence-engine | — |
| 08 | [Hard negative mining and the domain embedder](S08-engine-embeddings.md) | legal-intelligence-engine | — |
| 09 | [MCP server, eval gate, ship](S09-engine-mcp-server.md) | legal-intelligence-engine | — |
| 10 | [AgentState schema and the research node](S10-briefing-agent-state.md) | research-briefing-agent | — |
| 11 | [Synthesis node and the degradation paths](S11-briefing-degradation-paths.md) | research-briefing-agent | — |
| 12 | [FastAPI layer and the three-status contract](S12-briefing-service-contract.md) | research-briefing-agent | — |
| 13 | [ARM64 container](S13-briefing-docker.md) | research-briefing-agent | — |
| 14 | [Fourteen mocked tests and CI](S14-briefing-ci.md) | research-briefing-agent | — |
| 15 | [Reliability benchmark and ship](S15-briefing-reliability-benchmark.md) | research-briefing-agent | — |
| 16 | [State shapes and the coverage matrix](S16-diligence-coverage-matrix.md) | due-diligence-agent | — |
| 17 | [Ingestion and retrieval over MCP](S17-diligence-mcp-research.md) | due-diligence-agent | — |
| 18 | [Evidence pool and memo synthesis](S18-diligence-evidence-pool.md) | due-diligence-agent | — |
| 19 | [Groundedness gate and the headline number](S19-diligence-groundedness-gate.md) | due-diligence-agent | — |
| 20 | [Hardening, adversarial suite, eval gate](S20-diligence-hardening.md) | due-diligence-agent | — |
| 21 | [UI, benchmarks, portfolio rebuild](S21-diligence-launch.md) | due-diligence-agent | — |
| 22 | [Bulletin Officiel scraper](S22-scope2-bo-scraper.md) | ma-corpus | — |
| 23 | [Text-layer inventory](S23-scope2-text-layer-inventory.md) | ma-corpus | — |
| 24 | [200-page OCR ground truth](S24-scope2-ocr-ground-truth.md) | ma-corpus | — |
| 25 | [Five-system OCR bake-off](S25-scope2-ocr-bakeoff.md) | ma-ocr | — |
| 26 | [Three-tier OCR router](S26-scope2-ocr-router.md) | ma-ocr | — |
| 27 | [Arabic normalisation and dual-calendar parser](S27-scope2-arabic-normalisation.md) | ma-norm | — |
| 28 | [AR/FR alignment from paired editions](S28-scope2-ar-fr-alignment.md) | ma-corpus | — |
| 29 | [Five hundred candidate QA pairs](S29-scope2-benchmark-candidates.md) | ma-bench | — |
| 30 | [Jurist verification and benchmark v0.1](S30-scope2-benchmark-v0.md) | ma-bench | — |
| 31 | [Retrieval benchmark, three models x hybrid](S31-scope2-retrieval-benchmark.md) | ma-retrieval | — |
| 32 | [Cross-lingual FR to AR retrieval](S32-scope2-cross-lingual.md) | ma-retrieval | — |
| 33 | [Publish dataset and results](S33-scope2-release.md) | ma-bench | — |

*Built with intention. Measured before it ships.*
