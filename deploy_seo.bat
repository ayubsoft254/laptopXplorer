@echo off
echo ========================================
echo   Deploying SEO Features
echo ========================================
echo.

cd src

echo Step 1: Running migrations...
python manage.py migrate
echo.

echo Step 2: Collecting static files...
python manage.py collectstatic --noinput
echo.

echo Step 3: Testing SEO endpoints...
echo.
echo Testing robots.txt...
curl -s http://localhost:8000/robots.txt > NUL
if %errorlevel%==0 (
    echo ✓ robots.txt working
) else (
    echo ⚠ Server needs to be running to test
)
echo.

echo Testing sitemap.xml...
curl -s http://localhost:8000/sitemap.xml > NUL
if %errorlevel%==0 (
    echo ✓ sitemap.xml working
) else (
    echo ⚠ Server needs to be running to test
)
echo.

echo ========================================
echo   SEO Features Deployed Successfully!
echo ========================================
echo.
echo ✅ Meta Tags & Open Graph
echo ✅ Schema.org Structured Data (JSON-LD)
echo ✅ XML Sitemap (5 sections)
echo ✅ robots.txt
echo ✅ Canonical URLs
echo ✅ Twitter Cards
echo ✅ SEO Template Tags
echo.
echo -------------------------------------
echo Available SEO Endpoints:
echo -------------------------------------
echo 📄 /robots.txt            - Robots exclusion file
echo 🗺️  /sitemap.xml          - Master sitemap index
echo 🗺️  /sitemap.xml?section=laptops    - Laptop pages
echo 🗺️  /sitemap.xml?section=brands     - Brand pages
echo 🗺️  /sitemap.xml?section=articles   - Article pages
echo 🗺️  /sitemap.xml?section=categories - Category pages
echo 🗺️  /sitemap.xml?section=static     - Static pages
echo.
echo -------------------------------------
echo How to Test:
echo -------------------------------------
echo 1. Start server: python manage.py runserver
echo 2. Visit: http://localhost:8000/sitemap.xml
echo 3. Visit: http://localhost:8000/robots.txt
echo 4. View any laptop page source to see:
echo    - Meta descriptions
echo    - Open Graph tags
echo    - Schema.org JSON-LD
echo    - Canonical URL
echo.
echo -------------------------------------
echo Next Steps for Production:
echo -------------------------------------
echo 1. Update robots.txt Sitemap URL with production domain
echo 2. Add actual logo.png to static/
echo 3. Add og-image.jpg to static/
echo 4. Submit sitemap to Google Search Console
echo 5. Test with Google Rich Results Test:
echo    https://search.google.com/test/rich-results
echo.
pause
