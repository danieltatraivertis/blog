#!/bin/bash
set -e

if [ $UWSGI = True ]; then
  uwsgi --ini /uwsgi.conf
else
  cd /code
  python manage.py runserver 0:8000
fi

exec "$@"
