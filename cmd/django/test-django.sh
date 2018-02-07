#!/bin/bash
coverage run --source=/code/ /code/manage.py test -v 2
echo -n "Creating HTML... "
coverage html
echo "Done."
