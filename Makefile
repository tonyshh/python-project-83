PORT ?= 8000
DB_URL = page_analyzer

dev:
	poetry run flask --app page_analyzer:app --debug run

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) page_analyzer:app

install:
	poetry install

build:
	./build.sh

schema-db:
	psql $(DB_URL) < database.sql

schema-db-render:
	psql $(DATABASE_URL) < database.sql

build-render: install schema-db-render

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

lint:
	poetry run flake8


.PHONY: dev install test lint selfcheck check build
