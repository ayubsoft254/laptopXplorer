# LaptopXplorer

A web-based platform for exploring and comparing laptops, inspired by GSMArena. Built with Django and Tailwind CSS.

## Features

- **Comprehensive Laptop Database** - Detailed specifications for laptops across multiple brands
- **Advanced Search & Filtering** - Search by brand, price, specifications, and more
- **Comparison Tool** - Compare multiple laptops side by side
- **Responsive Design** - Built with Tailwind CSS for a sleek, mobile-friendly interface
- **Admin Dashboard** - Manage laptop database efficiently

## Tech Stack

- **Backend:** Django 5.0.7
- **Frontend:** HTML, Tailwind CSS
- **Database:** SQLite (development)

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
