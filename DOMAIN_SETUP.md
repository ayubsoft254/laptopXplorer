# 🌐 Domain Setup Guide

## Domain Configuration

**Domain:** laptopxplorer.ayubsoft-inc.systems

---

## 📋 Prerequisites Checklist

- [ ] DNS A record points to your server IP
- [ ] Port 80 open on firewall
- [ ] Port 443 open on firewall (for HTTPS)
- [ ] Nginx installed on server
- [ ] Docker container running on port 1480

---

## 🔧 DNS Configuration

### Add A Record

Go to your DNS provider (where ayubsoft-inc.systems is managed) and add:

```
Type: A
Name: laptopxplorer
Value: YOUR_SERVER_IP
TTL: 3600 (or Auto)
```

**Result:** `laptopxplorer.ayubsoft-inc.systems` → Your Server IP

### Verify DNS Propagation

```bash
# Linux/Mac
nslookup laptopxplorer.ayubsoft-inc.systems

# Windows
nslookup laptopxplorer.ayubsoft-inc.systems

# Online tools
https://dnschecker.org
```

Wait 5-10 minutes for DNS propagation.

---

## 🚀 Deployment Steps

### 1. Update Django Settings

Already configured! ✅
- `ALLOWED_HOSTS` includes `laptopxplorer.ayubsoft-inc.systems`

### 2. Start Docker Container

```bash
cd /path/to/laptopXplorer
docker-compose up -d --build
```

Verify it's running:
```bash
curl http://localhost:1480
```

### 3. Configure Nginx

**Copy configuration:**
```bash
# Linux
sudo cp nginx.conf /etc/nginx/sites-available/laptopxplorer
sudo ln -s /etc/nginx/sites-available/laptopxplorer /etc/nginx/sites-enabled/

# Update static/media paths in the file
sudo nano /etc/nginx/sites-available/laptopxplorer
```

**Update paths in nginx.conf:**
```nginx
location /static/ {
    alias /home/user/laptopXplorer/staticfiles/;  # Change to your path
}

location /media/ {
    alias /home/user/laptopXplorer/mediafiles/;  # Change to your path
}
```

**Test configuration:**
```bash
sudo nginx -t
```

**Restart nginx:**
```bash
sudo systemctl restart nginx
```

### 4. Test HTTP Access

```bash
curl http://laptopxplorer.ayubsoft-inc.systems
```

Visit: http://laptopxplorer.ayubsoft-inc.systems

---

## 🔒 Enable HTTPS (Recommended)

### Install Certbot

```bash
# Ubuntu/Debian
sudo apt install certbot python3-certbot-nginx

# CentOS/RHEL
sudo yum install certbot python3-certbot-nginx
```

### Get SSL Certificate

```bash
sudo certbot --nginx -d laptopxplorer.ayubsoft-inc.systems
```

Follow the prompts:
1. Enter email address
2. Agree to Terms of Service
3. Choose to redirect HTTP to HTTPS (recommended)

**Certbot will:**
- Get free SSL certificate from Let's Encrypt
- Auto-configure nginx for HTTPS
- Set up auto-renewal

### Verify HTTPS

Visit: https://laptopxplorer.ayubsoft-inc.systems

### Test SSL Rating

https://www.ssllabs.com/ssltest/

---

## 🔥 Firewall Configuration

### Ubuntu/Debian (UFW)

```bash
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw reload
```

### CentOS/RHEL (firewalld)

```bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

---

## ✅ Verification Checklist

After deployment:

- [ ] DNS resolves to correct IP
- [ ] HTTP access works (http://laptopxplorer.ayubsoft-inc.systems)
- [ ] HTTPS access works (https://laptopxplorer.ayubsoft-inc.systems)
- [ ] Admin panel accessible (/admin)
- [ ] Static files loading (CSS, JS, images)
- [ ] Media files loading (user uploads)
- [ ] SSL certificate valid (A+ rating)
- [ ] Auto-renewal configured (certbot)

---

## 🔧 Troubleshooting

### DNS Not Resolving

```bash
# Check DNS
nslookup laptopxplorer.ayubsoft-inc.systems

# If not resolving:
# 1. Verify A record in DNS settings
# 2. Wait 10-15 minutes for propagation
# 3. Clear local DNS cache
```

### 502 Bad Gateway

```bash
# Check if Docker container is running
docker-compose ps

# Check container logs
docker-compose logs -f

# Verify port 1480 is accessible
curl http://localhost:1480

# Restart container
docker-compose restart
```

### Static Files Not Loading

```bash
# Collect static files
docker-compose exec web python src/manage.py collectstatic --noinput

# Verify nginx path is correct
ls /path/to/staticfiles/

# Check nginx error log
sudo tail -f /var/log/nginx/error.log

# Fix permissions
sudo chown -R www-data:www-data /path/to/staticfiles/
```

### SSL Certificate Issues

```bash
# Test renewal
sudo certbot renew --dry-run

# Force renewal
sudo certbot renew --force-renewal

# Check certificate status
sudo certbot certificates
```

---

## 📊 Monitoring

### Check Nginx Status

```bash
sudo systemctl status nginx
```

### Check Docker Container

```bash
docker-compose ps
docker-compose logs -f
```

### Monitor Access Logs

```bash
# Nginx
sudo tail -f /var/log/nginx/access.log

# Nginx errors
sudo tail -f /var/log/nginx/error.log
```

---

## 🔄 Auto-Renewal (SSL)

Certbot automatically configures auto-renewal.

**Verify:**
```bash
sudo systemctl status certbot.timer
```

**Test renewal:**
```bash
sudo certbot renew --dry-run
```

---

## 🎯 Production Optimization

### Enable Gzip Compression

Add to nginx.conf:
```nginx
gzip on;
gzip_vary on;
gzip_min_length 1024;
gzip_types text/plain text/css application/json application/javascript text/xml application/xml text/javascript;
```

### Enable Caching

Add to nginx.conf:
```nginx
# Browser caching for static files
location ~* \.(jpg|jpeg|png|gif|ico|css|js|svg|woff|woff2|ttf)$ {
    expires 1y;
    add_header Cache-Control "public, immutable";
}
```

### Rate Limiting

Add to nginx.conf:
```nginx
# Limit requests
limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s;

server {
    location / {
        limit_req zone=one burst=20;
        # ... other settings
    }
}
```

---

## 📝 Nginx Configuration Summary

```nginx
server {
    listen 80;
    server_name laptopxplorer.ayubsoft-inc.systems;
    
    # Certbot will add HTTPS redirect here
    
    location / {
        proxy_pass http://localhost:1480;
        # ... proxy headers
    }
}

server {
    listen 443 ssl http2;
    server_name laptopxplorer.ayubsoft-inc.systems;
    
    # SSL certificates (managed by Certbot)
    # ... SSL settings
    
    location / {
        proxy_pass http://localhost:1480;
        # ... proxy headers
    }
}
```

---

## 🎉 Success!

Your application should now be accessible at:

**HTTP:** http://laptopxplorer.ayubsoft-inc.systems  
**HTTPS:** https://laptopxplorer.ayubsoft-inc.systems  
**Admin:** https://laptopxplorer.ayubsoft-inc.systems/admin

---

## 📞 Quick Reference

```bash
# Start Docker
docker-compose up -d

# Restart nginx
sudo systemctl restart nginx

# View logs
docker-compose logs -f
sudo tail -f /var/log/nginx/error.log

# Renew SSL
sudo certbot renew

# Check SSL expiry
sudo certbot certificates
```

---

**Domain configured! 🌐 Your LaptopXplorer is now live!** 🚀
