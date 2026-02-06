@echo off
echo ========================================
echo Setting Up Authentication System
echo ========================================
echo.

echo Step 1: Installing dependencies...
pip install django-allauth==0.57.0 crispy-tailwind==1.0.3 --quiet
echo ✅ Dependencies installed
echo.

echo Step 2: Creating authentication templates...
python create_auth_templates.py
echo.

echo Step 3: Running migrations...
cd src
python manage.py makemigrations accounts
python manage.py migrate
echo ✅ Migrations complete
echo.

echo Step 4: Replacing laptop list template...
cd templates\laptops
if exist laptop_list_new.html (
    del laptop_list.html 2>nul
    ren laptop_list_new.html laptop_list.html
    echo ✅ Advanced filters template activated
)
cd ..\..
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo ✅ Authentication system is ready!
echo ✅ Advanced filters are active!
echo.
echo Next steps:
echo  1. Start server: python manage.py runserver
echo  2. Create account: http://localhost:8000/accounts/signup/
echo  3. Sign in: http://localhost:8000/accounts/login/
echo  4. Browse with filters: http://localhost:8000/laptops/
echo.
pause
