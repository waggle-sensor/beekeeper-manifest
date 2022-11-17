from .base import *

DEBUG = True

SECRET_KEY = "django-insecure-4DQhs101FK4NgF_PHyEDFyDTze4REhtcHmKiksqO_ztM7vV3Vw"
ALLOWED_HOSTS = ["*"]
SESSION_COOKIE_SECURE = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
