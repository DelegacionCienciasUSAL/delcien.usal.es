#!/bin/bash

# Start Gunicorn processes
echo "Starting Gunicorn."
cd /src/
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic --noinput
exec gunicorn delcien.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
