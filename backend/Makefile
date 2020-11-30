.PHONY: migrate
migrate:
	docker-compose run backend python manage.py migrate

.PHONY: makemigrations
makemigrations:
	docker-compose run backend python manage.py makemigrations

.PHONY: test
test:
	echo 'test'

.PHONY: up
up:
	docker-compose up -d

.PHYTON: sh
sh:
	docker-compose run backend sh
