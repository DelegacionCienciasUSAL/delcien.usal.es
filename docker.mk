# Commands for managing the development docker-compose setup
include settings.mk

docker-build:
	docker build -t $(DOCKER_IMAGE_NAME) .

compose-build:
	docker-compose build

compose-run:
	docker-compose up

compose-migrate:
	docker-compose run web $(DJANGO_MANAGE) \
		makemigrations \
		--settings=delcien.settings_compose
	docker-compose run web $(DJANGO_MANAGE) \
		migrate \
		--settings=delcien.settings_compose

compose-createsuperuser:
	docker-compose run web $(DJANGO_MANAGE) \
		createsuperuser \
		--settings=delcien.settings_compose

.PHONY: docker-build compose-build compose-run compose-migrate compose-createsuperuser