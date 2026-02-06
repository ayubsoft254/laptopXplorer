#!/bin/bash

echo ""
echo "========================================"
echo "  NGINX SETUP - Ubuntu"
echo "  laptopxplorer.ayubsoft-inc.systems"
echo "========================================"
echo ""

# Check if nginx is installed
if ! command -v nginx &> /dev/null; then
    echo "Nginx is not installed. Installing..."
    sudo apt update
    sudo apt install nginx -y
else
    echo "✅ Nginx is already installed"
fi

echo ""
echo "Step 1: Detecting paths..."
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "   Project: $SCRIPT_DIR"
echo "   Static:  $SCRIPT_DIR/staticfiles"
echo "   Media:   $SCRIPT_DIR/mediafiles"
echo ""

echo "Step 2: Creating nginx configuration..."

# Create nginx config with ACTUAL paths (not placeholders)
sudo tee /etc/nginx/sites-available/laptopxplorer > /dev/null <<EOF
server {
    listen 80;
    server_name laptopxplorer.ayubsoft-inc.systems;

    client_max_body_size 100M;

    # Proxy to Django container on port 1480
    location / {
        proxy_pass http://localhost:1480;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_redirect off;
    }

    # Static files - ACTUAL PATH (not placeholder)
    location /static/ {
        alias $SCRIPT_DIR/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Media files - ACTUAL PATH (not placeholder)
    location /media/ {
        alias $SCRIPT_DIR/mediafiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
EOF

echo "✅ Created /etc/nginx/sites-available/laptopxplorer"
echo ""
echo "Configuration uses ACTUAL paths:"
echo "   Static: $SCRIPT_DIR/staticfiles/"
echo "   Media:  $SCRIPT_DIR/mediafiles/"
echo ""

echo "Step 3: Enabling site..."
# Remove default site if exists
if [ -f /etc/nginx/sites-enabled/default ]; then
    sudo rm /etc/nginx/sites-enabled/default
    echo "   Removed default site"
fi

# Create symlink
sudo ln -sf /etc/nginx/sites-available/laptopxplorer /etc/nginx/sites-enabled/
echo "✅ Enabled laptopxplorer site"
echo ""

echo "Step 4: Testing nginx configuration..."
sudo nginx -t

if [ $? -ne 0 ]; then
    echo "❌ ERROR: Nginx configuration test failed"
    exit 1
fi

echo ""
echo "Step 5: Restarting nginx..."
sudo systemctl restart nginx

if [ $? -ne 0 ]; then
    echo "❌ ERROR: Failed to restart nginx"
    exit 1
fi

echo "✅ Nginx restarted successfully"
echo ""

echo "Step 6: Configuring firewall..."
if command -v ufw &> /dev/null; then
    sudo ufw allow 'Nginx Full'
    echo "✅ Firewall configured (UFW)"
else
    echo "⚠️  UFW not found, configure firewall manually:"
    echo "   - Allow port 80 (HTTP)"
    echo "   - Allow port 443 (HTTPS)"
fi

echo ""
echo "========================================"
echo "  NGINX SETUP COMPLETE!"
echo "========================================"
echo ""
echo "✅ Nginx is configured and running"
echo "✅ Static files path: $SCRIPT_DIR/staticfiles/"
echo "✅ Media files path:  $SCRIPT_DIR/mediafiles/"
echo ""
echo "🌐 Test Access:"
echo "   http://laptopxplorer.ayubsoft-inc.systems"
echo ""
echo "⚠️  NEXT STEPS:"
echo ""
echo "1. Verify HTTP access works"
echo ""
echo "2. Enable HTTPS with certbot:"
echo "   sudo apt install certbot python3-certbot-nginx"
echo "   sudo certbot --nginx -d laptopxplorer.ayubsoft-inc.systems"
echo ""
echo "3. Test HTTPS access:"
echo "   https://laptopxplorer.ayubsoft-inc.systems"
echo ""
echo "📚 See SSL_CERTBOT.md for detailed SSL setup"
echo ""
