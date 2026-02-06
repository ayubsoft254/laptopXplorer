@echo off
echo ========================================
echo Committing LaptopXplorer to GitHub
echo ========================================
echo.

cd C:\Users\henry\Desktop\laptopXplorer

echo Step 1: Checking git status...
git status

echo.
echo Step 2: Adding all changes...
git add .

echo.
echo Step 3: Committing changes...
git commit -m "Complete rebuild: Full-featured laptop comparison platform

- Implemented comprehensive database models (Brand, Category, Processor, Laptop)
- Created all views with search, filter, sort, and pagination
- Built 9 responsive templates with Tailwind CSS
- Added admin interface with customized panels
- Implemented comparison tool for side-by-side specs
- Added responsive navigation and mobile support
- Configured static and media file handling
- Created documentation (README, SETUP, PROJECT_STATUS)

Features:
* Advanced search and filtering
* Laptop comparison (up to 4 laptops)
* Brand and category browsing
* Detailed specifications display
* SEO-friendly slug URLs
* Mobile-first responsive design
* Admin dashboard for easy management

Tech Stack: Django 5.0.7, Tailwind CSS, SQLite"

echo.
echo Step 4: Pushing to GitHub...
git push origin main

echo.
echo ========================================
echo Commit Complete!
echo ========================================
echo.
echo Your changes have been pushed to GitHub
echo Visit: https://github.com/ayubsoft254/laptopXplorer
echo.
pause
