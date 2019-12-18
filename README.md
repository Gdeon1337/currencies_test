# currencies_test

start server:
python manage.py runserver

start celery:
celery -A jango_currencies worker --scheduler django --loglevel=info

start celery beat: celery beat -A jango_currencies --loglevel=INFO
