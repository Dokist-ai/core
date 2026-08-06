<p align="center">
  <img src="assets/logo.png" alt="DocumentLab.ai" width="80"/>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-0c1a2e?style=flat-square" alt="License: MIT"/>
  <img src="https://img.shields.io/badge/python-3.11+-0c1a2e?style=flat-square" alt="Python 3.11+"/>
  <img src="https://img.shields.io/badge/evaluation-RAGAS-C8960C?style=flat-square" alt="Evaluated with RAGAS"/>
</p>
 
 # DocumentLab

**RAG systems, LLM agents, and evaluation harnesses for legal and financial documents.**
Four systems, one niche, every claim traced to a raw run in `evidence/`.

> **These are reference systems, not client deployments.** Built on public corpora (CUAD, EDGAR, EUR-Lex) and benchmarked before and after tuning. Sample sizes, definitions and caveats: **[docs/METHODOLOGY.md](docs/METHODOLOGY.md)**

---

## The four systems

| # | System | Corpus | Headline measurement | Live |
|---|--------|--------|----------------------|------|
| 1 | **Due Diligence Agent** — *flagship* | CUAD + EDGAR | Unsupported answers 31% → 12% · ~€0.023/doc · ~4.2s end to end | [demo](#) · [code](due-diligence-agent/) |
| 2 | **Contract Q&A Assistant** | CUAD | Faithfulness 0.84 (RAG) vs 0.81 (LoRA r8), n = 40 — no measurable difference; RAG chosen at ~4× lower cost | [demo](#) · [code](contract-qa-assistant/) |
| 3 | **Research Briefing Agent** | Financial news | 94% tool-call success · p95 1.8s · 14 tests passing | [demo](#) · [code](research-briefing-agent/) |
| 4 | **Legal Intelligence Engine** | CUAD + EDGAR + EUR-Lex | Recall@3 0.71 → 0.83 vs baseline · rank-8 LoRA at ~€0.002/query | [models](#) · [code](legal-intelligence-engine/) |

### How they connect

System 2 is the base RAG pipeline with evaluation attached. System 4 improves the retrieval half — a domain-adapted embedding model trained with hard negative mining, so clauses that *read* alike but *mean* opposite things stop colliding — and exposes the pipeline as an MCP server. System 3 proves the agent layer survives production: FastAPI, Docker, CI/CD, tracing. System 1 composes all of it, calling System 4's MCP server as a tool.

Four demos would be four demos. One system that calls another through a standard protocol is an architecture.

---

## Run it yourself

```bash
git clone https://github.com/DocumentLab-ai/core
cd core/contract-qa-assistant

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

---

## Known limitations

Short version — full analysis in **[docs/LIMITATIONS.md](docs/LIMITATIONS.md)**, per-system detail in each `evidence/failure_analysis.md`.

- **Document parsing is the weakest link**, and it sits upstream of everything measured here. All four systems assume clean text extraction; every benchmark runs on corpora that were already clean text.
- **Cross-document reasoning is shallow.** Top-k similarity search does not reliably hold two documents in tension.
- **Evaluation sets are too small to be decisive.** 40 questions catches obvious regressions, not rare failure modes.

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
├── due-diligence-agent/          ← Flagship · legal + finance
├── contract-qa-assistant/        ← Legal · RAG baseline + eval harness
├── research-briefing-agent/      ← Finance · production agent
├── legal-intelligence-engine/    ← Legal · retrieval + MCP server
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
