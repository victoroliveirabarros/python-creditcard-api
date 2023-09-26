test:
	ENV='test' pytest --cov-config=.coveragerc --cov-report html --cov=. app/

install_requirements:
	pip install -r development/requirements.txt

format:
	autopep8 --in-place -r --exclude="venv,main.py" .; isort --skip=main/routes/__init__.py .

dev:
	cd development && docker compose up

dev-build:
	cd development && docker compose up --build
