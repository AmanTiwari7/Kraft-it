# Makefile for Kraft-it Project
# Simple commands to manage the application

.PHONY: help install dev frontend backend test lint format clean

# Default target
help:
	@echo "Kraft-it - Available Commands:"
	@echo "================================"
	@echo "  make install   - Install all dependencies"
	@echo "  make dev       - Start both frontend and backend"
	@echo "  make frontend  - Start only frontend (Streamlit)"
	@echo "  make backend   - Start only backend (FastAPI)"
	@echo "  make test      - Run all tests"
	@echo "  make lint      - Check code quality"
	@echo "  make format    - Format code with Black"
	@echo "  make clean     - Clean temporary files"

# Install dependencies
install:
	@echo "📦 Installing dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt

# Start development environment (both servers)
dev:
	@echo "🚀 Starting Kraft-it in Dev Mode..."
	python start.py dev

# Start frontend only
frontend:
	@echo "🎨 Starting Frontend..."
	streamlit run streamlit_app/Home.py --server.port $(STREAMLIT_PORT)

# Start backend only
backend:
	@echo "📡 Starting Backend..."
	uvicorn api.main:app --reload --port $(BACKEND_PORT) --host 0.0.0.0

# Run tests
test:
	@echo "🧪 Running tests..."
	pytest tests/ -v --cov=kraft_it --cov-report=term-missing

# Check code quality
lint:
	@echo "🔍 Checking code quality..."
	flake8 kraft_it/ api/ streamlit_app/ --max-line-length=127
	@echo "✅ Linting complete!"

# Format code
format:
	@echo "✨ Formatting code..."
	black kraft_it/ api/ streamlit_app/ tests/
	@echo "✅ Formatting complete!"

# Clean temporary files
clean:
	@echo "🧹 Cleaning temporary files..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache .coverage htmlcov
	@echo "✅ Cleanup complete!"