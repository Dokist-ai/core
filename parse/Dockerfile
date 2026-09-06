# DOKIST Parse — Multi-stage build
# Stage 1: Compile the Rust extension with Maturin
# Stage 2: Slim Python runtime with the compiled wheel

# ---------------------------------------------------------------------------
# Builder
# ---------------------------------------------------------------------------
FROM rust:1.80-slim AS builder

WORKDIR /build

# System deps for PyO3 + maturin
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-venv pkg-config libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --break-system-packages maturin

# Copy manifests first for layer caching
COPY Cargo.toml pyproject.toml ./
COPY src ./src

# Build release wheel
RUN maturin build --release

# ---------------------------------------------------------------------------
# Runtime
# ---------------------------------------------------------------------------
FROM python:3.11-slim

WORKDIR /app

# Install the wheel built in stage 1
COPY --from=builder /build/target/wheels/*.whl ./wheels/
RUN pip install --no-cache-dir ./wheels/*.whl && rm -rf ./wheels

# Copy Python facade (tests, evidence scripts, etc.)
COPY dokist_parse ./dokist_parse

# Healthcheck: verify the Rust extension loads
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD python -c "from dokist_parse import normalize_text; print('ok')" || exit 1

CMD ["python", "-c", "from dokist_parse import normalize_text, parse_pdf_bytes; print('DOKIST parse ready')"]
