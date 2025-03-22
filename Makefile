.PHONY: setup run run-docker lint format test clean

# Variables
VENV_DIR = venv
PYTHON = python
DOCKER_IMAGE = bg-remover
PORT = 5000

# Setup development environment
setup:
	$(PYTHON) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install uv
	$(VENV_DIR)/bin/uv pip install -r requirements.txt
	$(VENV_DIR)/bin/uv pip install ruff pytest

# Run the application (local)
run:
	$(VENV_DIR)/bin/python app.py

# Run the application (Docker)
run-docker:
	docker build -t $(DOCKER_IMAGE) .
	docker run -p $(PORT):$(PORT) $(DOCKER_IMAGE)

# Run linting
lint:
	$(VENV_DIR)/bin/ruff check .

# Run formatting
format:
	$(VENV_DIR)/bin/ruff format .

# Run tests
test:
	$(VENV_DIR)/bin/pytest

# Clean up
clean:
	rm -rf $(VENV_DIR) __pycache__ .pytest_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name *.egg-info -exec rm -rf {} +
	find . -type f -name *.pyc -delete

# Help
help:
	@echo "Available commands:"
	@echo "  make setup         - Set up development environment"
	@echo "  make run           - Run the application locally"
	@echo "  make run-docker    - Build and run the application using Docker"
	@echo "  make lint          - Run linting checks"
	@echo "  make format        - Format code"
	@echo "  make test          - Run tests"
	@echo "  make clean         - Clean up temporary files"