#!/bin/bash
set -e
#if no db exists
cd /db
if [[ $(ls /db) = "" ]];
then
   chown postgres:postgres /db
   #init db
   su postgres -c "/usr/lib/postgresql/10/bin/initdb -D /db"
   #start db for config
   su postgres -c "/usr/lib/postgresql/10/bin/pg_ctl -D /db start"
   #create db
   su postgres -c "/usr/lib/postgresql/10/bin/createdb itblog"
   #create main user
   su postgres -c "/usr/lib/postgresql/10/bin/createuser django"
   su postgres -c "/usr/lib/postgresql/10/bin/psql -c \"alter user django with encrypted password '$DB_PASSWORD' SUPERUSER\""
   su postgres -c "/usr/lib/postgresql/10/bin/psql -c \"grant all privileges on database itblog to django\""
   #creating explorer user with read only rights
   su postgres -c "/usr/lib/postgresql/10/bin/createuser explorer"
   su postgres -c "/usr/lib/postgresql/10/bin/psql -c \"alter user django with encrypted password '$DB_PASSWORD'\""
   su postgres -c "/usr/lib/postgresql/10/bin/psql -c \"GRANT SELECT ON ALL TABLES IN SCHEMA public TO explorer\""
   su postgres -c "/usr/lib/postgresql/10/bin/psql -c \"ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO explorer\""
   #exit from config
   su postgres -c "/usr/lib/postgresql/10/bin/pg_ctl stop -D /db -m fast"
fi
#start db
exec su postgres -c "/usr/lib/postgresql/10/bin/postgres -c config_file=/postgresql.conf"
exec "$@"
