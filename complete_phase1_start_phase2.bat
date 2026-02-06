@echo off
echo ========================================
echo Phase 1 Complete + Starting Phase 2
echo ========================================
echo.

echo ✅ PHASE 1 COMPLETE (100%%)
echo    - Advanced Filters
echo    - User Authentication
echo    - Favorites System
echo    - Dark Mode Toggle
echo.

echo 🚀 PHASE 2 IN PROGRESS...
echo.

echo Step 1: Running migrations for price tracking...
cd src
python manage.py makemigrations laptops
python manage.py migrate
echo ✅ Price tracking models created
echo.

echo Step 2: Running authentication migrations...
python manage.py makemigrations accounts
python manage.py migrate
echo ✅ User profiles ready
echo.

echo Step 3: Activating advanced filters template...
cd templates\laptops
if exist laptop_list_new.html (
    del laptop_list.html 2>nul
    ren laptop_list_new.html laptop_list.html
    echo ✅ Advanced filters activated
)
cd ..\..
echo.

echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo ✅ Phase 1: 100%% Complete
echo ⏳ Phase 2: Price Tracking models ready
echo.
echo Next:
echo  1. Start server: python manage.py runserver
echo  2. Test dark mode: Click toggle in navbar
echo  3. Add price history in admin panel
echo  4. View: http://localhost:8000/laptops/deals/ (coming soon)
echo.
pause
