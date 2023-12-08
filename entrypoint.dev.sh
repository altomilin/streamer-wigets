#!/bin/sh

python manage.py migrate --noinput

python manage.py runserver
