#!/bin/bash
set -e

#cp /pg_hba.conf /var/lib/postgresql/data/
cd /db
if [[ $(ls /db) = "" ]];
then
   chown postgres:postgres /db
   su postgres -c "/usr/lib/postgresql/10/bin/initdb -D /db"
   su postgres -c "/usr/lib/postgresql/10/bin/pg_ctl -D /db start"
   su postgres -c "/usr/lib/postgresql/10/bin/createuser django"
   su postgres -c "/usr/lib/postgresql/10/bin/createdb itblog"
   su postgres -c "/usr/lib/postgresql/10/bin/psql -c \"alter user django with encrypted password '$DB_PASSWORD'\""
   su postgres -c "/usr/lib/postgresql/10/bin/psql -c \"grant all privileges on database itblog to django\""
   su postgres -c "/usr/lib/postgresql/10/bin/pg_ctl stop -D /db -m fast"
fi
exec su postgres -c "/usr/lib/postgresql/10/bin/postgres -c config_file=/postgresql.conf"
exec "$@"
