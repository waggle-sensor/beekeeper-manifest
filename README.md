# Beekeeper Manifest

The beekeeper manifest database is used to store the manifests of a node on the ecosystem.

* If you don't have a MySQL server on your computer yet, please follow the [official documentation](https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing) to install.

* Enter the following command at the command line terminal to login with your superuser account `root`

```
mysql -u root -p
```

* Create a database `manifest_db` on your MySQL server then switch to it.
```
CREATE DATABASE manifest_db;
USE manifest_db;
```
* To link this Django project with your MySQL server, go to `DjangoManifest/settings.py`, replace the section `DATABASES` with your database information.

```
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'manifest_db',
        'USER': 'root',
        'PASSWORD': '<your password>',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}
```

* To create the database tables that we're going to use, first create a fork then clone your repository. Enter python terminal with command

```
python3
```
then run the following to migrate data models defined in `ManifestApp/models.py` to your database.
```
python3 manage.py makemigrations
python3 manage.py migrate
```

* After migrating data tables, run the following command to start your Django server.
```
python3 manage.py runserver
```
