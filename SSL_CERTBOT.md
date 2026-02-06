# 🔒 SSL/HTTPS Setup with Certbot

## Overview

This guide shows how to add HTTPS/SSL to your nginx configuration using Certbot.

---

## Prerequisites

- ✅ Domain DNS configured (laptopxplorer.ayubsoft-inc.systems → Server IP)
- ✅ Nginx running with HTTP (port 80)
- ✅ Docker container running on port 1480
- ✅ Ports 80 and 443 open on firewall

---

## 1. Install Certbot

### Ubuntu/Debian
```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx
```

### CentOS/RHEL
```bash
sudo yum install certbot python3-certbot-nginx
```

### Verify Installation
```bash
certbot --version
```

---

## 2. Run Certbot

### Automatic Configuration (Recommended)

Certbot will automatically configure nginx for HTTPS:

```bash
sudo certbot --nginx -d laptopxplorer.ayubsoft-inc.systems
```

**During setup, you'll be asked:**

1. **Email address** - For renewal notifications
   ```
   Enter email address: your-email@example.com
   ```

2. **Terms of Service** - Press `Y` to agree
   ```
   (A)gree/(C)ancel: A
   ```

3. **Share email?** - Press `N` (optional)
   ```
   (Y)es/(N)o: N
   ```

4. **Redirect HTTP to HTTPS?** - Press `2` (Recommended)
   ```
   1: No redirect
   2: Redirect - Make all requests redirect to secure HTTPS
   
   Select: 2
   ```

**Certbot will:**
- ✅ Obtain SSL certificate from Let's Encrypt
- ✅ Automatically update nginx.conf
- ✅ Add HTTPS server block (port 443)
- ✅ Configure SSL settings
- ✅ Set up HTTP → HTTPS redirect
- ✅ Enable auto-renewal

---

## 3. Verify HTTPS

### Test Access
Visit your site:
```
https://laptopxplorer.ayubsoft-inc.systems
```

### Check Certificate
```bash
sudo certbot certificates
```

Output should show:
```
Certificate Name: laptopxplorer.ayubsoft-inc.systems
  Domains: laptopxplorer.ayubsoft-inc.systems
  Expiry Date: 2024-05-06 (VALID: 89 days)
  Certificate Path: /etc/letsencrypt/live/laptopxplorer.ayubsoft-inc.systems/fullchain.pem
  Private Key Path: /etc/letsencrypt/live/laptopxplorer.ayubsoft-inc.systems/privkey.pem
```

---

## 4. Verify Auto-Renewal

Certbot sets up automatic renewal via systemd timer.

### Check Timer Status
```bash
sudo systemctl status certbot.timer
```

Should show: `Active: active (waiting)`

### Test Renewal (Dry Run)
```bash
sudo certbot renew --dry-run
```

Should complete without errors.

---

## 5. What Certbot Changes

After running certbot, your nginx.conf will have:

### Added HTTPS Server Block
```nginx
server {
    listen 443 ssl http2;
    server_name laptopxplorer.ayubsoft-inc.systems;

    ssl_certificate /etc/letsencrypt/live/laptopxplorer.ayubsoft-inc.systems/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/laptopxplorer.ayubsoft-inc.systems/privkey.pem;
    include /etc/letsencrypt/options-ssl-nginx.conf;
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem;

    # ... rest of your configuration
}
```

### Modified HTTP Block (Redirect)
```nginx
server {
    listen 80;
    server_name laptopxplorer.ayubsoft-inc.systems;
    
    if ($host = laptopxplorer.ayubsoft-inc.systems) {
        return 301 https://$host$request_uri;
    }
    
    return 404;
}
```

---

## 6. Firewall Configuration

### Ubuntu/Debian (UFW)
```bash
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'
sudo ufw reload
```

Or manually:
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

## 7. Test SSL Configuration

### Online SSL Test
Visit: https://www.ssllabs.com/ssltest/

Enter: `laptopxplorer.ayubsoft-inc.systems`

**Goal:** A or A+ rating

### Command Line Test
```bash
openssl s_client -connect laptopxplorer.ayubsoft-inc.systems:443 -servername laptopxplorer.ayubsoft-inc.systems
```

---

## Troubleshooting

### Port 80 Required Error

**Error:**
```
Problem binding to port 80: Could not bind to IPv4 or IPv6.
```

**Solution:**
```bash
# Check what's using port 80
sudo netstat -tlnp | grep :80

# If nginx is running, stop it temporarily
sudo systemctl stop nginx

# Run certbot
sudo certbot --nginx -d laptopxplorer.ayubsoft-inc.systems

# Start nginx
sudo systemctl start nginx
```

### DNS Not Resolving

**Error:**
```
Detail: DNS problem: NXDOMAIN looking up A for laptopxplorer.ayubsoft-inc.systems
```

**Solution:**
```bash
# Verify DNS
nslookup laptopxplorer.ayubsoft-inc.systems

# If not resolving, wait 10-30 minutes for DNS propagation
# Or check DNS configuration at your registrar
```

### Certificate Already Exists

**Error:**
```
Certificate already exists
```

**Solution:**
```bash
# Renew/reinstall
sudo certbot --nginx --reinstall -d laptopxplorer.ayubsoft-inc.systems

# Or force renewal
sudo certbot renew --force-renewal
```

---

## Certificate Management

### View Certificates
```bash
sudo certbot certificates
```

### Renew Certificate Manually
```bash
sudo certbot renew
```

### Renew Specific Certificate
```bash
sudo certbot renew --cert-name laptopxplorer.ayubsoft-inc.systems
```

### Delete Certificate
```bash
sudo certbot delete --cert-name laptopxplorer.ayubsoft-inc.systems
```

---

## Auto-Renewal

Certbot automatically renews certificates 30 days before expiry.

### Check Auto-Renewal Configuration
```bash
# Systemd timer
sudo systemctl list-timers certbot.timer

# Cron (older systems)
sudo crontab -l | grep certbot
```

### Force Test Renewal
```bash
sudo certbot renew --dry-run
```

### Manual Renewal (if needed)
```bash
sudo certbot renew
sudo systemctl reload nginx
```

---

## Security Enhancements (Optional)

After certbot setup, you can enhance security:

### Add Security Headers

Edit your nginx config:
```bash
sudo nano /etc/nginx/sites-available/laptopxplorer
```

Add in the HTTPS server block:
```nginx
server {
    listen 443 ssl http2;
    # ... certbot configs ...
    
    # Security headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    
    # ... rest of config
}
```

Test and reload:
```bash
sudo nginx -t
sudo systemctl reload nginx
```

---

## Quick Reference

```bash
# Install certbot
sudo apt install certbot python3-certbot-nginx

# Get certificate + auto-configure nginx
sudo certbot --nginx -d laptopxplorer.ayubsoft-inc.systems

# Test renewal
sudo certbot renew --dry-run

# View certificates
sudo certbot certificates

# Renew certificates
sudo certbot renew

# Check auto-renewal timer
sudo systemctl status certbot.timer
```

---

## Expected Result

After certbot setup:

✅ **HTTPS:** https://laptopxplorer.ayubsoft-inc.systems  
✅ **HTTP redirects to HTTPS** automatically  
✅ **Valid SSL certificate** (green padlock in browser)  
✅ **Auto-renewal** configured (renews every 60 days)  
✅ **A/A+ SSL rating** on SSL Labs  

---

## Support

If you encounter issues:

1. Check certbot logs:
   ```bash
   sudo tail -f /var/log/letsencrypt/letsencrypt.log
   ```

2. Check nginx logs:
   ```bash
   sudo tail -f /var/log/nginx/error.log
   ```

3. Verify DNS:
   ```bash
   nslookup laptopxplorer.ayubsoft-inc.systems
   ```

4. Test nginx config:
   ```bash
   sudo nginx -t
   ```

---

**🔒 SSL setup complete with certbot! Your site is now secure!** 🎉
