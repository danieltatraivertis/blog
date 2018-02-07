#!/bin/bash
# now=$(date+'%Y-%m-%d_%H:%M')
# filename="db_$(now).backup"
su postgres -c "pg_dumpall -c -f /backupdb/db_latest.backup"
su postgres -c "cp /backupdb/db_latest.backup /backupdb/db_$(date +\'%Y-%m-%d_%H:%M:%S\').backup"
