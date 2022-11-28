# Beekeeper Manifest

The beekeeper manifest database is used to store the manifests of a node on the ecosystem.

## Local docker-compose environment

Start services:
```
make start
```

Once the services have started, perform database migrations:
```
make migrate
```

Create superuser to login to `/admin/` page:
```
make createsuperuser
```
The last command will prompt you for the admin username and password.

* Your Django server will run on `http://localhost:8000/`. Head over to your browser and enter `http://localhost:8000/admin` to access the admin page. Enter the account and password you created at the last step to log in.

## Initialize Sage node and sensor data

The purpose of the initialization process is to be easily load data into BK-Manifest and allow developers to easily standup their own instance of BK-Manifest based on their own node's metadata.
