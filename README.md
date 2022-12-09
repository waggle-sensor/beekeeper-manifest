# Beekeeper Manifest

The beekeeper manifest database is used to store the manifests of a node on the ecosystem.

## Local docker-compose environment

Start services:
```
make start
```

Once the services have started, perform database migrations and prep static content:
```
make migrate
make collectstatic
```

If you plan on logging in to the admin page `/admin/`, you'll need to create a superuser:
```
make createsuperuser
```

The last command will prompt you for the admin username and password.

Your Django server will run on `http://localhost:8000/`. Head over to your browser and enter `http://localhost:8000/admin` to access the admin page. Enter the account and password you created at the last step to log in.

## Initialize Sage node and sensor data

The purpose of the initialization process is to be easily load data into BK-Manifest and allow developers to easily standup their own instance of BK-Manifest based on their own node's metadata.

To load node and hardware data, create a folder `data` under folder `ManifestApp`. Move `hardware.csv` and `nodedata.csv` under this folder. In the terminal, navigate to `/api/` then execute

```
docker-compose exec -T api python manage.py runscript load_hardware
docker-compose exec -T api python manage.py runscript load_nodedata
```
