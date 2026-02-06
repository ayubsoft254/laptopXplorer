@echo off
echo ========================================
echo Creating Database Migrations
echo ========================================
echo.

cd src
python manage.py makemigrations
python manage.py migrate

echo.
echo ========================================
echo Migrations Complete!
echo ========================================
pause
