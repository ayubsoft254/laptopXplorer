@echo off
echo ========================================
echo Testing Advanced Filters Feature
echo ========================================
echo.
echo Running template replacement...
cd src\templates\laptops
if exist laptop_list_new.html (
    del laptop_list.html 2>nul
    ren laptop_list_new.html laptop_list.html
    echo ✅ Template replaced successfully!
) else (
    echo ⚠️  laptop_list_new.html not found
)
echo.
cd ..\..
echo Starting development server...
python manage.py runserver
