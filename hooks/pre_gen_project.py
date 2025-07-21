#!/use/bin/env python

"""Pre-generation hook for cookiecutter-python-project.
This script is executed before the project generation starts."""

import re
import sys

def validate_project_name(project_name):
    """Validate the project name to ensure it follows Python package naming conventions."""
    print(project_name)
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', project_name):
        print(f"Error: '{project_name}' is not a valid Python package name.")
        sys.exit(1)

def validate_python_version():
    """Validate the Python version to ensure it is supported."""
    python_version = "{cookiecutter.python_version}"
    min_version = "{cookiecutter.min_python_version}"
    max_version = "{cookiecutter.max_python_version}"

    if python_version < min_version:
        print(f"Error: This project requires Python {min_version} or higher.")
        sys.exit(1)
    if python_version > max_version:
        print(f"Error: This project does not support Python {max_version} or higher.")
        sys.exit(1)


if __name__ == "__main__":
    project_name = "{{cookiecutter.project_name}}"
    
    validate_project_name(project_name)
    validate_python_version()
    
    print("Pre-generation checks passed. Proceeding with project generation.")