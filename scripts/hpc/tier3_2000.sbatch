#!/bin/bash
# Tier-3 latency grid at 2000-shuffle null, one SLURM array task per piece.
#
# BEFORE SUBMITTING, fill the two <PLACEHOLDERS> below from your cluster's
# `sinfo` / documentation. Everything else is ready.
#
# Submit (from the repo root on the cluster):
#   python -m scripts.hpc.make_cells > scripts/hpc/cells.txt
#   N=$(wc -l < scripts/hpc/cells.txt)
#   sbatch --array=1-${N} scripts/hpc/tier3_2000.sbatch
#
#SBATCH --job-name=tier3-2000
#SBATCH --partition=<PARTITION>          # from `sinfo` on your cluster
#SBATCH --account=<ACCOUNT_IF_REQUIRED>  # delete this line if not needed
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --time=24:00:00
#SBATCH --output=scripts/hpc/logs/%x_%a.out

set -euo pipefail
mkdir -p scripts/hpc/logs data/processed/tier3/shards

CELL=$(sed -n "${SLURM_ARRAY_TASK_ID}p" scripts/hpc/cells.txt)
DATASET=$(echo "$CELL" | cut -d' ' -f1)
PIECE=$(echo "$CELL" | cut -d' ' -f2)

echo "[$(date)] task ${SLURM_ARRAY_TASK_ID}: ${DATASET} / ${PIECE}"

uv run python -m scripts.tier3_latency_grid \
  --dataset "${DATASET}" \
  --pieces "${PIECE}" \
  --shuffles 2000 \
  --out "data/processed/tier3/shards/${DATASET}__${PIECE}.csv"

echo "[$(date)] done"
