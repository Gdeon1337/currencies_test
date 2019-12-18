import requests
from celery.schedules import crontab

from jango_currencies import celery_app

from .models import Currencies


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        load_currencies.s()
    )


@celery_app.task(autoretry_for=(Exception,), retry_kwargs={'max_retries': 3})
def load_currencies():
    currencies = Currencies.objects.all()
    cbr_currencies = parse_cbr_currencies()
    for currency in currencies:
        ruble_rate = cbr_currencies.get(currency.title, {}).get('Value', 0)
        currency.ruble_rate = ruble_rate
        currency.save()


def parse_cbr_currencies():
    cbr_currencies = requests.get('https://www.cbr-xml-daily.ru/daily_json.js', timeout=(5, 30)).json()
    return cbr_currencies.get('Valute', {})
