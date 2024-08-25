python ?=.venv/bin/python
npm ?= npm
uv ?= uv

help:
	@echo make help - display this message
	@echo make devpy - run dev server \(watch\)
	@echo make devcss - run tailwind build \(watch\)
	@echo make build - build for production
	@echo make deps - generate requirements.txt from pyproject.toml using uv
	@echo make sync - sync venv with requirements.txt using uv, install npm dependencies
	@echo make makemigrations - generate migrations for db
	@echo make migrate - migrate db
	@echo make dump - dump data from db to json files
	@echo make load - load data to db from json files

devpy:
	${python} heliumos_website/manage.py runserver

devcss:
	${npm} run tw-watch

build:
	rm -rdf dist static
	${npm} run tw-build
	${python} heliumos_website/manage.py distill-local --force --collectstatic dist

deps:
	${uv} pip compile pyproject.toml -o requirements.txt --generate-hashes


sync:
	${uv} pip sync requirements.txt
	${npm} install

makemigrations:
	${python} heliumos_website/manage.py makemigrations

migrate:
	${python} heliumos_website/manage.py migrate

dump:
	${python} heliumos_website/manage.py dumpdata www.BlogPost > data/blog_post.json
	${python} -m json.tool data/blog_post.json data/blog_post.json
	${python} heliumos_website/manage.py dumpdata www.QuestionAnswer > data/question_answer.json
	${python} -m json.tool data/question_answer.json data/question_answer.json
	${python} heliumos_website/manage.py dumpdata www.Release > data/release.json
	${python} -m json.tool data/release.json data/release.json
	${python} heliumos_website/manage.py dumpdata sites.Site > data/sites.json
	${python} -m json.tool data/sites.json data/sites.json

load:
	${python} heliumos_website/manage.py loaddata data/blog_post.json
	${python} heliumos_website/manage.py loaddata data/question_answer.json
	${python} heliumos_website/manage.py loaddata data/release.json
	${python} heliumos_website/manage.py loaddata data/sites.json
