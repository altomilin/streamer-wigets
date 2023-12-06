#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn wigets.wsgi:application --reload -b 0.0.0.0:8000
