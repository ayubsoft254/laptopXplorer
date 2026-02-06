#!/bin/bash

echo ""
echo "========================================"
echo "  SSL SETUP WITH CERTBOT - Ubuntu"
echo "  laptopxplorer.ayubsoft-inc.systems"
echo "========================================"
echo ""

# Check if certbot is installed
if ! command -v certbot &> /dev/null; then
    echo "Certbot is not installed. Installing..."
    sudo apt update
    sudo apt install certbot python3-certbot-nginx -y
else
    echo "✅ Certbot is already installed"
fi

echo ""
echo "Step 1: Verifying nginx is running..."
if ! systemctl is-active --quiet nginx; then
    echo "❌ ERROR: Nginx is not running"
    echo "Run: sudo systemctl start nginx"
    exit 1
fi
echo "✅ Nginx is running"

echo ""
echo "Step 2: Verifying Docker container is running..."
if ! docker-compose ps | grep -q "Up"; then
    echo "❌ ERROR: Docker container is not running"
    echo "Run: sudo docker-compose up -d"
    exit 1
fi
echo "✅ Docker container is running"

echo ""
echo "Step 3: Testing port 1480 connectivity..."
if ! curl -s http://localhost:1480 > /dev/null; then
    echo "⚠️  WARNING: Could not connect to port 1480"
    echo "The Django app might not be responding"
fi

echo ""
echo "========================================"
echo "  Ready to obtain SSL certificate!"
echo "========================================"
echo ""
echo "Run the following command:"
echo ""
echo "  sudo certbot --nginx -d laptopxplorer.ayubsoft-inc.systems"
echo ""
echo "During setup:"
echo "  1. Enter your email address"
echo "  2. Agree to Terms of Service (Y)"
echo "  3. Choose option 2 (Redirect HTTP to HTTPS)"
echo ""
echo "After certbot completes:"
echo "  - Your site will have HTTPS enabled"
echo "  - HTTP will redirect to HTTPS"
echo "  - Auto-renewal will be configured"
echo ""
echo "To run certbot now, press Enter (or Ctrl+C to cancel)..."
read -r

echo ""
echo "Running certbot..."
sudo certbot --nginx -d laptopxplorer.ayubsoft-inc.systems

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "  SSL SETUP COMPLETE!"
    echo "========================================"
    echo ""
    echo "✅ HTTPS is now enabled"
    echo ""
    echo "🌐 Access your site:"
    echo "   https://laptopxplorer.ayubsoft-inc.systems"
    echo ""
    echo "🔒 Verify SSL:"
    echo "   https://www.ssllabs.com/ssltest/"
    echo ""
    echo "🔄 Auto-renewal is configured"
    echo "   Test with: sudo certbot renew --dry-run"
    echo ""
else
    echo ""
    echo "❌ SSL setup failed"
    echo "Check the error messages above"
    echo ""
    echo "Common issues:"
    echo "  - DNS not propagated (wait 10-30 minutes)"
    echo "  - Port 80 not accessible from internet"
    echo "  - Firewall blocking connections"
    echo ""
fi
