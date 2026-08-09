<p align="center">
  <img src="assets/logo.png" alt="DocumentLab.ai" width="80"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-0c1a2e?style=flat-square" alt="License: MIT"/>
  <img src="https://img.shields.io/badge/python-3.11+-0c1a2e?style=flat-square" alt="Python 3.11+"/>
  <img src="https://img.shields.io/badge/evaluation-RAGAS-C8960C?style=flat-square" alt="Evaluated with RAGAS"/>
</p>

# Sara Dhimdi — AI Engineer

**RAG systems, LLM agents, and evaluation harnesses for legal and financial documents.**
Three systems, one niche, every claim traced to a raw run in `evidence/`.

> **These are reference systems, not client deployments.** Built on public corpora (CUAD, EDGAR, EUR-Lex) and benchmarked before and after tuning. Sample sizes, definitions and caveats: **[docs/METHODOLOGY.md](docs/METHODOLOGY.md)**

---

## The three systems

| # | System | Corpus | Headline measurement | Live |
|---|--------|--------|----------------------|------|
| 1 | **Due Diligence Agent** — *flagship* | CUAD + EDGAR | Unsupported answers 31% → 12% · ~€0.023/doc · ~4.2s end to end | [demo](#) · [code](due-diligence-agent/) |
| 2 | **Legal Intelligence Engine** | CUAD + EDGAR + EUR-Lex | Recall@3 0.71 → 0.83 vs baseline · faithfulness 0.84 (RAG) vs 0.81 (LoRA r8), n = 40 — no measurable difference · ~€0.002/query | [models](#) · [code](legal-intelligence-engine/) |
| 3 | **Research Briefing Agent** | Financial news | 94% tool-call success · p95 1.8s · 14 tests passing | [demo](#) · [code](research-briefing-agent/) |

### Why three and not four

Each system owns a distinct failure mode: orchestration, retrieval, tool calls. Systems that fail the same way are one system, so the contract Q&A baseline lives inside the Legal Intelligence Engine rather than beside it — it was that engine's baseline, and reporting a baseline as a separate deliverable inflates the count without adding a result.

### How they connect

**The Legal Intelligence Engine** is the retrieval core, and its history is the argument. It starts as a plain RAG pipeline over CUAD with an evaluation harness attached. A rank-8 LoRA tested against that baseline produced no measurable improvement in faithfulness at n = 40 — 0.84 against 0.81 — so RAG stayed, at roughly a quarter of the cost. The generation half being already close to its ceiling is what moved the work to the retrieval half: a domain-adapted embedding model trained with hard negative mining, so clauses that *read* alike but *mean* opposite things stop colliding. Recall@3 went 0.71 → 0.83. The engine exposes the result as an MCP server.

**The Research Briefing Agent** tests a different failure surface. Retrieval faithfulness is not what breaks an agent in production — tool calls are, and they break in ways an answer-quality metric cannot see. It measures that directly at 94% success and p95 1.8s, behind FastAPI, Docker, CI/CD and tracing.

**The Due Diligence Agent** composes both, calling the engine's MCP server as a tool rather than reimplementing retrieval.

Three demos would be three demos. One system that calls another through a standard protocol is an architecture.

---

## Run it yourself

```bash
git clone https://github.com/SaraDHimdi/ai-engineer-portfolio
cd ai-engineer-portfolio/legal-intelligence-engine

python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cp .env.example .env          # add your API key
python -m src.ingest          # builds the index from the sample corpus
python -m src.ask "What is the termination notice period?"
```

Reproduce the published numbers:

```bash
pytest                                    # 14 tests, all external calls mocked
python -m src.evaluate --config all       # writes to evidence/eval_runs/<date>/
```

The LoRA comparison above is a stored run, not a live one — the config and its raw output sit in `legal-intelligence-engine/evidence/`.

---

## Known limitations

Short version — full analysis in **[docs/LIMITATIONS.md](docs/LIMITATIONS.md)**, per-system detail in each `evidence/failure_analysis.md`.

- **Document parsing is the weakest link**, and it sits upstream of everything measured here. All three systems assume clean text extraction; every benchmark runs on corpora that were already clean text.
- **Cross-document reasoning is shallow.** Top-k similarity search does not reliably hold two documents in tension.
- **Evaluation sets are too small to be decisive.** 40 questions catches obvious regressions, not rare failure modes. Consolidating the contract baseline into the Legal Intelligence Engine puts one harness over one legal corpus, which is where that number grows next.

---

## Scope 2 — Arabic and French

Every metric above is measured on English corpora, so the French/Arabic civil-law positioning is currently a **claim, not a demonstration**. Scope 2 is the twelve-session programme that closes that gap: a text-layer inventory of the Bulletin Officiel archive, a five-system Arabic OCR comparison on hand-verified pages, and a **public French/Arabic legal retrieval benchmark verified by a jurist**. No such benchmark exists today.

Three Moroccan legal-AI products are already live — none publishes an evaluation harness, a benchmark, or a failure analysis, and none works on a firm's private corpus. That is the gap this scope targets.

→ **[docs/SCOPE-2-ARABIC-FRENCH.md](docs/SCOPE-2-ARABIC-FRENCH.md)** · sources, prior art, competitive landscape, honest risk

---

## Stack

**Orchestration** LangChain · LangGraph · LangSmith · MCP
**Retrieval** Chroma · Pinecone · Sentence Transformers · contrastive learning with hard negatives
**Evaluation** RAGAS · DeepEval · Guardrails AI
**Fine-tuning** HuggingFace PEFT · LoRA · bitsandbytes · TRL
**Production** FastAPI · Docker · GitHub Actions · pytest · Helicone

---

## Repo structure

```
ai-engineer-portfolio/
├── due-diligence-agent/          ← Flagship · legal + finance · composes the engine over MCP
├── legal-intelligence-engine/    ← Legal · RAG baseline, eval harness, retrieval model, MCP server
├── research-briefing-agent/      ← Finance · production agent
├── docs/                         ← Methodology, limitations, Scope 2
├── playbook/                     ← Build manual
├── SESSIONS.md                   ← Engineering log
└── demos/                        ← Video walkthroughs
```

Every system folder carries `src/`, `tests/`, `adr/`, and `evidence/` — the last containing `metrics.json`, raw evaluation runs, traces, and a failure analysis for every number claimed above.

---

## Contact

[LinkedIn](https://linkedin.com/in/sara-d-1a4795300) · [DocumentLab.ai](https://documentlab.ai) · [GitHub](https://github.com/SaraDHimdi)

MIT licensed — see [LICENSE](LICENSE). Code and assets © Sara Dhimdi / DocumentLab.ai.

---

*Built with intention. Measured before it ships.*
