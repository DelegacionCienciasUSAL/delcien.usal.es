# Commands for managing the development docker-compose setup
include settings.mk

docker-build:
	docker build -t $(DOCKER_IMAGE_NAME) .

compose-build:
	docker-compose build

compose-run:
	docker-compose up

compose-stop:
	docker-compose down

compose-migrate:
	docker-compose run web $(DJANGO_MANAGE) \
		makemigrations \
		--settings=delcien.settings_compose && \
		$(DJANGO_MANAGE) \
		migrate \
		--settings=delcien.settings_compose

	docker-compose run web $(DJANGO_MANAGE) \
		makemigrations delcien \
		--settings=delcien.settings_compose && \
		$(DJANGO_MANAGE) \
		migrate delcien \
		--settings=delcien.settings_compose

	docker-compose run web $(DJANGO_MANAGE) \
		makemigrations inicio \
		--settings=delcien.settings_compose && \
		$(DJANGO_MANAGE) \
		migrate inicio \
		--settings=delcien.settings_compose

compose-prune:
	docker-compose down

	rm -f .src/apps/*/migrations/0*.py

compose-bash:
	docker-compose run web bash

compose-createsuperuser:
	docker-compose run web $(DJANGO_MANAGE) \
		createsuperuser \
		--settings=delcien.settings_compose

.PHONY: docker-build compose-build compose-run compose-migrate compose-createsuperuser