# currencies_test
export CELERY_BROKER_URL=
export PG_HOST=
export PG_USER=
export PG_PASS=
export PG_NAME=
export PG_PORT=

start server:
python manage.py runserver

start celery:
celery -A jango_currencies worker --scheduler django --loglevel=info

start celery beat: celery beat -A jango_currencies --loglevel=INFO
