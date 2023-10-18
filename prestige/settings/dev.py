from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-9$@jx%_^tfp*3rnoc4$k(9*#g%)o-=dc7#-zt^#!fwwctbslwr"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "prestige",  # Имя вашей базы данных
        "USER": "postgres",  # Имя пользователя PostgreSQL
        "PASSWORD": "kallemort1",  # Пароль пользователя (если установлен)
        "HOST": "localhost",  # Хост PostgreSQL
        "PORT": "",  # Порт PostgreSQL (по умолчанию 5432)
    }
}
try:
    from .local import *
except ImportError:
    pass
