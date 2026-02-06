@echo off
echo.
echo ========================================
echo   SETUP EXTERNAL NGINX FOR LAPTOPXPLORER
echo ========================================
echo.
echo This script helps you configure external nginx
echo to proxy to the Django container on port 1480.
echo.
echo Prerequisites:
echo   - Nginx installed on your system
echo   - Docker container running on port 1480
echo.
pause
echo.

REM Get the current directory
set CURRENT_DIR=%CD%

echo Step 1: Detected paths
echo   Project: %CURRENT_DIR%
echo   Static:  %CURRENT_DIR%\staticfiles
echo   Media:   %CURRENT_DIR%\mediafiles
echo.

echo Step 2: Creating nginx configuration...
echo.

REM Create a custom nginx config with correct paths
(
echo server {
echo     listen 80;
echo     server_name localhost;
echo.
echo     client_max_body_size 100M;
echo.
echo     # Proxy to Django container on port 1480
echo     location / {
echo         proxy_pass http://localhost:1480;
echo         proxy_set_header Host $host;
echo         proxy_set_header X-Real-IP $remote_addr;
echo         proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
echo         proxy_set_header X-Forwarded-Proto $scheme;
echo         proxy_redirect off;
echo     }
echo.
echo     # Static files
echo     location /static/ {
echo         alias %CURRENT_DIR%\staticfiles\;
echo         expires 30d;
echo         add_header Cache-Control "public, immutable";
echo     }
echo.
echo     # Media files
echo     location /media/ {
echo         alias %CURRENT_DIR%\mediafiles\;
echo         expires 30d;
echo         add_header Cache-Control "public, immutable";
echo     }
echo }
) > nginx-laptopxplorer.conf

echo ✅ Created nginx-laptopxplorer.conf
echo.

echo ========================================
echo   NEXT STEPS (Manual)
echo ========================================
echo.
echo 1. Copy configuration to nginx:
echo    Windows: copy nginx-laptopxplorer.conf C:\nginx\conf\
echo    Linux:   sudo cp nginx-laptopxplorer.conf /etc/nginx/sites-available/laptopxplorer
echo.
echo 2. For Linux, enable the site:
echo    sudo ln -s /etc/nginx/sites-available/laptopxplorer /etc/nginx/sites-enabled/
echo.
echo 3. Test nginx configuration:
echo    nginx -t
echo.
echo 4. Start/Reload nginx:
echo    Windows: nginx -s reload
echo    Linux:   sudo systemctl reload nginx
echo.
echo 5. Start Docker container:
echo    docker-compose up -d
echo.
echo 6. Access application:
echo    http://localhost (via nginx)
echo    http://localhost:1480 (direct)
echo.
echo For detailed instructions, see NGINX_EXTERNAL.md
echo.
pause
