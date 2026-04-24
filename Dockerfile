# syntax=docker/dockerfile:1.7
# Stage 1: build the venv with all deps + the package itself
FROM python:3.11.9-slim-bookworm AS builder

# Build-time system deps for any wheels that compile from source
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Pinned uv binary
COPY --from=ghcr.io/astral-sh/uv:0.10.10 /uv /usr/local/bin/uv

WORKDIR /app

# Copy lock + pyproject + README first so layer caches on code-only changes
COPY pyproject.toml uv.lock README.md ./
COPY src/ ./src/

RUN uv sync --frozen --all-extras --no-dev

# Stage 2: runtime image
FROM python:3.11.9-slim-bookworm

# Runtime system deps (ffmpeg for audio, libgl/libglib for opencv, make for Makefile targets)
RUN apt-get update && apt-get install -y --no-install-recommends \
        ffmpeg \
        libgl1 \
        libglib2.0-0 \
        make \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src
COPY pyproject.toml Makefile /app/
COPY tests /app/tests

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MPLBACKEND=Agg

WORKDIR /app

# Default entrypoint: smoke tests so `docker run <image>` is a working self-check
CMD ["make", "smoke"]
