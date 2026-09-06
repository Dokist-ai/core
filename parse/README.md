# dokist-parse

Memory-safe PDF text extraction with bilingual (AR/FR/EN) normalization for the DOKIST legal RAG stack.

## Why Rust?

This crate sits at the highest-risk boundary in the DOKIST pipeline:

1. **Char-offset span integrity** — A buffer miscalculation in PDF parsing invalidates every downstream citation. Rust's ownership model makes off-by-one errors unrepresentable.
2. **Normalization consistency** — Arabic legal text requires NFKC + alef/ya/ta-marbuta unification + tatweel stripping. Doing this in Python with `unicodedata` + regex risks divergence between indexer and query paths. One Rust function, called from both sides, eliminates that risk.

## Quick start

```bash
pip install maturin
maturin develop
python -c "from dokist_parse import normalize_text; print(normalize_text('العربية', 'ar'))"
```

## Run tests

```bash
cargo test          # Rust unit tests (normalization invariants, offset contiguity)
pytest              # Python integration tests (mocked, zero external calls)
```

## Build production image

```bash
docker build -t dokist-parse:latest .
```

## License

MIT — see top-level `LICENSE` in the DOKIST monorepo.
