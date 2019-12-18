import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jango_currencies.settings')

app = Celery('django_currencies')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
