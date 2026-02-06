#!/bin/bash

echo ""
echo "========================================"
echo "  STATIC FILES DIAGNOSTIC"
echo "========================================"
echo ""

PROJECT_DIR="/home/ayub/dev/deploy/laptopXplorer"
STATIC_DIR="$PROJECT_DIR/staticfiles"

echo "📂 Checking directories..."
echo ""

# Check if project directory exists
if [ -d "$PROJECT_DIR" ]; then
    echo "✅ Project directory exists: $PROJECT_DIR"
else
    echo "❌ Project directory NOT found: $PROJECT_DIR"
    exit 1
fi

# Check if staticfiles directory exists
if [ -d "$STATIC_DIR" ]; then
    echo "✅ Static files directory exists: $STATIC_DIR"
    echo ""
    echo "📊 Directory contents:"
    ls -lah "$STATIC_DIR" | head -20
else
    echo "❌ Static files directory NOT found: $STATIC_DIR"
    echo "   Creating directory..."
    mkdir -p "$STATIC_DIR"
    echo "✅ Directory created"
fi

echo ""
echo "🔍 Checking for admin static files..."

# Check if admin directory exists in staticfiles
if [ -d "$STATIC_DIR/admin" ]; then
    echo "✅ Admin static files found"
    echo ""
    echo "📁 Admin directory structure:"
    find "$STATIC_DIR/admin" -type d | head -10
    echo ""
    echo "📄 Sample admin files:"
    find "$STATIC_DIR/admin" -type f | head -10
else
    echo "❌ Admin static files NOT found in $STATIC_DIR/admin"
    echo "   This is why admin panel has no styles!"
fi

echo ""
echo "🔐 Checking permissions..."
echo ""
echo "Static directory permissions:"
ls -ld "$STATIC_DIR"
echo ""
if [ -d "$STATIC_DIR/admin" ]; then
    echo "Admin directory permissions:"
    ls -ld "$STATIC_DIR/admin"
fi

echo ""
echo "🐳 Checking Docker container..."
echo ""
docker ps --filter "name=laptopxplorer" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

echo ""
echo "📝 Checking Django settings in container..."
echo ""
docker exec laptopxplorer-web-1 python manage.py diffsettings | grep -E "STATIC_ROOT|STATIC_URL|STATICFILES_STORAGE" || echo "Container may not be running"

echo ""
echo "========================================"
echo "  RECOMMENDED FIXES"
echo "========================================"
echo ""

if [ ! -d "$STATIC_DIR/admin" ]; then
    echo "🔧 ISSUE: Admin static files are missing"
    echo ""
    echo "FIX 1: Run collectstatic inside Docker container"
    echo "   cd $PROJECT_DIR"
    echo "   docker-compose exec web python manage.py collectstatic --noinput"
    echo ""
    echo "FIX 2: Or rebuild container (which runs collectstatic)"
    echo "   cd $PROJECT_DIR"
    echo "   docker-compose down"
    echo "   docker-compose up -d --build"
    echo ""
else
    echo "✅ Admin files exist - checking nginx access..."
    echo ""
    echo "Test URL:"
    echo "   curl -I https://laptopxplorer.ayubsoft-inc.systems/static/admin/css/base.css"
fi

echo ""
echo "🧪 Testing file access from nginx perspective..."
NGINX_USER=$(ps aux | grep nginx | grep -v grep | head -1 | awk '{print $1}')
echo "Nginx running as user: $NGINX_USER"
echo ""
if [ -f "$STATIC_DIR/admin/css/base.css" ]; then
    echo "File exists: $STATIC_DIR/admin/css/base.css"
    ls -l "$STATIC_DIR/admin/css/base.css"
else
    echo "❌ File NOT found: $STATIC_DIR/admin/css/base.css"
fi

echo ""
