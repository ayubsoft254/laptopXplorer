#!/bin/bash

echo ""
echo "========================================"
echo "  DEPLOY TO PRODUCTION - Ubuntu"
echo "  laptopxplorer.ayubsoft-inc.systems"
echo "========================================"
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ ERROR: Docker is not installed"
    echo "Install with: curl -fsSL https://get.docker.com | sh"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ ERROR: Docker Compose is not installed"
    echo "Install with: sudo apt install docker-compose"
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"
echo ""

echo "Step 1: Stopping existing containers..."
sudo docker-compose down

echo ""
echo "Step 2: Building and starting Docker container..."
sudo docker-compose up -d --build

if [ $? -ne 0 ]; then
    echo "❌ ERROR: Docker build failed"
    exit 1
fi

echo ""
echo "Step 3: Waiting for container to be ready..."
sleep 5

echo ""
echo "Step 4: Collecting static files..."
sudo docker-compose exec -T web python src/manage.py collectstatic --noinput

echo ""
echo "Step 5: Running migrations..."
sudo docker-compose exec -T web python src/manage.py migrate --noinput

echo ""
echo "========================================"
echo "  DEPLOYMENT COMPLETE!"
echo "========================================"
echo ""
echo "✅ Docker container is running"
echo ""
echo "🌐 Access URLs:"
echo "   Local:      http://localhost:1480"
echo "   Production: http://laptopxplorer.ayubsoft-inc.systems"
echo "   Admin:      http://laptopxplorer.ayubsoft-inc.systems/admin"
echo ""
echo "👤 Default Admin:"
echo "   Username: admin"
echo "   Password: admin123"
echo ""
echo "⚠️  NEXT STEPS:"
echo ""
echo "1. Configure Nginx:"
echo "   Run: sudo ./setup-nginx.sh"
echo ""
echo "2. Enable HTTPS:"
echo "   Run: sudo certbot --nginx -d laptopxplorer.ayubsoft-inc.systems"
echo ""
echo "3. Security:"
echo "   - Change admin password immediately!"
echo "   - Update SECRET_KEY in docker-compose.yaml"
echo "   - Enable firewall (ports 80, 443)"
echo ""
echo "📚 See UBUNTU_DEPLOY.md for detailed instructions"
echo ""
