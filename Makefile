.PHONY: help sync smoke all reproduce lint typecheck test docker-build docker-smoke clean

UV_RUN := uv run --all-extras

help:
	@echo "Targets:"
	@echo "  sync           install deps from uv.lock (all WP groups + dev)"
	@echo "  smoke          run canary smoke tests (< 90s)"
	@echo "  all            run the full pipeline on raw/ (stub until WP1 lands)"
	@echo "  reproduce      rebuild results from committed features (stub)"
	@echo "  lint           ruff format + check"
	@echo "  typecheck      mypy strict"
	@echo "  test           pytest with coverage"
	@echo "  docker-build   build the project image"
	@echo "  docker-smoke   run 'make smoke' inside the container"
	@echo "  clean          remove caches, venvs, build artefacts"

sync:
	uv sync --frozen --all-extras

smoke:
	$(UV_RUN) pytest tests/test_smoke.py -v

all:
	@echo "Pipeline entry point. Real implementation lands in WP1-4 plans."
	@echo "Stub exits 0."

reproduce:
	@echo "Reproducibility entry point. Real implementation lands later."
	@echo "Stub exits 0."

lint:
	$(UV_RUN) ruff format .
	$(UV_RUN) ruff check --fix .

typecheck:
	$(UV_RUN) mypy src tests

test:
	$(UV_RUN) pytest tests/ -v --cov=src/choir_entanglement --cov-report=term-missing

docker-build:
	docker build -t choir-entanglement:dev .

docker-smoke: docker-build
	docker run --rm choir-entanglement:dev make smoke

clean:
	rm -rf .venv .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
