.PHONY: help sync smoke all reproduce ieee-report lint typecheck test clean

UV_RUN := uv run --all-extras

help:
	@echo "Targets:"
	@echo "  sync           install deps from uv.lock (all WP groups + dev)"
	@echo "  smoke          run canary smoke tests (< 90s)"
	@echo "  all            run tests and rebuild final report artifacts"
	@echo "  reproduce      rebuild final statistics, figure, and PDF"
	@echo "  ieee-report    build the separate IEEE-style report PDF"
	@echo "  lint           ruff format + check"
	@echo "  typecheck      mypy strict"
	@echo "  test           pytest with coverage"
	@echo "  clean          remove caches, venvs, build artefacts"

sync:
	uv sync --frozen --all-extras

smoke:
	$(UV_RUN) pytest tests/test_smoke.py -v

all:
	$(MAKE) test
	$(MAKE) reproduce

reproduce:
	$(UV_RUN) python -m scripts.h1_paired_test
	$(UV_RUN) python -m scripts.h2_centralization_test
	$(UV_RUN) python -m scripts.tier3_corpus_figure
	$(UV_RUN) python -m scripts.render_report

ieee-report:
	$(UV_RUN) python -m scripts.render_report_ieee

lint:
	$(UV_RUN) ruff format .
	$(UV_RUN) ruff check --fix .

typecheck:
	$(UV_RUN) mypy src tests

test:
	$(UV_RUN) pytest tests/ -v --cov=src/choir_entanglement --cov-report=term-missing

clean:
	rm -rf .venv .pytest_cache .mypy_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
