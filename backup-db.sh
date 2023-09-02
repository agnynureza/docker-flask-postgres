#!/usr/bin/env bash

docker exec -t db-container pg_dumpall -c -U myuser > dump_`date +%Y%m%d`.sql