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

setup: venv
	${VENV_PATH}/bin/uv pip install -e ".[dev]"

linting:
	${VENV_NAME}/bin/python -m ruff format src/${PROJECT}
	${VENV_NAME}/bin/python -m ruff check --fix src/${PROJECT}
	${VENV_NAME}/bin/python -m ruff format --check src/${PROJECT}

test:
	${VENV_NAME}/bin/python -m pytest -v --disable-warnings --ignore=init_tests --cov=src/${PROJECT} tests/
	${VENV_NAME}/bin/python -m coverage report -m --fail-under=90

build:
	${VENV_NAME}/bin/uv build --no-sources

clean:
	rm -rf ${VENV_PATH}
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -type f -name "*.pyc" -delete
