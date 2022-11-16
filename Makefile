start:
	docker-compose up --build -d

stop:
	docker-compose down --volumes

migrate:
	docker-compose exec api python manage.py migrate

collectstatic:
	docker-compose exec api python manage.py collectstatic --no-input

createsuperuser:
	docker-compose exec api python manage.py createsuperuser

test:
	docker-compose exec api python manage.py test
	docker-compose exec api python manage.py check --deploy
