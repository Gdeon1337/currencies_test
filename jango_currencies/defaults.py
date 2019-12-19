from jango_currencies import settings

PERIOD_TASK_CELERY_MINUTE = getattr(settings, 'PERIOD_TASK_CELERY_MINUTE', 0)
PERIOD_TASK_CELERY_HOUR = getattr(settings, 'PERIOD_TASK_CELERY_HOUR', 0)

CBR_URL = getattr(settings, 'CBR_URL', 'https://www.cbr-xml-daily.ru/daily_json.js')
REQUESTS_TIMEOUT = getattr(settings, 'REQUESTS_TIMEOUT', 10)

CELERY_MAX_RETRY = getattr(settings, 'CELERY_MAX_RETRY', 3)
