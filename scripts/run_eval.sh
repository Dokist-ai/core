#!/usr/bin/env bash
set -euo pipefail

RUN_DIR="eval_runs/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$RUN_DIR"

# TODO: replace with your real evaluation command
python -m dokist.eval --output "$RUN_DIR"

echo "Raw evaluation output saved to $RUN_DIR"
