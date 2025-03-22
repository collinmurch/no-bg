.PHONY: setup run run-docker lint format test clean docker-clean help

# Variables
VENV_DIR = .venv
DOCKER_IMAGE = bg-remover
PORT = 8080

# Setup development environment with uv
setup:
	@echo "Setting up environment using uv..."
	uv venv
	@echo "Installing dependencies from pyproject.toml..."
	uv pip install -e .
	@echo "Setup complete!"

# Run the application (local)
run:
	uv run app.py

# Run the application (Docker)
run-docker:
	docker build -t $(DOCKER_IMAGE) .
	docker run -p $(PORT):$(PORT) $(DOCKER_IMAGE)

# Run linting
lint:
	uv run ruff check .

# Run formatting
format:
	uv run ruff format .

# Run tests
test:
	uv run pytest

# Clean up
clean:
	rm -rf $(VENV_DIR) __pycache__ .pytest_cache .ruff_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name *.egg-info -exec rm -rf {} +
	find . -type f -name *.pyc -delete

# Docker clean up
docker-clean:
	docker rmi $(DOCKER_IMAGE) || true
	docker image prune -f

# Help
help:
	@echo "Available commands:"
	@echo "  make setup         - Set up development environment using uv"
	@echo "  make run           - Run the application locally"
	@echo "  make run-docker    - Build and run the application using Docker"
	@echo "  make lint          - Run linting checks"
	@echo "  make format        - Format code"
	@echo "  make test          - Run tests"
	@echo "  make clean         - Clean up temporary files"
	@echo "  make docker-clean  - Clean up Docker images"