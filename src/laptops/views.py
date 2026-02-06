from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Laptop, Brand, Category, Processor


def laptop_list(request):
    """Display all laptops with filtering and search"""
    laptops = Laptop.objects.select_related('brand', 'category', 'processor').all()
    
    # Search
    search_query = request.GET.get('q', '')
    if search_query:
        laptops = laptops.filter(
            Q(name__icontains=search_query) |
            Q(brand__name__icontains=search_query) |
            Q(model_number__icontains=search_query) |
            Q(processor__name__icontains=search_query)
        )
    
    # Filter by brand
    brand_id = request.GET.get('brand')
    if brand_id:
        laptops = laptops.filter(brand_id=brand_id)
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        laptops = laptops.filter(category_id=category_id)
    
    # Filter by price range
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        laptops = laptops.filter(price__gte=min_price)
    if max_price:
        laptops = laptops.filter(price__lte=max_price)
    
    # Filter by RAM
    ram_size = request.GET.get('ram')
    if ram_size:
        laptops = laptops.filter(ram_size=ram_size)
    
    # Filter by storage
    storage_size = request.GET.get('storage')
    if storage_size:
        laptops = laptops.filter(storage_size__gte=storage_size)
    
    # Sorting
    sort_by = request.GET.get('sort', '-created_at')
    valid_sorts = ['price', '-price', 'name', '-name', '-created_at', 'created_at']
    if sort_by in valid_sorts:
        laptops = laptops.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(laptops, 12)  # 12 laptops per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get filter options
    brands = Brand.objects.all()
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'brands': brands,
        'categories': categories,
        'search_query': search_query,
        'selected_brand': brand_id,
        'selected_category': category_id,
        'sort_by': sort_by,
    }
    
    return render(request, 'laptops/laptop_list.html', context)


def laptop_detail(request, slug):
    """Display detailed information about a specific laptop"""
    laptop = get_object_or_404(Laptop.objects.select_related('brand', 'category', 'processor'), slug=slug)
    
    # Increment views
    laptop.views += 1
    laptop.save(update_fields=['views'])
    
    # Get similar laptops (same brand or category)
    similar_laptops = Laptop.objects.filter(
        Q(brand=laptop.brand) | Q(category=laptop.category)
    ).exclude(id=laptop.id).select_related('brand', 'category')[:4]
    
    context = {
        'laptop': laptop,
        'similar_laptops': similar_laptops,
    }
    
    return render(request, 'laptops/laptop_detail.html', context)


def brand_list(request):
    """Display all brands"""
    brands = Brand.objects.all()
    
    context = {
        'brands': brands,
    }
    
    return render(request, 'laptops/brand_list.html', context)


def brand_detail(request, slug):
    """Display laptops from a specific brand"""
    brand = get_object_or_404(Brand, slug=slug)
    laptops = Laptop.objects.filter(brand=brand).select_related('category', 'processor')
    
    # Sorting
    sort_by = request.GET.get('sort', '-created_at')
    valid_sorts = ['price', '-price', 'name', '-name', '-created_at']
    if sort_by in valid_sorts:
        laptops = laptops.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(laptops, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'brand': brand,
        'page_obj': page_obj,
    }
    
    return render(request, 'laptops/brand_detail.html', context)


def compare_laptops(request):
    """Compare multiple laptops side by side"""
    laptop_ids = request.GET.getlist('ids')
    
    if not laptop_ids:
        return redirect('laptop_list')
    
    laptops = Laptop.objects.filter(id__in=laptop_ids).select_related('brand', 'category', 'processor')
    
    if laptops.count() < 2:
        return redirect('laptop_list')
    
    context = {
        'laptops': laptops,
    }
    
    return render(request, 'laptops/compare.html', context)
