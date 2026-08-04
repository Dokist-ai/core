<p align="center">
  <img src="assets/logo.png" alt="DocumentLab.ai" width="80"/>
</p>
<p align="center">
  <img src="https://img.shields.io/github/last-commit/SaraDHimdi/ai-engineer-portfolio?color=0c1a2e&style=flat-square" alt="Last commit"/>
  <img src="https://img.shields.io/github/repo-size/SaraDHimdi/ai-engineer-portfolio?color=0c1a2e&style=flat-square" alt="Repo size"/>
  <img src="https://img.shields.io/github/languages/top/SaraDHimdi/ai-engineer-portfolio?color=C8960C&style=flat-square" alt="Top language"/>
  <img src="https://img.shields.io/github/issues/SaraDHimdi/ai-engineer-portfolio?color=0c1a2e&style=flat-square" alt="Issues"/>
</p>
<p align="center">
  <em>Built with intention. Shipped with evidence.</em>
</p>

# Sara Dhimdi — AI Developer & Founder of DocumentLab.ai
Building RAG systems, LLM agents, and production pipelines for legal and financial document intelligence.

---

## About

I care about AI that is robust, interpretable, and genuinely useful.

**DocumentLab.ai** is my AI engineering studio, specialized in LLM-based document intelligence across research, analytics, automation, and customer service — not a horizontal generalist tool, but systems built and tuned for legal and financial documents specifically, including French- and Arabic-speaking, civil-law markets that most enterprise players don't serve.

Four systems, each proving a different core capability, each built so the underlying architecture is domain-agnostic — swap the document corpus and the same system serves legal or financial workflows.

---

## Projects

| # | Project | Vertical | What it does | Key metric | Status |
|---|---------|----------|--------------|------------|--------|
| 1 | **Due Diligence Agent for Legal & Financial Teams** — *Flagship* | ⚖️ 🏦 Both | 3-agent orchestration. Agent 1 ingests documents. Agent 2 retrieves context + searches the web — including calling the MCP server from the Legal Intelligence Engine below as a composable tool. Agent 3 writes a structured risk assessment memo. Works for law firms and banks. 3 ADRs documented. | Hallucination rate 31% → 12% · avg €0.023/document · 4.2s end-to-end | 🧢 Live |
| 2 | **Contract Q&A Assistant** | ⚖️ Legal | Q&A over NDAs and commercial contracts (CUAD dataset) with source attribution on every answer, stress-tested with a RAGAS harness across 4 configurations on a 40-question golden dataset, plus red-team and prompt injection testing and a RAG vs LoRA fine-tuning comparison on the same test set. Architecture is corpus-agnostic — the same pipeline runs equally well over financial filings. | Faithfulness 0.84 (RAG) vs 0.81 (LoRA rank 8) at 4x lower cost | 🧢 Live |
| 3 | **Research Briefing Agent** | 🏦 Finance | Two-agent LangGraph system: Agent 1 searches financial news, Agent 2 synthesises a structured briefing. Wrapped in FastAPI, Dockerised, CI/CD, LangSmith traced. Same architecture repurposes directly for legal/compliance monitoring — swap the search domain, keep the pipeline. | 94% tool call success · p95 1.8s · 14 pytest tests, 100% pass | 🧢 Live |
| 4 | **Legal Intelligence Engine** | ⚖️ Legal | LoRA ablation study on Mistral 7B (3 rank configs, CUAD + EDGAR + EUR-Lex — legal *and* financial corpora). Domain-adapted sentence transformer with hard negative mining flags unusual or risky clauses automatically. MCP server exposes the pipeline as a composable tool — integrated into the Due Diligence Agent above, tested with Claude Desktop. | Rank 8: 0.81 faithfulness at €0.002/query · Recall@3 0.71 → 0.83 vs OpenAI baseline · 2 models on HuggingFace Hub | 🧢 Live |

---

## Stack

| Layer | Tools |
|-------|-------|
| Language | Python 3.11+ |
| Orchestration | LangChain · LangGraph · LangSmith |
| LLM APIs | OpenAI API · Anthropic API |
| Vector DBs | Chroma · Pinecone |
| Evaluation | RAGAS · DeepEval · Guardrails AI |
| Fine-tuning | HuggingFace PEFT · LoRA · bitsandbytes · TRL |
| NLP | Sentence Transformers · Contrastive Learning |
| Infrastructure | MCP (Model Context Protocol) |
| Production | FastAPI · Docker · GitHub Actions · CI/CD |
| Monitoring | Helicone · LangSmith |
| Deployment | Vercel · Render · Streamlit Cloud · HuggingFace Hub |
| Tooling | pytest · ruff · pre-commit · python-dotenv · Git |

---

## Niche

**LLM-Based Document Intelligence for legal and financial services.**

- Multi-agent due diligence and risk assessment
- Contract analysis and clause retrieval
- Financial report Q&A and summarisation
- Fine-tuning and evaluation for domain-specific accuracy
- Agentic workflows for research, analytics, and automation
- RAG systems exposed as composable, interoperable infrastructure (MCP)
- French, Arabic, English · civil and common law — markets most enterprise legal-AI tools don't cover

---

## Repo Structure

```
ai-engineer-portfolio/
├── README.md
├── due-diligence-agent/          ← Flagship · Legal & Finance
├── contract-qa-assistant/        ← Legal
├── research-briefing-agent/      ← Finance
├── legal-intelligence-engine/    ← Legal
└── demos/                        ← Video walkthroughs
```

---

## Contact

- LinkedIn: [linkedin.com/in/sara-d-1a4795300](https://linkedin.com/in/sara-d-1a4795300)
- Studio: [DocumentLab.ai](https://documentlab.ai)
- GitHub: [github.com/SaraDHimdi](https://github.com/SaraDHimdi)

---
## 📄 License

This project is licensed under the [MIT License](LICENSE).

**The code and all assets of this project are a property of Sara Dhimdi / DocumentLab.ai.**

---


*Built with intention. Shipped with evidence.*
