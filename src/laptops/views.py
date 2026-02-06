from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Min, Max
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from .models import Laptop, Brand, Category, Processor, Article


def laptop_list(request):
    """Display all laptops with advanced filtering and search"""
    laptops = Laptop.objects.select_related('brand', 'category', 'processor').all()
    
    # Track active filters count
    active_filters = 0
    
    # Search
    search_query = request.GET.get('q', '')
    if search_query:
        laptops = laptops.filter(
            Q(name__icontains=search_query) |
            Q(brand__name__icontains=search_query) |
            Q(model_number__icontains=search_query) |
            Q(processor__name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
        active_filters += 1
    
    # Filter by multiple brands
    brand_ids = request.GET.getlist('brand')
    if brand_ids:
        laptops = laptops.filter(brand_id__in=brand_ids)
        active_filters += len(brand_ids)
    
    # Filter by multiple categories
    category_ids = request.GET.getlist('category')
    if category_ids:
        laptops = laptops.filter(category_id__in=category_ids)
        active_filters += len(category_ids)
    
    # Filter by price range
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        laptops = laptops.filter(price__gte=min_price)
        active_filters += 1
    if max_price:
        laptops = laptops.filter(price__lte=max_price)
        active_filters += 1
    
    # Filter by multiple RAM sizes
    ram_sizes = request.GET.getlist('ram')
    if ram_sizes:
        laptops = laptops.filter(ram_size__in=ram_sizes)
        active_filters += len(ram_sizes)
    
    # Filter by multiple storage sizes
    storage_sizes = request.GET.getlist('storage')
    if storage_sizes:
        laptops = laptops.filter(storage_size__in=storage_sizes)
        active_filters += len(storage_sizes)
    
    # Filter by screen size
    screen_sizes = request.GET.getlist('screen')
    if screen_sizes:
        # Convert screen sizes to ranges
        screen_filters = Q()
        for size in screen_sizes:
            if size == '13':
                screen_filters |= Q(display_size__lt=14)
            elif size == '14':
                screen_filters |= Q(display_size__gte=14, display_size__lt=15)
            elif size == '15':
                screen_filters |= Q(display_size__gte=15, display_size__lt=16)
            elif size == '16':
                screen_filters |= Q(display_size__gte=16, display_size__lt=17)
            elif size == '17':
                screen_filters |= Q(display_size__gte=17)
        laptops = laptops.filter(screen_filters)
        active_filters += len(screen_sizes)
    
    # Filter by weight
    weight_category = request.GET.get('weight')
    if weight_category:
        if weight_category == 'ultraportable':
            laptops = laptops.filter(weight__lt=1.5)  # Less than 1.5kg (~3.3lbs)
        elif weight_category == 'standard':
            laptops = laptops.filter(weight__gte=1.5, weight__lt=2.5)  # 1.5-2.5kg
        elif weight_category == 'heavy':
            laptops = laptops.filter(weight__gte=2.5)  # Over 2.5kg (~5.5lbs)
        active_filters += 1
    
    # Filter by battery life
    min_battery = request.GET.get('min_battery')
    if min_battery:
        laptops = laptops.filter(battery_life__gte=min_battery)
        active_filters += 1
    
    # Filter by graphics type
    graphics_types = request.GET.getlist('graphics')
    if graphics_types:
        laptops = laptops.filter(graphics_type__in=graphics_types)
        active_filters += len(graphics_types)
    
    # Filter by OS
    os_list = request.GET.getlist('os')
    if os_list:
        laptops = laptops.filter(operating_system__in=os_list)
        active_filters += len(os_list)
    
    # Sorting
    sort_by = request.GET.get('sort', '-created_at')
    valid_sorts = ['price', '-price', 'name', '-name', '-created_at', 'created_at', 'ram_size', '-ram_size']
    if sort_by in valid_sorts:
        laptops = laptops.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(laptops, 12)  # 12 laptops per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get filter options
    brands = Brand.objects.all()
    categories = Category.objects.all()
    
    # Get price range from all laptops
    price_range = Laptop.objects.aggregate(
        min_price=Min('price'),
        max_price=Max('price')
    )
    
    # Get unique RAM and storage options
    ram_options = sorted(set(filter(None, Laptop.objects.values_list('ram_size', flat=True).distinct())))
    storage_options = sorted(set(filter(None, Laptop.objects.values_list('storage_size', flat=True).distinct())))
    
    # Get unique graphics types
    graphics_options = sorted(set(filter(None, Laptop.objects.values_list('graphics_type', flat=True).distinct())))
    
    # Get unique OS options
    os_options = sorted(set(filter(None, Laptop.objects.values_list('operating_system', flat=True).distinct())))
    
    context = {
        'page_obj': page_obj,
        'brands': brands,
        'categories': categories,
        'ram_options': ram_options,
        'storage_options': storage_options,
        'graphics_options': graphics_options,
        'os_options': os_options,
        'price_range': price_range,
        'search_query': search_query,
        'selected_brands': brand_ids,
        'selected_categories': category_ids,
        'selected_rams': ram_sizes,
        'selected_storages': storage_sizes,
        'selected_screens': screen_sizes if 'screen_sizes' in locals() else [],
        'selected_graphics': graphics_types if 'graphics_types' in locals() else [],
        'selected_os': os_list if 'os_list' in locals() else [],
        'selected_weight': weight_category,
        'min_price_selected': min_price,
        'max_price_selected': max_price,
        'min_battery_selected': min_battery,
        'sort_by': sort_by,
        'active_filters': active_filters,
        'total_results': paginator.count,
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
    
    # Get reviews
    reviews = laptop.reviews.all()
    
    # Handle review submission
    if request.method == 'POST':
        from .models import Review
        user_name = request.POST.get('user_name')
        rating = request.POST.get('rating')
        title = request.POST.get('title')
        comment = request.POST.get('comment')
        pros = request.POST.get('pros', '')
        cons = request.POST.get('cons', '')
        email = request.POST.get('email', '')
        
        if user_name and rating and title and comment:
            Review.objects.create(
                laptop=laptop,
                user_name=user_name,
                email=email,
                rating=int(rating),
                title=title,
                comment=comment,
                pros=pros,
                cons=cons
            )
            return redirect('laptops:laptop_detail', slug=slug)
    
    context = {
        'laptop': laptop,
        'similar_laptops': similar_laptops,
        'reviews': reviews,
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


def autocomplete_search(request):
    """AJAX endpoint for search autocomplete"""
    query = request.GET.get('q', '')
    suggestions = []
    
    if len(query) >= 2:
        # Search laptops
        laptops = Laptop.objects.filter(
            Q(name__icontains=query) |
            Q(brand__name__icontains=query) |
            Q(model_number__icontains=query)
        ).select_related('brand')[:8]
        
        for laptop in laptops:
            suggestions.append({
                'type': 'laptop',
                'name': f"{laptop.brand.name} {laptop.name}",
                'price': float(laptop.price),
                'url': f'/laptops/{laptop.slug}/'
            })
    
    return JsonResponse({'suggestions': suggestions})


def robots_txt(request):
    """Serve robots.txt dynamically"""
    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        "# Disallow admin and user account pages",
        "Disallow: /admin/",
        "Disallow: /accounts/login/",
        "Disallow: /accounts/signup/",
        "Disallow: /accounts/password/",
        "",
        "# Allow all laptops, brands, and articles",
        "Allow: /laptops/",
        "Allow: /articles/",
        "",
        "# Sitemap location",
        f"Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def article_list(request):
    """Display all published articles"""
    articles = Article.objects.select_related('laptop', 'laptop__brand').filter(published=True)
    
    # Pagination
    paginator = Paginator(articles, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    
    return render(request, 'laptops/article_list.html', context)


def article_detail(request, slug):
    """Display single article"""
    article = get_object_or_404(
        Article.objects.select_related('laptop', 'laptop__brand'),
        slug=slug,
        published=True
    )
    
    # Increment views
    article.views += 1
    article.save(update_fields=['views'])
    
    # Get related articles (same laptop or recent)
    related_articles = Article.objects.filter(published=True).exclude(id=article.id).select_related('laptop', 'laptop__brand')[:3]
    
    context = {
        'article': article,
        'related_articles': related_articles,
    }
    
    return render(request, 'laptops/article_detail.html', context)


def compare_laptops(request):
    """Compare multiple laptops side by side"""
    # Get IDs from query string - can be comma-separated or multiple params
    ids_param = request.GET.get('ids', '')
    
    if ',' in ids_param:
        # Comma-separated IDs (e.g., ?ids=1,2,3)
        laptop_ids = [id.strip() for id in ids_param.split(',') if id.strip()]
    else:
        # Multiple id parameters (e.g., ?ids=1&ids=2&ids=3)
        laptop_ids = request.GET.getlist('ids')
    
    if not laptop_ids:
        return redirect('laptops:laptop_list')
    
    laptops = Laptop.objects.filter(id__in=laptop_ids).select_related('brand', 'category', 'processor')
    
    if laptops.count() < 2:
        return redirect('laptops:laptop_list')
    
    context = {
        'laptops': laptops,
    }
    
    return render(request, 'laptops/compare.html', context)
