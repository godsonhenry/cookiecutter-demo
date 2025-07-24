Project={{cookiecutter.project_slug}}
Venv_name={{cookiecutter.venv_name}}
python_version={{cookiecutter.python_version}}
requires-python={{cookiecutter.requires_python}}

venv:
	pip3 install nv
	uv venv .${Venv_name} --python $(python_version)

setup:
	pip3 install uv
	uv pip install -e .	--target .${Venv_name}/lib/python$(python_version)/site-packages
	uv sync --extra dev --active

linting:
	pip3 install uv
	python -m ruff format ${PROJECT}
	python -m ruff format --check ${PROJECT}
	Python -m ruff check --fix ${PROJECT}

test:
	pip3 install uv
	python -m pytest -v --disable-warnings --ignore=init_tests --cov=${PROJECT} tests/
	python -m coverage report -m --fail-under=90

build:
	uv build --no-sources