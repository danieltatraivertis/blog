#!/bin/bash
if [[ $1 == "" ]]
then
	#su postgres -c "psql -f /backupdb/db_latest.backup"
	ls -l /backupdb/
else
	su postgres -c "psql -f /backupdb/$1"
fi
