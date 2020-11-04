SHELL:=/bin/bash
ARGS = $(filter-out $@,$(MAKECMDGOALS))
MAKEFLAGS += --silent
BASE_PATH=${PWD}
PYTHON_EXEC=pipenv run
DOCKER_COMPOSE_FILE=$(shell echo -f docker-compose.yml)


_drop_db:
	docker-compose ${DOCKER_COMPOSE_FILE} stop db
	docker-compose ${DOCKER_COMPOSE_FILE} rm db

_create_db:
	docker-compose ${DOCKER_COMPOSE_FILE} up -d db

recreate_db: _drop_db _create_db

up:
	docker-compose ${DOCKER_COMPOSE_FILE} up -d --remove-orphans --build

start:
	docker-compose ${DOCKER_COMPOSE_FILE} start "${ARGS}"

logs:
	docker-compose ${DOCKER_COMPOSE_FILE} logs -f "${ARGS}"

sh:
	docker-compose ${DOCKER_COMPOSE_FILE} exec "${ARGS}" ash

test:
	docker-compose ${DOCKER_COMPOSE_FILE} exec web ${PYTHON_EXEC} py.test "${ARGS}"

install:
	docker-compose ${DOCKER_COMPOSE_FILE} exec web pipenv install "${ARGS}"

dj:
	docker-compose ${DOCKER_COMPOSE_FILE} exec web ${PYTHON_EXEC} python ./manage.py ${ARGS}

stop:
	docker-compose ${DOCKER_COMPOSE_FILE} stop "${ARGS}"

deps:
	docker-compose -f docker-compose.yml up -d db localstack

_migrate:
	cd api && pipenv run python ./manage.py migrate

createsu:
	docker-compose ${DOCKER_COMPOSE_FILE} exec web ${PYTHON_EXEC} ./manage.py shell -c "from apps.accounts.models import User; User.objects.create_superuser('admin@stock.com', 'stock123'); print('Superuser created: admin@stock.com:stock123')"

_makemigrations:
	cd api && pipenv run python ./manage.py makemigrations

_runserver:
	cd api && pipenv run ./manage.py runserver

superuser:
	cd api && pipenv run python ./manage.py shell -c "from apps.accounts.models import User; User.objects.create_superuser('admin@stock.com', 'stock123'); print('Superuser created: admin@stock.com:stock123')"

shell_plus:
	cd api && pipenv run ./manage.py shell_plus
