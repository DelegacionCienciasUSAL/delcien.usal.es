#!/bin/bash

# Start Gunicorn processes
echo "Starting Gunicorn."
cd /src/
rm -f db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python3 manage.py shell
python3 manage.py collectstatic --noinput
exec gunicorn delcien.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3 
