# Instala o gerenciador de pacotes (poetry) e requirements.txt
install_requirements:
	pip install poetry && pip install -r development/requirements.txt

# Formata o código-fonte de acordo com o padrão PEP8
format:
	cd app && poetry run autopep8 --exclude="main.py" .; poetry run isort --skip=main/routes/__init__.py .

# Checa se o código-fonte está de acordo com o padrão PEP8
check_format:
	poetry run pycodestyle ./app; poetry run isort --check-only ./app

# Checa se o código-fonte possui erros de sintaxe
check_errors:
	poetry run pylint app/ --disable=all --enable=e,f

dev:
	cd development && docker compose up

dev-build:
	cd development && docker compose up --build

# Roda os testes unitários
test:
	ENV='test' poetry run pytest --cov-config=.coveragerc --cov-report html --cov=. tests/
