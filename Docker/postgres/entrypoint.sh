#!/bin/bash
set -e

if [[ $(ls /db) = "" ]];
then
#  echo "db folder is empty" > /db/notemptyanymore.txt
  chown postgres /db
  su postgres -c "/usr/lib/postgresql/10/bin/initdb -D /db"
fi
#su postgres -c "/usr/lib/postgresql/10/bin/pg_ctl -D /db -l /db/logfile.log start"
cp /pg_hba.conf /var/lib/postgresql/data/
#su postgres -c "/usr/lib/postgresql/10/bin/postgres -c CREATE DATABASE itblog WITH ENCODING UTF8 OWNER django"
su postgres -c "/usr/lib/postgresql/10/bin/postgres -c config_file=/postgresql.conf"

#sleep 100
exec "$@"
