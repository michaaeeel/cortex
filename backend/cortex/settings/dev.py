from .base import *  # noqa: F401,F403

import dj_database_url
from decouple import config

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "backend"]

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://cortex:cortex@db:5432/cortex"
    )
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost",
    "http://127.0.0.1",
]
