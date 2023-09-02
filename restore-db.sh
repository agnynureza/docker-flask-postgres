#!/usr/bin/env bash

cat dump_20230903.sql | docker exec -i db-container psql -U myuser -d postgres