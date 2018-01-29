SHELL=/bin/bash

timestamp := $(shell date +"%Y-%m-%d-%H-%M")
env := $(shell cat .env | grep "MV2_ENV")
usr := $(shell id -u):$(shell id -g)

################################################################################
# self documenting makefile
################################################################################
.DEFAULT_GOAL := help
.PHONY: help
## print available targets
help: bold = $(shell tput bold; tput setaf 3)
help: reset = $(shell tput sgr0)
help:
	@echo
	@sed -nr \
		-e '/^## /{s/^## /    /;h;:a;n;/^## /{s/^## /    /;H;ba};' \
		-e '/^[[:alnum:]_\-]+:/ {s/(.+):.*$$/$(bold)\1$(reset):/;G;p};' \
		-e 's/^[[:alnum:]_\-]+://;x}' ${MAKEFILE_LIST}
	@echo

################################################################################
# Only need to run once on first launch
.PHONY: init

init:
	python manage.py migrate
	python manage.py collectstatic
	python manage.py createsuperuser

# Executes automata tests
.PHONY: test

test:
	coverage run --source=/code/ /code/manage.py test -v 2
	echo -n "Creating HTML... "
	coverage html
	echo "Done."

# Start django
.PHONY: start

start:
	python manage.py migrate
	python manage.py collectstatic
	sudo docker-compose up -d
