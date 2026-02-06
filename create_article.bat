@echo off
echo ========================================
echo Creating Sample Article
echo ========================================
echo.

cd src
python manage.py create_sample_article

echo.
echo ========================================
echo Done!
echo ========================================
echo.
echo View your article at:
echo  - Article page: http://localhost:8000/laptops/article/macbook-air-m2-review-2024/
echo  - All articles: http://localhost:8000/laptops/articles/
echo  - Homepage: http://localhost:8000 (Expert Articles section)
echo.
pause
