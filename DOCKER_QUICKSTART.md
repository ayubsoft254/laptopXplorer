# 🚀 Quick Docker Deployment

## Setup (External Nginx)

Your Django app runs in Docker on **port 1480**.  
Nginx runs **externally** and proxies to it.

---

## 1. Start Django Container

```bash
docker-compose up -d --build
```

**Container runs on:** http://localhost:1480

---

## 2. Configure External Nginx

### Install Nginx (if not installed)

**Linux/Ubuntu:**
```bash
sudo apt install nginx
```

**Windows:**  
Download from https://nginx.org/en/download.html

**macOS:**
```bash
brew install nginx
```

### Setup Configuration

**Linux:**
```bash
sudo cp nginx.conf /etc/nginx/sites-available/laptopxplorer
sudo ln -s /etc/nginx/sites-available/laptopxplorer /etc/nginx/sites-enabled/
```

**Update paths in nginx.conf:**
```nginx
location /static/ {
    alias /path/to/laptopXplorer/staticfiles/;
}
location /media/ {
    alias /path/to/laptopXplorer/mediafiles/;
}
```

### Test & Start Nginx

```bash
# Test configuration
sudo nginx -t

# Start nginx
sudo systemctl start nginx

# Or reload if already running
sudo systemctl reload nginx
```

---

## 3. Access Application

- **Direct (Django):** http://localhost:1480
- **Via Nginx:** http://localhost
- **Admin Panel:** http://localhost/admin
  - Username: `admin`
  - Password: `admin123`

---

## Architecture

```
Internet (Port 80)
      ↓
 External Nginx
      ↓
localhost:1480
      ↓
Docker Container
 (Django + Gunicorn)
```

---

## Common Commands

### Docker Container
```bash
# Start
docker-compose up -d

# Stop
docker-compose down

# Logs
docker-compose logs -f

# Restart
docker-compose restart
```

### Nginx (External)
```bash
# Linux/macOS
sudo systemctl start nginx
sudo systemctl stop nginx
sudo systemctl reload nginx

# Windows
start nginx
nginx -s stop
nginx -s reload
```

---

## Files

- **nginx.conf** - External nginx configuration (proxies to port 1480)
- **NGINX_EXTERNAL.md** - Detailed nginx setup guide
- **docker-compose.yaml** - Django container only (no nginx)

---

**That's it! 🎉**

- Django runs in Docker on port 1480
- Nginx runs externally and proxies to it
- Access via http://localhost (port 80)

