#!/bin/sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn wigets.wsgi:application -b 0.0.0.0:8000
