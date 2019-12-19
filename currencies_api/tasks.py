import logging

from jango_currencies import celery_app

from .cbr_requests import parse_cbr_currencies
from .defaults import MAX_RETRY_CELERY_TASK
from .models import Currencies


@celery_app.task(autoretry_for=(Exception,), retry_kwargs={'max_retries': MAX_RETRY_CELERY_TASK})
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
