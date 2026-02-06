# 🐳 Docker Deployment Guide

## Quick Start

### 1. Build and Start Containers
```bash
docker-compose up -d --build
```

### 2. Access Application
- **Main App:** http://localhost:1480
- **Admin Panel:** http://localhost:1480/admin
  - Username: `admin`
  - Password: `admin123` (auto-created)

### 3. With Nginx (Port 80)
```bash
docker-compose up -d
```
Then visit: http://localhost

---

## 📦 What's Included

### Services:
- **web** - Django application (Port 1480)
- **db** - PostgreSQL 15 database
- **nginx** - Reverse proxy & static file server (Port 80)

### Volumes:
- `postgres_data` - Database persistence
- `static_volume` - Static files (CSS, JS)
- `media_volume` - User uploads (images)

---

## 🛠️ Common Commands

### Start Services
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f web
```

### Stop Services
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (⚠️ deletes database)
docker-compose down -v
```

### Rebuild After Code Changes
```bash
docker-compose up -d --build
```

### Run Django Commands
```bash
# Run migrations
docker-compose exec web python src/manage.py migrate

# Create superuser
docker-compose exec web python src/manage.py createsuperuser

# Collect static files
docker-compose exec web python src/manage.py collectstatic

# Run shell
docker-compose exec web python src/manage.py shell
```

### Database Commands
```bash
# Access PostgreSQL shell
docker-compose exec db psql -U postgres -d laptopxplorer

# Backup database
docker-compose exec db pg_dump -U postgres laptopxplorer > backup.sql

# Restore database
docker-compose exec -T db psql -U postgres laptopxplorer < backup.sql
```

---

## ⚙️ Configuration

### Environment Variables

Edit `.env.docker` or create `.env`:

```env
# Django
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# Database
DATABASE_URL=postgresql://postgres:postgres@db:5432/laptopxplorer

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-password
```

### Using SQLite Instead of PostgreSQL

1. Edit `docker-compose.yaml`:
   ```yaml
   environment:
     - DATABASE_URL=sqlite:///db.sqlite3
   ```

2. Remove `db` service dependency:
   ```yaml
   # Comment out or remove:
   # depends_on:
   #   - db
   ```

3. Restart:
   ```bash
   docker-compose up -d --build
   ```

---

## 🚀 Production Deployment

### 1. Update Environment
```bash
cp .env.docker .env
# Edit .env with production values
```

### 2. Change Default Passwords
```bash
# In docker-compose.yaml, update:
POSTGRES_PASSWORD=your-secure-password
```

### 3. Update Django Settings
```bash
# In .env:
DEBUG=False
SECRET_KEY=generate-new-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### 4. Enable HTTPS (Production)
```bash
# In .env:
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### 5. Deploy
```bash
docker-compose -f docker-compose.yaml up -d --build
```

---

## 📊 Port Mapping

| Service | Internal Port | External Port | URL |
|---------|---------------|---------------|-----|
| Django (web) | 1480 | 1480 | http://localhost:1480 |
| Nginx | 80 | 80 | http://localhost |
| PostgreSQL | 5432 | - | Internal only |

---

## 🔧 Troubleshooting

### Container Won't Start
```bash
# Check logs
docker-compose logs web

# Check if port is in use
netstat -ano | findstr :1480  # Windows
lsof -i :1480                 # Linux/Mac

# Restart services
docker-compose restart
```

### Database Connection Error
```bash
# Check if database is running
docker-compose ps

# Restart database
docker-compose restart db

# Check database logs
docker-compose logs db
```

### Static Files Not Loading
```bash
# Collect static files
docker-compose exec web python src/manage.py collectstatic --noinput

# Restart nginx
docker-compose restart nginx
```

### Permission Errors
```bash
# Fix permissions (Linux/Mac)
sudo chown -R $USER:$USER staticfiles/ mediafiles/

# Windows: Run as administrator or adjust folder permissions
```

---

## 📁 File Structure

```
laptopXplorer/
├── Dockerfile              # Django app container config
├── docker-compose.yaml     # Multi-container orchestration
├── docker-entrypoint.sh    # Startup script
├── nginx.conf              # Nginx configuration
├── .dockerignore           # Files to exclude from image
├── .env.docker             # Environment variables template
└── src/                    # Django project
    ├── manage.py
    └── config/
        └── settings.py     # Updated for Docker
```

---

## 🎯 Next Steps

### After Deployment:

1. **Change Default Admin Password**
   ```bash
   docker-compose exec web python src/manage.py changepassword admin
   ```

2. **Create Sample Data**
   ```bash
   docker-compose exec web python src/manage.py shell
   # Import and create sample laptops, brands, etc.
   ```

3. **Monitor Logs**
   ```bash
   docker-compose logs -f --tail=100
   ```

4. **Set Up Backups**
   ```bash
   # Create backup script
   docker-compose exec db pg_dump -U postgres laptopxplorer > backups/backup_$(date +%Y%m%d).sql
   ```

---

## 🔒 Security Checklist

- [ ] Change default `SECRET_KEY`
- [ ] Set `DEBUG=False`
- [ ] Update `ALLOWED_HOSTS`
- [ ] Change database password
- [ ] Change default admin password
- [ ] Enable HTTPS in production
- [ ] Set up firewall rules
- [ ] Regular database backups
- [ ] Monitor logs for errors
- [ ] Keep Docker images updated

---

## 📚 Additional Resources

- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Docs](https://docs.docker.com/compose/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [PostgreSQL Docker](https://hub.docker.com/_/postgres)

---

**🎉 Your LaptopXplorer is now Dockerized!**

Access your app at: **http://localhost:1480** 🚀
