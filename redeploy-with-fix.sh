#!/bin/bash

echo ""
echo "========================================"
echo "  DEPLOY UPDATED DOCKER CONFIGURATION"
echo "========================================"
echo ""

PROJECT_DIR="/home/ayub/dev/deploy/laptopXplorer"
cd "$PROJECT_DIR" || exit 1

echo "📍 Working directory: $(pwd)"
echo ""

echo "Step 1: Stopping current container..."
docker-compose down
echo "✅ Container stopped"
echo ""

echo "Step 2: Removing old named volumes..."
docker volume rm laptopxplorer_static_volume 2>/dev/null || echo "   (No old static volume to remove)"
docker volume rm laptopxplorer_media_volume 2>/dev/null || echo "   (No old media volume to remove)"
echo "✅ Old volumes removed"
echo ""

echo "Step 3: Creating host directories..."
mkdir -p ./staticfiles
mkdir -p ./mediafiles
echo "✅ Directories created:"
echo "   $(pwd)/staticfiles"
echo "   $(pwd)/mediafiles"
echo ""

echo "Step 4: Starting container with new configuration..."
docker-compose up -d --build
echo "✅ Container started"
echo ""

echo "Step 5: Waiting for container to be ready..."
sleep 5
echo ""

echo "Step 6: Collecting static files..."
docker-compose exec -T web python manage.py collectstatic --noinput --clear
echo ""

echo "Step 7: Verifying static files on host..."
if [ -d "./staticfiles/admin" ]; then
    echo "✅ Admin static files found on host!"
    echo ""
    echo "📊 Files collected:"
    find ./staticfiles/admin -type f | wc -l
    echo ""
    echo "Sample files:"
    ls -lh ./staticfiles/admin/css/ | head -5
else
    echo "❌ ERROR: Admin files not found!"
    exit 1
fi

echo ""
echo "Step 8: Setting permissions..."
chmod -R 755 ./staticfiles
chmod -R 755 ./mediafiles
echo "✅ Permissions set"
echo ""

echo "Step 9: Verifying full path..."
FULL_PATH="$(pwd)/staticfiles"
echo "Static files location: $FULL_PATH"
ls -ld "$FULL_PATH"
echo ""

echo "Step 10: Testing nginx can read files..."
NGINX_USER=$(ps aux | grep nginx | grep -v grep | head -1 | awk '{print $1}')
echo "Nginx runs as: $NGINX_USER"
echo ""

if [ -f "$FULL_PATH/admin/css/base.css" ]; then
    echo "✅ Base CSS file accessible:"
    ls -lh "$FULL_PATH/admin/css/base.css"
else
    echo "❌ Base CSS not found!"
fi

echo ""
echo "Step 11: Reloading nginx..."
sudo nginx -t && sudo systemctl reload nginx
echo "✅ Nginx reloaded"
echo ""

echo "========================================"
echo "  DEPLOYMENT COMPLETE!"
echo "========================================"
echo ""
echo "✅ Docker container running with host volumes"
echo "✅ Static files accessible to nginx"
echo "✅ Path: $FULL_PATH"
echo ""
echo "🧪 TEST NOW:"
echo ""
echo "1. Clear browser cache (Ctrl+Shift+R)"
echo ""
echo "2. Visit admin panel:"
echo "   https://laptopxplorer.ayubsoft-inc.systems/admin"
echo ""
echo "3. Test static file:"
echo "   curl -I https://laptopxplorer.ayubsoft-inc.systems/static/admin/css/base.css"
echo ""
echo "   Expected: HTTP/2 200 OK"
echo ""
echo "📊 Container status:"
docker-compose ps
echo ""
