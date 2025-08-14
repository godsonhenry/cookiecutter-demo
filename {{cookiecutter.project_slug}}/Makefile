PROJECT={{cookiecutter.package_name}}
VENV_NAME={{cookiecutter.venv_name}}
PYTHON_VERSION={{cookiecutter.python_version}}
REQUIRES_PYTHON={{cookiecutter.requires_python}}
VENV_PATH = .${VENV_NAME}

.PHONY: venv setup linting test build clean help

help:
	@echo "Available targets:"
	@echo "  venv     - Create virtual environment"
	@echo "  setup    - Install package and dependencies"
	@echo "  linting  - Run code formatting and linting"
	@echo "  test     - Run tests with coverage"
	@echo "  build    - Build the package"
	@echo "  clean    - Remove virtual environment and build artifacts"

venv: 
	pip3 install uv
	uv venv .${VENV_NAME} --python ${PYTHON_VERSION}

setup: 
	pip3 install uv
	uv pip install -e . --target .${VENV_NAME}/lib/python${PYTHON_VERSION}/site-packages
	uv sync --extra dev --active

linting:
	pip3 install uv
	python -m ruff format src/${PROJECT}
	python -m ruff check --fix src/${PROJECT}
	python -m ruff format --check src/${PROJECT}

test:
	pip3 install uv
	python -m pytest -v --disable-warnings --ignore=init_tests --cov=src/${PROJECT} tests/
	# python -m coverage report -m --fail-under=90

build:
	uv build --no-sources

clean:
	rm -rf ${VENV_PATH}
	find . -type d -name "build" -exec rm -rf {} +
	find . -type d -name "dist" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
