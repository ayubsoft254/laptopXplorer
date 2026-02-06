#!/bin/bash

echo ""
echo "========================================"
echo "  FIX ADMIN PANEL STYLES"
echo "========================================"
echo ""

echo "This script will fix missing admin panel styles in production"
echo ""

echo "Step 1: Collecting static files (including admin CSS)..."
sudo docker-compose exec -T web python src/manage.py collectstatic --noinput --clear

if [ $? -ne 0 ]; then
    echo "❌ ERROR: Failed to collect static files"
    exit 1
fi

echo ""
echo "Step 2: Verifying static files location..."
sudo docker-compose exec -T web ls -la /app/staticfiles/admin/css/ | head -5

echo ""
echo "Step 3: Checking permissions..."
sudo ls -la staticfiles/admin/css/ | head -5

echo ""
echo "Step 4: Restarting Django container..."
sudo docker-compose restart

echo ""
echo "========================================"
echo "  FIX COMPLETE!"
echo "========================================"
echo ""
echo "✅ Admin static files collected"
echo "✅ Django container restarted"
echo ""
echo "🌐 Test admin panel:"
echo "   https://laptopxplorer.ayubsoft-inc.systems/admin"
echo ""
echo "If styles still don't load:"
echo "  1. Check nginx logs: sudo tail -f /var/log/nginx/error.log"
echo "  2. Check nginx config has correct static path"
echo "  3. Restart nginx: sudo systemctl restart nginx"
echo ""
echo "Admin static files should be at:"
echo "  /path/to/laptopXplorer/staticfiles/admin/"
echo ""
