import logging.config
import os

from celery import Celery

from .settings import LOGGING

logging.config.dictConfig(LOGGING)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jango_currencies.settings')

app = Celery('django_currencies')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
