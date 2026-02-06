@echo off
echo ========================================
echo Running Django Migrations
echo ========================================
echo.

cd src

echo Step 1: Making migrations...
python manage.py makemigrations

echo.
echo Step 2: Running migrations...
python manage.py migrate

echo.
echo ========================================
echo Migrations Complete!
echo ========================================
echo.
echo Next: Create superuser with: python manage.py createsuperuser
echo Then: Run server with: python manage.py runserver
echo.
pause
