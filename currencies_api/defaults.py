from jango_currencies import settings

CBR_URL = getattr(settings, 'CBR_URL', 'https://www.cbr-xml-daily.ru/daily_json.js')
REQUESTS_TIMEOUT = getattr(settings, 'REQUESTS_TIMEOUT', 10)

MAX_RETRY_CELERY_TASK = getattr(settings, 'MAX_RETRY_CELERY_TASK', 3)
