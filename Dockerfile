# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY due-diligence-agent/requirements.txt ./due-diligence-agent/requirements.txt
COPY legal-intelligence-engine/requirements.txt ./legal-intelligence-engine/requirements.txt
COPY research-briefing-agent/requirements.txt ./research-briefing-agent/requirements.txt

RUN pip install --no-cache-dir \
    -r due-diligence-agent/requirements.txt \
    -r legal-intelligence-engine/requirements.txt \
    -r research-briefing-agent/requirements.txt

COPY due-diligence-agent/src ./due-diligence-agent/src
COPY legal-intelligence-engine/src ./legal-intelligence-engine/src
COPY research-briefing-agent/src ./research-briefing-agent/src

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# CHANGE THIS LINE to your actual entrypoint:
CMD ["python", "-m", "legal_intelligence_engine.src.server"]
