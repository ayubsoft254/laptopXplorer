from django.shortcuts import render
from laptops.models import Laptop, Brand, Category, Review, Article


def home(request):
    """Home page with featured laptops"""
    featured_laptops = Laptop.objects.select_related('brand', 'category', 'processor').filter(in_stock=True)[:6]
    latest_laptops = Laptop.objects.select_related('brand', 'category', 'processor').order_by('-created_at')[:8]
    recent_reviews = Review.objects.select_related('laptop', 'laptop__brand').order_by('-created_at')[:6]
    featured_articles = Article.objects.select_related('laptop', 'laptop__brand').filter(published=True, featured=True)[:3]
    brands = Brand.objects.all()[:8]
    categories = Category.objects.all()
    
    context = {
        'featured_laptops': featured_laptops,
        'latest_laptops': latest_laptops,
        'recent_reviews': recent_reviews,
        'featured_articles': featured_articles,
        'brands': brands,
        'categories': categories,
    }
    
    return render(request, 'core/home.html', context)


def about(request):
    """About page"""
    return render(request, 'core/about.html')


def contact(request):
    """Contact page"""
    return render(request, 'core/contact.html')
