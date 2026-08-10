# Engineering log

One file per session. Written the same evening, never "tomorrow." It exists first to solve
re-entry — seven days is long enough to forget where you were — and second because a log that
records a dead end and names its cause reads as engineering, where a log of only successes reads
as marketing.

**Fill four fields and nothing else matters.**

| Field | Rule |
|---|---|
| **The number** | Always with its `n`. No sample size, no number. If there wasn't one, write "no number this session." |
| **Blocker** | The verbatim error, not a paraphrase. You will search for the exact string again. |
| **Decision** | "Chose X over Y because [measurement]" — never just "chose X". This is what an ADR is written from. |
| **Next** | One sentence. If it takes two, the next session is scoped too large. |

`Goal`, `Commit` and `Evidence` are pre-written. They are the definition of done — don't rewrite them.
Set `status: done` and the date in the frontmatter when the PR merges.

Not here: roadmap (→ Issues), API docs (→ `README.md`), how a number was produced (→ `docs/METHODOLOGY.md`),
a decision's full record (→ `<system>/adr/`). This is completed work and confirmed decisions only.

---

## Sessions

**21 core across three systems, then 12 for Scope 2.** Three recovery weeks sit after S09, S15 and S21.

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