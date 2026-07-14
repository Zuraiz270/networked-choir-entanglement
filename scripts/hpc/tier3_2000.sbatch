#!/bin/bash
# Tier-3 latency grid at 2000-shuffle null, one SLURM array task per (piece, level).
#
# Values below are validated on NHR@FAU TinyGPU (job 1744899, 140/140 cells,
# 2026-07-14). On a different cluster, adjust --partition/--gres from `sinfo`
# and local policy.
#
# Submit (from the repo root on the cluster, after `uv sync --extra all`):
#   python -m scripts.hpc.make_cells > scripts/hpc/cells.txt
#   N=$(wc -l < scripts/hpc/cells.txt)
#   sbatch --array=1-${N} scripts/hpc/tier3_2000.sbatch
#
#SBATCH --job-name=tier3-2000
#SBATCH --partition=work          # NHR@FAU TinyGPU; adjust for other clusters
#SBATCH --gres=gpu:1              # TinyGPU mandates >=1 GPU per job (CPU-only work still needs it)
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00
#SBATCH --output=scripts/hpc/logs/%x_%a.out
# NOTE: no --mem-per-cpu: TinyGPU forbids explicit memory requests on GPU jobs.

set -euo pipefail
export PATH="$HOME/.local/bin:$PATH"   # uv lives here; the SLURM batch env is not the login env
mkdir -p scripts/hpc/logs data/processed/tier3/shards

CELL=$(sed -n "${SLURM_ARRAY_TASK_ID}p" scripts/hpc/cells.txt)
DATASET=$(echo "$CELL" | cut -d' ' -f1)
PIECE=$(echo "$CELL" | cut -d' ' -f2)
LEVEL=$(echo "$CELL" | cut -d' ' -f3)

echo "[$(date)] task ${SLURM_ARRAY_TASK_ID}: ${DATASET} / ${PIECE} / ${LEVEL}"

# --no-sync is load-bearing: `uv run` without it syncs the venv against the
# core spec, and concurrent tasks doing that stripped the extras mid-run on
# 2026-07-14 (65 tasks died with ModuleNotFoundError). Tasks must treat the
# venv as read-only; sync once on the login node with `uv sync --extra all`.
uv run --no-sync python -m scripts.tier3_latency_grid \
  --dataset "${DATASET}" \
  --pieces "${PIECE}" \
  --levels "${LEVEL}" \
  --shuffles 2000 \
  --out "data/processed/tier3/shards/${DATASET}__${PIECE}__${LEVEL}.csv"

echo "[$(date)] done"
