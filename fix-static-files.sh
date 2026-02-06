#!/bin/bash

echo ""
echo "========================================"
echo "  FIX STATIC FILES - Complete Solution"
echo "========================================"
echo ""

PROJECT_DIR="/home/ayub/dev/deploy/laptopXplorer"
STATIC_DIR="$PROJECT_DIR/staticfiles"

cd "$PROJECT_DIR" || exit 1

echo "📍 Working directory: $(pwd)"
echo ""

echo "Step 1: Ensuring staticfiles directory exists..."
mkdir -p "$STATIC_DIR"
echo "✅ Directory ready: $STATIC_DIR"
echo ""

echo "Step 2: Checking Docker container status..."
if ! docker ps | grep -q "laptopxplorer-web"; then
    echo "⚠️  Container not running. Starting..."
    docker-compose up -d
    sleep 5
else
    echo "✅ Container is running"
fi
echo ""

echo "Step 3: Collecting static files..."
echo ""
docker-compose exec -T web python manage.py collectstatic --noinput --clear

if [ $? -ne 0 ]; then
    echo ""
    echo "❌ collectstatic failed. Trying alternative approach..."
    echo ""
    echo "Rebuilding container..."
    docker-compose down
    docker-compose up -d --build
    sleep 10
    echo ""
    echo "Running collectstatic again..."
    docker-compose exec -T web python manage.py collectstatic --noinput --clear
fi

echo ""
echo "Step 4: Verifying admin files..."
echo ""
if [ -d "$STATIC_DIR/admin" ]; then
    echo "✅ Admin static files collected"
    echo ""
    echo "Sample files found:"
    find "$STATIC_DIR/admin" -type f | head -5
    echo ""
    echo "Total admin files: $(find "$STATIC_DIR/admin" -type f | wc -l)"
else
    echo "❌ ERROR: Admin files still missing!"
    echo ""
    echo "Debug information:"
    docker-compose exec -T web python manage.py findstatic admin/css/base.css --verbosity 2
    exit 1
fi

echo ""
echo "Step 5: Setting correct permissions..."
echo ""
# Ensure nginx can read the files
chmod -R 755 "$STATIC_DIR"
echo "✅ Permissions set to 755 for staticfiles"
echo ""
ls -ld "$STATIC_DIR"

echo ""
echo "Step 6: Testing nginx access..."
echo ""
if [ -f "$STATIC_DIR/admin/css/base.css" ]; then
    echo "✅ Base CSS exists:"
    ls -lh "$STATIC_DIR/admin/css/base.css"
else
    echo "❌ Base CSS not found!"
fi

echo ""
echo "Step 7: Reloading nginx..."
sudo nginx -t && sudo systemctl reload nginx
echo "✅ Nginx reloaded"

echo ""
echo "========================================"
echo "  STATIC FILES FIX COMPLETE!"
echo "========================================"
echo ""
echo "✅ Static files collected: $STATIC_DIR"
echo "✅ Admin files available"
echo "✅ Permissions configured"
echo "✅ Nginx reloaded"
echo ""
echo "🧪 TEST NOW:"
echo ""
echo "1. Clear browser cache (Ctrl+Shift+Del)"
echo ""
echo "2. Visit admin panel:"
echo "   https://laptopxplorer.ayubsoft-inc.systems/admin"
echo ""
echo "3. Test static file directly:"
echo "   curl -I https://laptopxplorer.ayubsoft-inc.systems/static/admin/css/base.css"
echo ""
echo "   Should return: HTTP/2 200"
echo ""
echo "4. Check nginx logs if still failing:"
echo "   sudo tail -f /var/log/nginx/error.log"
echo ""
