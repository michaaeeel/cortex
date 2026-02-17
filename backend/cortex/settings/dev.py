from .base import *  # noqa: F401,F403

import dj_database_url
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://cortex:cortex@db:5432/cortex"
    )
}

CORS_ALLOW_ALL_ORIGINS = True
