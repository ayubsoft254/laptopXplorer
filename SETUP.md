# Setup Instructions for LaptopXplorer

## Quick Start

Follow these steps to set up the project from scratch:

### 1. Activate Virtual Environment
```bash
# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Create Environment File
Copy `.env.example` to `.env` and update the values:
```bash
copy .env.example .env  # Windows
cp .env.example .env    # Mac/Linux
```

### 4. Initialize Django Project (First Time Only)
We'll create the Django project structure inside the `src` directory.

### 5. Run Migrations
```bash
cd src
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Server
```bash
python manage.py runserver
```

Visit http://localhost:8000

## Next Steps After Setup

1. Access admin panel: http://localhost:8000/admin
2. Add brands
3. Add categories
4. Add laptops
5. Test search and filter functionality
6. Test comparison tool

## Development Workflow

1. Always activate virtual environment before working
2. Make model changes → run `python manage.py makemigrations` → run `python manage.py migrate`
3. Collect static files for production: `python manage.py collectstatic`

## Troubleshooting

**Issue: Module not found**
- Solution: Make sure virtual environment is activated and dependencies are installed

**Issue: Database locked**
- Solution: Close all connections to the database and try again

**Issue: Static files not loading**
- Solution: Run `python manage.py collectstatic`
