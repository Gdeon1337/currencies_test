import logging

from celery.schedules import crontab

from jango_currencies import celery_app, defaults

from .cbr_requests import parse_cbr_currencies
from .models import Currencies


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=defaults.PERIOD_TASK_CELERY_MINUTE, hour=defaults.PERIOD_TASK_CELERY_HOUR),
        load_currencies.s()
    )


@celery_app.task(autoretry_for=(Exception,), retry_kwargs={'max_retries': defaults.CELERY_MAX_RETRY})
def load_currencies():
    logging.info('Celery Task %s started', 'load_currencies')

    currencies = Currencies.objects.all()
    cbr_currencies = parse_cbr_currencies()

    for currency in currencies:
        ruble_rate = cbr_currencies.get(currency.title, {}).get('Value')
        if ruble_rate:
            logging.info('Currencies %s update', currency.title)
            currency.ruble_rate = ruble_rate
            currency.save()
