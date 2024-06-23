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

devpy:
	${python} heliumos_website/manage.py runserver

devcss:
	${npm} run tw-watch

build:
	rm -rdf dist static
	${npm} run tw-build
	${python} heliumos_website/manage.py distill-local --force --collectstatic dist

deps:
	${uv} pip compile pyproject.toml -o requirements.txt

sync:
	${uv} pip sync requirements.txt
	${npm} install
