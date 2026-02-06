@echo off
echo.
echo ========================================
echo   DOCKER DEPLOYMENT - LAPTOPXPLORER
echo ========================================
echo.
echo Building and starting containers...
echo.

docker-compose up -d --build

echo.
echo ========================================
echo   DEPLOYMENT COMPLETE!
echo ========================================
echo.
echo ✅ Application is running on port 1480
echo.
echo 🌐 Access URLs:
echo    Main App:    http://localhost:1480
echo    Admin Panel: http://localhost:1480/admin
echo.
echo 👤 Default Admin Credentials:
echo    Username: admin
echo    Password: admin123
echo.
echo 📋 Useful Commands:
echo    View logs:     docker-compose logs -f
echo    Stop:          docker-compose down
echo    Restart:       docker-compose restart
echo    Shell access:  docker-compose exec web bash
echo.
echo ⚠️  SECURITY: Change admin password after first login!
echo.
pause
