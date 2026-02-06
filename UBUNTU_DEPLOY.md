# 🐧 Ubuntu Deployment Guide

## Complete deployment guide for LaptopXplorer on Ubuntu server

---

## 📋 Prerequisites

- Ubuntu 20.04 or later
- Root or sudo access
- Domain DNS configured: `laptopxplorer.ayubsoft-inc.systems` → Server IP

---

## 🚀 Quick Deployment (5 Steps)

### 1. Install Docker & Docker Compose

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com | sh

# Add your user to docker group
sudo usermod -aG docker $USER

# Install Docker Compose
sudo apt install docker-compose -y

# Verify installation
docker --version
docker-compose --version
```

**Log out and back in** for group changes to take effect.

---

### 2. Clone/Upload Project

```bash
# If using git
git clone <your-repo-url> laptopXplorer
cd laptopXplorer

# Or upload files via SCP/SFTP
# Then:
cd laptopXplorer
```

---

### 3. Deploy Application

```bash
# Make scripts executable
chmod +x deploy-production.sh setup-nginx.sh setup-ssl.sh

# Run deployment
sudo ./deploy-production.sh
```

**What this does:**
- Builds Docker container
- Starts Django app on port 1480
- Runs migrations
- Collects static files
- Creates admin user (admin/admin123)

---

### 4. Setup Nginx

```bash
# Run nginx setup script
sudo ./setup-nginx.sh
```

**What this does:**
- Installs nginx (if needed)
- Creates nginx configuration
- Enables the site
- Configures firewall
- Restarts nginx

**Test HTTP access:**
```bash
curl http://laptopxplorer.ayubsoft-inc.systems
```

Or visit in browser: http://laptopxplorer.ayubsoft-inc.systems

---

### 5. Enable HTTPS (SSL)

```bash
# Run SSL setup script
sudo ./setup-ssl.sh
```

Or manually:
```bash
# Install certbot
sudo apt install certbot python3-certbot-nginx -y

# Get SSL certificate
sudo certbot --nginx -d laptopxplorer.ayubsoft-inc.systems
```

**Choose option 2** (Redirect HTTP to HTTPS)

**Test HTTPS access:**
Visit: https://laptopxplorer.ayubsoft-inc.systems

---

## ✅ Verification

### Check Services

```bash
# Docker container
sudo docker-compose ps

# Nginx
sudo systemctl status nginx

# SSL certificate
sudo certbot certificates
```

### Test Access

```bash
# Local (direct to Django)
curl http://localhost:1480

# Via nginx (HTTP)
curl http://laptopxplorer.ayubsoft-inc.systems

# Via nginx (HTTPS)
curl https://laptopxplorer.ayubsoft-inc.systems
```

---

## 🔧 Manual Installation Steps

If you prefer manual setup instead of scripts:

### Install Docker

```bash
# Remove old versions
sudo apt remove docker docker-engine docker.io containerd runc

# Install dependencies
sudo apt install apt-transport-https ca-certificates curl software-properties-common

# Add Docker's GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-compose

# Start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker
```

### Deploy Application

```bash
# Navigate to project
cd /path/to/laptopXplorer

# Start Docker container
sudo docker-compose up -d --build

# Run migrations
sudo docker-compose exec web python src/manage.py migrate

# Collect static files
sudo docker-compose exec web python src/manage.py collectstatic --noinput

# Create superuser (interactive)
sudo docker-compose exec web python src/manage.py createsuperuser
```

### Install and Configure Nginx

```bash
# Install nginx
sudo apt install nginx

# Copy configuration
sudo cp nginx.conf /etc/nginx/sites-available/laptopxplorer

# Edit paths
sudo nano /etc/nginx/sites-available/laptopxplorer
# Update: /path/to/laptopxplorer/staticfiles/
#     to: /home/user/laptopXplorer/staticfiles/

# Enable site
sudo ln -s /etc/nginx/sites-available/laptopxplorer /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default

# Test configuration
sudo nginx -t

# Restart nginx
sudo systemctl restart nginx
```

### Configure Firewall

```bash
# Using UFW
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable

# Check status
sudo ufw status
```

### Setup SSL

```bash
# Install certbot
sudo apt install certbot python3-certbot-nginx

# Get certificate
sudo certbot --nginx -d laptopxplorer.ayubsoft-inc.systems

# Test auto-renewal
sudo certbot renew --dry-run
```

---

## 📁 File Structure on Server

```
/home/user/laptopXplorer/
├── docker-compose.yaml
├── Dockerfile
├── docker-entrypoint.sh
├── nginx.conf
├── deploy-production.sh      ← Ubuntu deployment script
├── setup-nginx.sh             ← Nginx setup script
├── setup-ssl.sh               ← SSL setup script
├── src/
│   ├── manage.py
│   └── config/
└── staticfiles/               ← Created after collectstatic
└── mediafiles/                ← Created for uploads
```

---

## 🔄 Common Operations

### View Logs

```bash
# Docker container logs
sudo docker-compose logs -f

# Nginx access logs
sudo tail -f /var/log/nginx/access.log

# Nginx error logs
sudo tail -f /var/log/nginx/error.log

# System logs
sudo journalctl -u nginx -f
```

### Restart Services

```bash
# Restart Docker container
sudo docker-compose restart

# Rebuild and restart
sudo docker-compose up -d --build

# Restart nginx
sudo systemctl restart nginx
```

### Update Application

```bash
# Pull latest code (if using git)
git pull

# Rebuild container
sudo docker-compose up -d --build

# Run migrations
sudo docker-compose exec web python src/manage.py migrate

# Collect static files
sudo docker-compose exec web python src/manage.py collectstatic --noinput

# Restart
sudo docker-compose restart
```

### Database Backup

```bash
# Backup SQLite database
sudo docker-compose exec web python src/manage.py dumpdata > backup.json

# Or copy database file
sudo docker cp $(sudo docker-compose ps -q web):/app/src/db.sqlite3 backup_$(date +%Y%m%d).sqlite3
```

---

## 🔒 Security Checklist

After deployment:

- [ ] Change admin password
  ```bash
  sudo docker-compose exec web python src/manage.py changepassword admin
  ```

- [ ] Update SECRET_KEY in `docker-compose.yaml`
  ```bash
  sudo nano docker-compose.yaml
  # Change SECRET_KEY value
  sudo docker-compose restart
  ```

- [ ] Configure firewall
  ```bash
  sudo ufw enable
  sudo ufw status
  ```

- [ ] Verify HTTPS works
  - Visit: https://laptopxplorer.ayubsoft-inc.systems
  - Check SSL rating: https://www.ssllabs.com/ssltest/

- [ ] Set up automatic backups
  ```bash
  # Create backup script
  sudo nano /usr/local/bin/backup-laptopxplorer.sh
  # Add to crontab
  sudo crontab -e
  ```

- [ ] Enable fail2ban (optional)
  ```bash
  sudo apt install fail2ban
  sudo systemctl enable fail2ban
  ```

---

## 🐛 Troubleshooting

### Container won't start

```bash
# Check logs
sudo docker-compose logs

# Check if port 1480 is in use
sudo netstat -tlnp | grep 1480

# Rebuild from scratch
sudo docker-compose down -v
sudo docker-compose up -d --build
```

### Nginx 502 Bad Gateway

```bash
# Check if Docker container is running
sudo docker-compose ps

# Check if port 1480 is accessible
curl http://localhost:1480

# Check nginx error log
sudo tail -f /var/log/nginx/error.log

# Restart both
sudo docker-compose restart
sudo systemctl restart nginx
```

### Static files not loading

```bash
# Verify path in nginx config
sudo nano /etc/nginx/sites-available/laptopxplorer

# Collect static files
sudo docker-compose exec web python src/manage.py collectstatic --noinput

# Fix permissions
sudo chown -R www-data:www-data staticfiles/ mediafiles/

# Test nginx config
sudo nginx -t
sudo systemctl restart nginx
```

### SSL certificate issues

```bash
# Check certificate status
sudo certbot certificates

# Renew certificate
sudo certbot renew

# Force renewal
sudo certbot renew --force-renewal

# Check auto-renewal
sudo systemctl status certbot.timer
```

---

## 📊 Monitoring

### System Resources

```bash
# Check CPU and memory
htop

# Or
top

# Docker stats
sudo docker stats
```

### Disk Usage

```bash
# Check disk space
df -h

# Check Docker disk usage
sudo docker system df

# Clean up unused Docker resources
sudo docker system prune -a
```

---

## 🔄 Maintenance

### Update System

```bash
# Update packages
sudo apt update && sudo apt upgrade -y

# Update Docker images
sudo docker-compose pull
sudo docker-compose up -d
```

### SSL Certificate Renewal

Automatic renewal is configured, but you can test:

```bash
# Test renewal
sudo certbot renew --dry-run

# Force renewal (if needed)
sudo certbot renew --force-renewal
```

### Cleanup

```bash
# Remove old Docker images
sudo docker image prune -a

# Remove unused volumes
sudo docker volume prune

# Clean package cache
sudo apt clean
sudo apt autoremove
```

---

## 📞 Quick Reference

```bash
# Deploy/Update
sudo ./deploy-production.sh

# Setup Nginx
sudo ./setup-nginx.sh

# Setup SSL
sudo ./setup-ssl.sh

# View logs
sudo docker-compose logs -f

# Restart
sudo docker-compose restart
sudo systemctl restart nginx

# Status
sudo docker-compose ps
sudo systemctl status nginx
```

---

## 🎯 Post-Deployment

After successful deployment:

1. **Test Everything:**
   - Visit https://laptopxplorer.ayubsoft-inc.systems
   - Login to admin panel
   - Upload test images
   - Test all features

2. **Monitor:**
   - Check logs regularly
   - Monitor disk space
   - Watch for SSL expiry (auto-renewed)

3. **Backup:**
   - Set up automated backups
   - Test restore procedure

4. **Documentation:**
   - Document any custom configurations
   - Keep credentials secure

---

**🐧 Ubuntu deployment complete!** 🚀

Your LaptopXplorer is now live at:
**https://laptopxplorer.ayubsoft-inc.systems**
