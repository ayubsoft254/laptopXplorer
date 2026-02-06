# Git Commands for Manual Commit

If the batch file doesn't work, run these commands manually:

```bash
# Navigate to project directory
cd C:\Users\henry\Desktop\laptopXplorer

# Check status
git status

# Add all changes
git add .

# Commit with message
git commit -m "Complete rebuild: Full-featured laptop comparison platform"

# Push to GitHub (main branch)
git push origin main

# If main doesn't work, try master
git push origin master

# Or if you need to set upstream
git push -u origin main
```

## If You Get Authentication Errors

### Option 1: Using GitHub CLI
```bash
gh auth login
```

### Option 2: Using Personal Access Token
1. Go to GitHub.com → Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Copy the token
4. When prompted for password, paste the token

### Option 3: Using SSH
```bash
# Check if you have SSH key
ssh -T git@github.com

# If not, generate one
ssh-keygen -t ed25519 -C "henryoayub15@gmail.com"

# Add to GitHub
# Copy the public key and add it to GitHub Settings → SSH Keys
cat ~/.ssh/id_ed25519.pub
```

## After Successful Push

Your changes will be live at:
https://github.com/ayubsoft254/laptopXplorer

## Files Being Committed

**Configuration Files:**
- requirements.txt
- .env.example
- README.md
- SETUP.md
- PROJECT_STATUS.md
- install.bat
- migrate.bat
- create_dirs.bat

**Django Source Code:**
- src/config/* (settings, urls)
- src/laptops/* (models, views, admin, urls)
- src/core/* (views, urls)

**Templates:**
- src/templates/base.html
- src/templates/core/*.html (3 files)
- src/templates/laptops/*.html (6 files)

**Total:** ~25+ files with 1000+ lines of code
