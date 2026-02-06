@echo off
echo ========================================
echo Populating LaptopXplorer Database
echo ========================================
echo.

cd src
python manage.py populate_db

echo.
echo ========================================
echo Done!
echo ========================================
echo.
pause
