import os

if os.getenv("CELERY_ENABLED", "True").lower() == "true":
    from .celery import app as celery_app