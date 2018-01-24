#!/bin/bash
cd /code
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
