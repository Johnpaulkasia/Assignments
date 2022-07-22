#!/bin/bash
source /home/administrator/linux/config.cfg
psql "host=${host} port=${port} dbname=${dbname} user=${username} password=${pwd}" -c "\COPY (${sql_query}) TO '/${directory}/${year}.csv' (FORMAT CSV)"

sed -i "1i ${columns}" ${year}.csv

gzip -c ${year}.csv > invoices_"${year}".gz



