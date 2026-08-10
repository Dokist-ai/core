# Engineering Log

## 2026-08-10 — Docker build fixed, CITATION.cff added
**Goal:** Fix the CI build blocking PR #52 and add proper citation metadata.  
**What happened:**  
- Build failed because `legal-intelligence-engine/requirements.txt` was missing. Added empty file to satisfy Dockerfile COPY.
- Build succeeded but cache export is slow (~15 min). Decided to keep `cache-to: type=gha` for now.
- Added `CITATION.cff` for GitHub's native citation button. Kept README section as a short pointer.
- Learned: `COPY` in Docker is relative to build context, not filesystem root.

**Decisions:**  
- Will skip `push: true` on PR builds later to save time. Not urgent now.
- Will add `version` and `doi` to CFF only after first stable release tag.

**Next unknown:**  
- How to reduce Docker image size? Currently pulling heavy LangChain deps. Maybe slim base image or multi-stage build?
