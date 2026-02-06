#!/bin/bash

# Exit on error
set -e

echo "Starting LaptopXplorer..."

# Navigate to src directory where manage.py is located
cd /app/src

# Wait for database to be ready (if using PostgreSQL)
if [ "$DATABASE_URL" != "sqlite:///db.sqlite3" ]; then
    echo "Waiting for PostgreSQL..."
    while ! nc -z db 5432; do
        sleep 0.1
    done
    echo "PostgreSQL started"
fi

# For SQLite, remove corrupted database to start fresh
if [ "$DATABASE_URL" = "sqlite:///db.sqlite3" ] && [ -f "/app/src/db.sqlite3" ]; then
    echo "Removing old SQLite database to resolve migration conflicts..."
    rm -f /app/src/db.sqlite3
fi

# Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist
echo "Checking for superuser..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@laptopxplorer.com', 'admin123')
    print('Superuser created: admin / admin123')
else:
    print('Superuser already exists')
END

echo "Starting application..."

# Execute the CMD from Dockerfile
exec "$@"
