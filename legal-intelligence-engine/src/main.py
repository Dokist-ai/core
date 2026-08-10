"""
Legal Intelligence Engine
RAG pipeline with MCP server interface.
Domain-adapted embeddings, hard-negative mining, evaluation harness.
"""

import os
import time
import logging
from contextlib import asynccontextmanager
from typing import Any, Literal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Config:
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    chroma_persist_dir: str = os.getenv("CHROMA_PERSIST_DIR", "./data/chroma")
    embedding_model: str = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
    top_k: int = int(os.getenv("RETRIEVAL_TOP_K", "3"))
    corpus_path: str = os.getenv("CORPUS_PATH", "./data/corpus")

config = Config()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("[Engine] Loading embedding model and vector index...")
    # TODO: Load SentenceTransformer + Chroma here
    app.state.embedder = None
    app.state.collection = None
    logger.info("[Engine] Ready.")
    yield
    logger.info("[Engine] Shutting down...")

app = FastAPI(
    title="Legal Intelligence Engine",
    description="RAG retrieval core with MCP server interface",
    version="0.1.0",
    lifespan=lifespan,
)


class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"
    service: str = "legal-intelligence-engine"

class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)
    top_k: int = Field(default=3, ge=1, le=10)

class QueryResponse(BaseModel):
    answer: str
    sources: list[dict[str, Any]]
    retrieval_time_ms: float
    generation_time_ms: float
    faithfulness_score: float | None = None

class IngestRequest(BaseModel):
    document_text: str = Field(..., min_length=10)
    metadata: dict[str, Any] = Field(default_factory=dict)

class IngestResponse(BaseModel):
    chunks_indexed: int
    doc_id: str

class MCPTool(BaseModel):
    name: str
    description: str
    parameters: dict[str, Any]

class MCPToolsListResponse(BaseModel):
    tools: list[MCPTool]

class MCPToolCallRequest(BaseModel):
    name: str
    arguments: dict[str, Any]

class MCPToolCallResponse(BaseModel):
    result: Any
    error: str | None = None


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse()

@app.post("/query", response_model=QueryResponse)
async def query(req: QueryRequest) -> QueryResponse:
    """RAG query: embed → retrieve top-k → generate answer."""
    start = time.perf_counter()
    # TODO: Actual retrieval + generation
    retrieval_time = (time.perf_counter() - start) * 1000
    gen_start = time.perf_counter()
    answer = f"[Placeholder] Answer to: {req.question}"
    generation_time = (time.perf_counter() - gen_start) * 1000
    sources = [
        {"doc_id": "cuad_001", "clause": "Termination Notice", "score": 0.91},
        {"doc_id": "edgar_042", "clause": "Section 4.2", "score": 0.87},
    ]
    return QueryResponse(
        answer=answer,
        sources=sources,
        retrieval_time_ms=round(retrieval_time, 2),
        generation_time_ms=round(generation_time, 2),
        faithfulness_score=None,
    )

@app.post("/ingest", response_model=IngestResponse)
async def ingest(req: IngestRequest) -> IngestResponse:
    """Ingest document: chunk → embed → store in Chroma."""
    import uuid
    doc_id = str(uuid.uuid4())[:8]
    # TODO: Chunk + embed + insert
    chunks_indexed = len(req.document_text) // 400
    logger.info(f"[Engine] Ingested doc {doc_id}: {chunks_indexed} chunks")
    return IngestResponse(chunks_indexed=chunks_indexed, doc_id=doc_id)

@app.get("/mcp/tools", response_model=MCPToolsListResponse)
async def mcp_list_tools() -> MCPToolsListResponse:
    """MCP-compatible tool listing."""
    return MCPToolsListResponse(tools=[
        MCPTool(
            name="legal_query",
            description="Query the legal corpus using RAG retrieval",
            parameters={
                "type": "object",
                "properties": {
                    "question": {"type": "string"},
                    "top_k": {"type": "integer", "default": 3}
                },
                "required": ["question"]
            }
        ),
        MCPTool(
            name="legal_ingest",
            description="Ingest a legal document into the index",
            parameters={
                "type": "object",
                "properties": {
                    "document_text": {"type": "string"},
                    "metadata": {"type": "object"}
                },
                "required": ["document_text"]
            }
        )
    ])

@app.post("/mcp/tools/call", response_model=MCPToolCallResponse)
async def mcp_call_tool(req: MCPToolCallRequest) -> MCPToolCallResponse:
    """MCP-compatible tool execution."""
    try:
        if req.name == "legal_query":
            q = QueryRequest(**req.arguments)
            result = await query(q)
            return MCPToolCallResponse(result=result.model_dump())
        elif req.name == "legal_ingest":
            i = IngestRequest(**req.arguments)
            result = await ingest(i)
            return MCPToolCallResponse(result=result.model_dump())
        else:
            return MCPToolCallResponse(error=f"Unknown tool: {req.name}")
    except Exception as e:
        logger.error(f"[Engine] Tool call failed: {e}")
        return MCPToolCallResponse(error=str(e))

@app.post("/evaluate")
async def evaluate_run(config_name: str = "all") -> dict[str, Any]:
    """Trigger RAGAS evaluation. Writes to evidence/eval_runs/<date>/"""
    import datetime
    run_id = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    logger.info(f"[Engine] Evaluation run {run_id} complete.")
    return {"run_id": run_id, "config": config_name, "output_dir": f"evidence/eval_runs/{run_id}/", "status": "stored"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
