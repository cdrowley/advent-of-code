all: py_venv py_pip_install

py_venv:
		@echo "Setting up python virtual environment (venv)..."
		@python3 -m venv venv

py_pip_install:
		@echo "Pip installing from requirements.txt..."
		@venv/bin/python -m pip install -r requirements.txt