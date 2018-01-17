#!/bin/bash
set -e

if [ $UWSGI = False ]; then
  cp /tmp/nginx.conf /nginx.conf
else
  cp /tmp/nginx_uwsgi.conf /nginx.conf
fi

if [ "$1" = 'nginx' ]; then
  exec nginx -c /nginx.conf
fi

exec "$@"
