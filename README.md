# currencies_test

start server:
python manage.py runserver

start celery :
celery -A jango_currencies worker --scheduler django --loglevel=info

celery beat -A jango_currencies --loglevel=INFO