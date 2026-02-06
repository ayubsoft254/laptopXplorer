# External Nginx Configuration for LaptopXplorer

This configuration is for running nginx OUTSIDE of Docker, proxying to the Django container on port 1480.

## Installation

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install nginx
```

### Windows
Download from: https://nginx.org/en/download.html

### macOS
```bash
brew install nginx
```

---

## Setup

### 1. Copy Configuration File

**Linux/macOS:**
```bash
sudo cp nginx.conf /etc/nginx/sites-available/laptopxplorer
sudo ln -s /etc/nginx/sites-available/laptopxplorer /etc/nginx/sites-enabled/
```

**Windows:**
```bash
copy nginx.conf C:\nginx\conf\laptopxplorer.conf
# Then include it in nginx.conf:
# include laptopxplorer.conf;
```

### 2. Update Paths in nginx.conf

Edit the static/media file paths:
```nginx
location /static/ {
    alias C:/Users/henry/Desktop/laptopXplorer/staticfiles/;  # Windows
    # alias /home/user/laptopXplorer/staticfiles/;           # Linux
}

location /media/ {
    alias C:/Users/henry/Desktop/laptopXplorer/mediafiles/;  # Windows
    # alias /home/user/laptopXplorer/mediafiles/;           # Linux
}
```

### 3. Test Configuration

```bash
# Linux/macOS
sudo nginx -t

# Windows
nginx -t
```

### 4. Restart Nginx

```bash
# Linux/macOS
sudo systemctl restart nginx

# Windows
nginx -s reload
```

---

## Configuration Explained

### Basic HTTP (Port 80)
```nginx
server {
    listen 80;
    server_name localhost;
    
    # Proxy all requests to Django container on port 1480
    location / {
        proxy_pass http://localhost:1480;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### With Static/Media Files
```nginx
# Serve static files directly (faster)
location /static/ {
    alias /path/to/staticfiles/;
    expires 30d;
}

# Serve media files directly
location /media/ {
    alias /path/to/mediafiles/;
    expires 30d;
}
```

---

## Production Setup (HTTPS)

### 1. Get SSL Certificate

**Using Let's Encrypt (Free):**
```bash
# Linux
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### 2. Update nginx.conf

Uncomment the HTTPS section and update:
```nginx
server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;
    
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    location / {
        proxy_pass http://localhost:1480;
        # ... other proxy settings
    }
}
```

### 3. Test and Reload
```bash
sudo nginx -t
sudo systemctl reload nginx
```

---

## Testing

### 1. Start Docker Container
```bash
cd C:\Users\henry\Desktop\laptopXplorer
docker-compose up -d
```

### 2. Test Direct Access (Port 1480)
Visit: http://localhost:1480

### 3. Test Through Nginx (Port 80)
Visit: http://localhost

---

## Troubleshooting

### Nginx Can't Connect to Port 1480
```bash
# Check if Docker container is running
docker-compose ps

# Check if port 1480 is accessible
curl http://localhost:1480
```

### Permission Denied on Static Files (Linux)
```bash
# Fix permissions
sudo chown -R www-data:www-data /path/to/staticfiles/
sudo chown -R www-data:www-data /path/to/mediafiles/
```

### Static Files Not Loading
```bash
# Verify paths are correct
ls /path/to/staticfiles/

# Check nginx error log
# Linux: sudo tail -f /var/log/nginx/error.log
# Windows: type C:\nginx\logs\error.log
```

---

## Common nginx Commands

```bash
# Start nginx (Linux/macOS)
sudo systemctl start nginx

# Stop nginx
sudo systemctl stop nginx

# Restart nginx
sudo systemctl restart nginx

# Reload configuration (no downtime)
sudo systemctl reload nginx

# Test configuration
sudo nginx -t

# View error logs
sudo tail -f /var/log/nginx/error.log

# View access logs
sudo tail -f /var/log/nginx/access.log
```

### Windows Commands
```bash
# Start nginx
start nginx

# Stop nginx
nginx -s stop

# Reload configuration
nginx -s reload

# View logs
type C:\nginx\logs\error.log
type C:\nginx\logs\access.log
```

---

## Architecture

```
Internet (Port 80/443)
         ↓
    External Nginx
         ↓
    localhost:1480
         ↓
Docker Container (Django + Gunicorn)
```

---

## Performance Tuning

### For High Traffic

```nginx
# Increase worker connections
events {
    worker_connections 4096;
}

# Enable gzip compression
http {
    gzip on;
    gzip_vary on;
    gzip_min_length 1024;
    gzip_types text/css application/javascript image/svg+xml;
}

# Enable caching
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m;

server {
    location / {
        proxy_cache my_cache;
        proxy_pass http://localhost:1480;
    }
}
```

---

## Security Headers

Add to your server block:
```nginx
# Security headers
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Referrer-Policy "no-referrer-when-downgrade" always;
add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;

# Hide nginx version
server_tokens off;
```

---

## Next Steps

1. ✅ Install nginx on your host machine
2. ✅ Copy and configure nginx.conf
3. ✅ Update file paths in configuration
4. ✅ Test configuration
5. ✅ Start Docker container
6. ✅ Start nginx
7. ✅ Access via http://localhost

For production:
8. ⬜ Get domain name
9. ⬜ Configure DNS
10. ⬜ Get SSL certificate
11. ⬜ Enable HTTPS configuration
12. ⬜ Set up firewall rules

---

**Your Django app runs in Docker on port 1480, nginx runs outside Docker and proxies to it!** 🚀
