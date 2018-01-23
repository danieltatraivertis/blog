#!/bin/bash
set -e

# exec su-exec django uwsgi --ini /uwsgi.conf
uwsgi --ini /uwsgi.conf
exec "$@"
