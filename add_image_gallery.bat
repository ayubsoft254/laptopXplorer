@echo off
echo ========================================
echo Adding Multi-Image Gallery Feature
echo ========================================
echo.

cd src

echo Step 1: Creating migrations...
python manage.py makemigrations laptops
echo.

echo Step 2: Running migrations...
python manage.py migrate
echo.

echo ========================================
echo Multi-Image Gallery Ready!
echo ========================================
echo.
echo ✅ LaptopImage model created
echo ✅ Admin inline gallery configured
echo ✅ Templates updated with gallery
echo.
echo Next steps:
echo  1. Start server: python manage.py runserver
echo  2. Go to admin panel: /admin/
echo  3. Edit any laptop
echo  4. Scroll down to "Laptop Images" section
echo  5. Add multiple images
echo  6. Mark one as "Primary"
echo  7. View laptop detail page to see gallery!
echo.
echo Features:
echo  - Upload multiple images per laptop
echo  - Set one as primary (main display)
echo  - Clickable thumbnails to switch view
echo  - Auto-fallback to old 'image' field
echo  - Captions for each image
echo  - Custom display order
echo.
pause
