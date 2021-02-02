#!/bin/bash
psql -h localhost -U postgres -f scriptSql.sql
python manage.py makemigrations
python manage.py migrate
