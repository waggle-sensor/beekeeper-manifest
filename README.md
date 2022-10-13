# Beekeeper Manifest
The beekeeper manifest database is used to store the manifests of a node on the ecosystem.

## Docker-compose
Make a copy of the `.env.example` environment variables and modify to your needs:
```
cp .env.example .env
```

Start backend services (db + api):
```
docker-compose up --build
```

Make Django migrations:
```
docker exec -it manifest-api python manage.py migrate
```

* After migrating data tables, run the following command to start your Django server.
```
docker exec -it manifest-api python manage.py runserver
```

Create superuser to login to `/admin/` page:
```
docker exec -it manifest-api python manage.py createsuperuser
```
The last command will prompt you for the admin username and password.

* Your Django server will run on `http://0.0.0.0:8000/`. Head over to your browser and enter `http://0.0.0.0:8000/admin` to access the admin page. Enter the account and password you created at the last step to log in.
