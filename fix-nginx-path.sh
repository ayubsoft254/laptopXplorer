#!/bin/bash

echo ""
echo "========================================"
echo "  FIX NGINX STATIC PATH"
echo "========================================"
echo ""

# Get the actual project directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "🔍 Detected project directory:"
echo "   $SCRIPT_DIR"
echo ""

# Check if nginx config exists
if [ ! -f /etc/nginx/sites-available/laptopxplorer ]; then
    echo "❌ ERROR: /etc/nginx/sites-available/laptopxplorer not found"
    echo "Run setup-nginx.sh first!"
    exit 1
fi

echo "📝 Current nginx configuration:"
grep -n "alias" /etc/nginx/sites-available/laptopxplorer
echo ""

echo "🔧 Updating nginx configuration with correct paths..."

# Update the nginx config with correct paths
sudo sed -i "s|alias /path/to/laptopxplorer/staticfiles/|alias $SCRIPT_DIR/staticfiles/|g" /etc/nginx/sites-available/laptopxplorer
sudo sed -i "s|alias /path/to/laptopxplorer/mediafiles/|alias $SCRIPT_DIR/mediafiles/|g" /etc/nginx/sites-available/laptopxplorer

echo ""
echo "✅ Updated nginx configuration:"
grep -n "alias" /etc/nginx/sites-available/laptopxplorer
echo ""

echo "🧪 Testing nginx configuration..."
sudo nginx -t

if [ $? -ne 0 ]; then
    echo "❌ ERROR: Nginx configuration test failed"
    exit 1
fi

echo ""
echo "🔄 Reloading nginx..."
sudo systemctl reload nginx

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "  NGINX PATHS FIXED!"
    echo "========================================"
    echo ""
    echo "✅ Static files path: $SCRIPT_DIR/staticfiles/"
    echo "✅ Media files path:  $SCRIPT_DIR/mediafiles/"
    echo "✅ Nginx reloaded successfully"
    echo ""
    echo "🌐 Test admin panel now:"
    echo "   https://laptopxplorer.ayubsoft-inc.systems/admin"
    echo ""
    echo "🔍 Verify static file is accessible:"
    echo "   curl -I https://laptopxplorer.ayubsoft-inc.systems/static/admin/css/base.css"
    echo ""
else
    echo "❌ ERROR: Failed to reload nginx"
    exit 1
fi
