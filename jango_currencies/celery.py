import logging.config
import os

from celery import Celery

from .settings import LOGGING, CELERY_BEAT_SCHEDULE

logging.config.dictConfig(LOGGING)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jango_currencies.settings')

app = Celery('django_currencies')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = CELERY_BEAT_SCHEDULE
app.autodiscover_tasks()
