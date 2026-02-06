@echo off
echo.
echo ========================================
echo   DEPLOY TO PRODUCTION
echo   laptopxplorer.ayubsoft-inc.systems
echo ========================================
echo.

REM Check if Docker is running
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ ERROR: Docker is not installed or not running
    echo Please install Docker first
    pause
    exit /b 1
)

echo Step 1: Building Docker container...
docker-compose down
docker-compose up -d --build

if %errorlevel% neq 0 (
    echo ❌ ERROR: Docker build failed
    pause
    exit /b 1
)

echo.
echo Step 2: Collecting static files...
docker-compose exec web python src/manage.py collectstatic --noinput

echo.
echo Step 3: Running migrations...
docker-compose exec web python src/manage.py migrate --noinput

echo.
echo ========================================
echo   DEPLOYMENT COMPLETE!
echo ========================================
echo.
echo ✅ Docker container is running
echo.
echo 🌐 Access URLs:
echo    Local:      http://localhost:1480
echo    Production: http://laptopxplorer.ayubsoft-inc.systems
echo    Admin:      http://laptopxplorer.ayubsoft-inc.systems/admin
echo.
echo 👤 Default Admin:
echo    Username: admin
echo    Password: admin123
echo.
echo ⚠️  NEXT STEPS:
echo.
echo 1. Configure DNS (if not done):
echo    - Add A record: laptopxplorer → YOUR_SERVER_IP
echo    - Wait 5-10 minutes for propagation
echo.
echo 2. Configure Nginx:
echo    - Copy nginx.conf to /etc/nginx/sites-available/
echo    - Update static/media paths
echo    - Test: sudo nginx -t
echo    - Restart: sudo systemctl restart nginx
echo.
echo 3. Enable HTTPS (SSL Certificate):
echo    - Run: sudo certbot --nginx -d laptopxplorer.ayubsoft-inc.systems
echo    - Choose option 2 (Redirect HTTP to HTTPS)
echo    - See SSL_CERTBOT.md for detailed guide
echo.
echo 4. Security:
echo    - Change admin password immediately!
echo    - Update SECRET_KEY in docker-compose.yaml
echo    - Enable firewall (ports 80, 443)
echo.
echo 📚 See DOMAIN_SETUP.md for detailed instructions
echo.
pause
