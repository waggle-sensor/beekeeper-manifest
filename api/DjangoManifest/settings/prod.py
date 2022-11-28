from .base import *
import os

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split()
CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS", "").split()
SESSION_COOKIE_SECURE = bool(int(os.environ.get("SESSION_COOKIE_SECURE", "1")))

DATABASES = {
    "default": {
        "ENGINE": os.environ["DATABASE_BACKEND"],
        "HOST": os.environ["DATABASE_HOST"],
        "USER": os.environ["DATABASE_USER"],
        "PASSWORD": os.environ["DATABASE_PASSWORD"],
        "NAME": os.environ["DATABASE_NAME"],
    }
}

STATIC_ROOT = "/var/www/static"
