from django.shortcuts import render
from laptops.models import Laptop, Brand, Category


def home(request):
    """Home page with featured laptops"""
    featured_laptops = Laptop.objects.select_related('brand', 'category', 'processor').filter(in_stock=True)[:6]
    brands = Brand.objects.all()[:8]
    categories = Category.objects.all()
    
    context = {
        'featured_laptops': featured_laptops,
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
