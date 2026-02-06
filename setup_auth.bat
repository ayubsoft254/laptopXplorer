@echo off
echo ========================================
echo Setting Up Authentication System
echo ========================================
echo.

cd src

echo Step 1: Creating template directories...
mkdir templates\account 2>nul
mkdir templates\accounts 2>nul
echo ✅ Directories created
echo.

echo Step 2: Installing dependencies...
pip install django-allauth crispy-tailwind --quiet
echo ✅ Dependencies installed
echo.

echo Step 3: Running migrations...
python manage.py makemigrations accounts
python manage.py migrate
echo ✅ Migrations complete
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo  1. Run: python manage.py runserver
echo  2. Visit: http://localhost:8000/accounts/login/
echo  3. Create account: http://localhost:8000/accounts/signup/
echo.
pause
