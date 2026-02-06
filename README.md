# 💻 LaptopXplorer

A modern Django-based laptop marketplace platform with advanced filtering, multi-image galleries, article system, and futuristic UI design.

**🌐 Live Demo**: https://laptopxplorer.ayubsoft-inc.systems  
**📦 Repository**: https://github.com/ayubsoft254/laptopXplorer

> Built with GitHub Copilot CLI for the [GitHub Copilot CLI Challenge](https://dev.to/challenges/github-2026-01-21)

## Features

- **Comprehensive Laptop Catalog** - Browse laptops with detailed specifications and multiple images
- **Multi-Image Galleries** - Each laptop showcases multiple product images
- **Advanced Filtering** - Filter by brand, category, price range, and specifications
- **Article System** - Tech news and laptop buying guides with full CRUD capabilities
- **SEO Optimized** - XML sitemaps, Schema.org structured data, Open Graph tags
- **Futuristic UI** - Gradient-heavy design with smooth animations
- **Responsive Design** - Mobile-friendly interface
- **Admin Dashboard** - Comprehensive content management

## Tech Stack

- **Backend:** Django 5.0.7, Python 3.12
- **Frontend:** HTML5, CSS3 (Custom futuristic design)
- **Database:** SQLite (development), PostgreSQL-ready
- **Deployment:** Docker, Docker Compose, Gunicorn, Nginx
- **Server:** Ubuntu 22.04 LTS with SSL (Let's Encrypt)

## Setup Instructions

### Prerequisites

- Python 3.10+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ayubsoft254/laptopXplorer.git
cd laptopXplorer
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Mac/Linux:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
cd src
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

7. Access the application:
- Frontend: http://localhost:8000
- Admin: http://localhost:8000/admin

## Project Structure

```
laptopXplorer/
├── src/
│   ├── config/           # Project settings
│   ├── laptops/          # Laptops app
│   ├── brands/           # Brands app  
│   ├── core/             # Core app (home, static pages)
│   ├── templates/        # HTML templates
│   ├── static/           # Static files
│   └── manage.py
├── .venv/                # Virtual environment
├── requirements.txt      # Python dependencies
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Author

[ayubsoft254](https://github.com/ayubsoft254)
