Project={{cookiecutter.project_slug}}
Venv_name=Venv
python_version={{cookiecutter.python_version}}
requires-python={{cookiecutter.requires_python}}

venv:
	pip3 install nv
	nv venv .${Venv_name} --python=$(python_version)

setup:
	pip3 install uv
	uv pip install -e .	--target .${Venv_name}/lib/python$(python_version)/site-packages
	uv sync --extra dev --active