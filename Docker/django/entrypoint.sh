#!/bin/bash
set -e

sleep 3
exec uwsgi --ini /uwsgi.conf
exec "$@"
