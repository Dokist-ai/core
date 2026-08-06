<p align="center">  <img src="assets/logo.png" alt="DocumentLab.ai" width="80"/></p><p align="center">  <img src="https://img.shields.io/github/last-commit/SaraDHimdi/ai-engineer-portfolio?color=0c1a2e&style=flat-square" alt="Last commit"/>  <img src="https://img.shields.io/github/repo-size/SaraDHimdi/ai-engineer-portfolio?color=0c1a2e&style=flat-square" alt="Repo size"/>  <img src="https://img.shields.io/github/languages/top/SaraDHimdi/ai-engineer-portfolio?color=C8960C&style=flat-square" alt="Top language"/>  <img src="https://img.shields.io/github/issues/SaraDHimdi/ai-engineer-portfolio?color=0c1a2e&style=flat-square" alt="Issues"/></p><p align="center">  
<p align="center"> <em>Document intelligence for legal and financial text.</em> </p>

# Sara Dhimdi — AI Engineer

**DocumentLab.ai** — RAG systems, LLM agents, and evaluation harnesses for legal and financial documents, with a focus on French- and Arabic-speaking civil-law markets.

---

## Read this first

These are **four reference systems**, built on public legal and financial corpora (CUAD, EDGAR, EUR-Lex) and benchmarked before and after tuning. They are not client deployments — no law firm or bank has shipped any of this. When that changes, this line changes.

Every number below comes from my own harness. The harness, the golden datasets, and the raw results are in the repositories, so you can disagree with my methodology rather than take my word for it. Where a sample is too small to support a strong claim, I say so instead of rounding it into one.

---

## How to read the numbers

Three things that matter more than the headline figures:

**Sample sizes are small.** The main golden dataset is 40 questions. At n = 40, the 95% interval around a score of 0.84 is roughly ±0.11. That means 0.84 and 0.81 are *not* distinguishable — anyone who presents that gap as one system beating another is overreading their own data. I've stated the comparisons accordingly.

**"Faithfulness" is a specific thing.** It measures whether an answer is supported by the chunks that were actually retrieved. It does **not** measure whether the answer is legally correct, whether retrieval found the right clause in the first place, or whether the source document was parsed correctly. A system can score well on faithfulness and still be wrong in ways that matter.

**Retrieval and generation are measured separately** where noted. When end-to-end quality drops, that split is the only way to know which half broke.

> `[n = TK]` marks a figure whose sample size I have not yet documented publicly. Those are being backfilled; treat them as unverified until they aren't.

---

## The four systems

They are one architecture told in four parts, not four unrelated demos.

| # | System | Corpus | What it proves | Headline measurement |
|---|--------|--------|----------------|----------------------|
| 1 | **Due Diligence Agent** — *flagship* | CUAD + EDGAR | Multi-agent orchestration and tool composition | Unsupported answers 31% → 12% `[n = TK]` · ~€0.023/doc · ~4.2s end to end |
| 2 | **Contract Q&A Assistant** | CUAD | RAG baseline with a real evaluation harness | Faithfulness 0.84 (RAG) vs 0.81 (LoRA r8), n = 40 — **no measurable difference**; RAG chosen at ~4× lower cost |
| 3 | **Research Briefing Agent** | Financial news | Production engineering, not notebooks | 94% tool-call success `[n = TK]` · p95 1.8s · 14 tests passing |
| 4 | **Legal Intelligence Engine** | CUAD + EDGAR + EUR-Lex | Retrieval quality and interoperability | Recall@3 0.71 → 0.83 vs OpenAI baseline `[n = TK]` · rank-8 LoRA at ~€0.002/query |

### How they connect

System 2 is the base RAG pipeline with evaluation attached. System 4 improves the retrieval half — a domain-adapted embedding model trained with hard negative mining, so clauses that *read* alike but *mean* opposite things stop colliding — and exposes the whole pipeline as an MCP server. System 3 proves the agent layer survives contact with production: FastAPI, Docker, CI/CD, LangSmith tracing. System 1 composes all of it, calling System 4's MCP server as a tool.

That composition is the point. Four demos would be four demos. One system that calls another through a standard protocol is an architecture.

---

## What these systems get wrong

The section most portfolios don't have. These are known, current, and unfixed.

**Document parsing is the weakest link, and it sits upstream of everything measured above.** All four systems assume clean text extraction. Real legal documents arrive as scans, as multi-column layouts, as tables that flatten into nonsense, and — for Arabic — as OCR output that is frequently unusable. Every benchmark here runs on corpora that were already clean text. That is a significant caveat on all of it.

**Cross-document reasoning is shallow.** Retrieval returns the top-k chunks for a query. A question like "does the indemnity in the MSA conflict with the cap in the side letter?" requires holding two documents in tension, and top-k similarity search doesn't do that reliably.

**Evaluation sets are too small to be decisive.** 40 questions catches obvious regressions. It does not catch rare failure modes, and it cannot support fine-grained comparisons between configurations.

**The 12% that still fails is not random.** [TK — replace this with a real breakdown of the remaining failures on the flagship: how many are retrieval misses vs. generation errors vs. ambiguous ground truth. This is the single most credible paragraph you can add to this file.]

**Faithfulness is not correctness.** See above. A confidently-cited answer drawn from the wrong clause scores well and is still wrong.

---

## Where the retrieval stack actually stands

Being explicit about what is built versus what is planned, because "RAG system" covers a very wide range of rigour.

| Component | Status |
|-----------|--------|
| Chunking strategy | TK — document the actual strategy and why |
| Dense retrieval (embeddings) | Built · domain-adapted with hard negative mining (System 4) |
| Hybrid retrieval (BM25 + dense) | Not implemented — matters for legal text where exact terms carry weight |
| Reranking | Not implemented |
| Query rewriting / decomposition | Not implemented |
| Retrieval evaluated separately from generation | Partial — Recall@3 on System 4 only |
| Long-document handling (100+ pages) | Untested at scale |
| Document parsing / OCR | Not addressed — see limitations above |
| Prompt injection & red-team testing | Built (System 2) |
| Tracing and cost monitoring | Built (LangSmith, Helicone) |

---

## Data handling

For any client engagement: storage location, which models process the documents, and access are agreed in writing before work begins. NDA as standard. Self-hosted deployment available where documents cannot leave the client's infrastructure. GDPR and Moroccan Law 09-08 considerations are addressed per engagement rather than assumed.

*(TK — replace with your actual position once you've decided it. A law firm's first question is never your faithfulness score; it's where their client's document goes.)*

---

## Roadmap

**A French/Arabic legal-document retrieval benchmark, released publicly.** Every metric in this repository is measured on English corpora, which means the French/Arabic civil-law positioning above is currently a claim rather than a demonstration. Closing that gap is the priority: a few hundred question–answer pairs over French civil-law and Moroccan/OHADA texts, with gold answers, published openly. Nobody owns this benchmark. It is the thing that would make this portfolio non-substitutable.

**Arabic and French legal PDF parsing.** The unglamorous, durable problem. LLM APIs commoditise every few months; a clean extraction layer for civil-law documents does not.

**Hybrid retrieval and reranking**, with a before/after measurement on the existing golden set.

**Larger evaluation sets** — 40 questions is a starting point, not a benchmark.

**One deployed design partner**, named with permission.

---

## Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.11+ |
| Orchestration | LangChain · LangGraph · LangSmith |
| LLM APIs | OpenAI · Anthropic |
| Vector DBs | Chroma · Pinecone |
| Evaluation | RAGAS · DeepEval · Guardrails AI |
| Fine-tuning | HuggingFace PEFT · LoRA · bitsandbytes · TRL |
| Embeddings | Sentence Transformers · contrastive learning with hard negatives |
| Interoperability | MCP (Model Context Protocol) |
| Production | FastAPI · Docker · GitHub Actions |
| Monitoring | Helicone · LangSmith |
| Tooling | pytest · ruff · pre-commit · Git |

---

## Repo structure

```
ai-engineer-portfolio/
├── README.md
├── due-diligence-agent/          ← Flagship · legal + finance
├── contract-qa-assistant/        ← Legal · RAG baseline + eval harness
├── research-briefing-agent/      ← Finance · production agent
├── legal-intelligence-engine/    ← Legal · retrieval + MCP server
├── evaluation/                   ← Golden datasets, harnesses, raw results
└── demos/                        ← Video walkthroughs
```

---

## Contact

- LinkedIn: [linkedin.com/in/sara-d-1a4795300](https://linkedin.com/in/sara-d-1a4795300)
- Studio: [DocumentLab.ai](https://documentlab.ai)
- GitHub: [github.com/SaraDHimdi](https://github.com/SaraDHimdi)

## License

MIT — see [LICENSE](LICENSE). Code and assets © Sara Dhimdi / DocumentLab.ai.

---

*Built with intention. Measured before it ships.*
