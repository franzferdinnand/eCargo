from config.settings.base import *  # NOQA

DEBUG = False

SECRET_KEY = "django-insecure-!zi6yb5w0%s_hx()f^3@-%$w!p9-+5!gr03&an*i(x(niu8lwr"

ALLOWED_HOSTS = []

STATIC_URL = "static/"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
