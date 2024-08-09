from django.shortcuts import render, get_object_or_404
from .models import Laptop, Brand


def landing_view(request):
    return render(request, "land.html", {})

def laptops_list(request):
    laptops = Laptop.objects.all()
    latest = Laptop.objects.all().order_by('-created_at')[:4]
    brands = Brand.objects.all()    

    context = {
        'laptops': laptops,
        'latest':latest,
        'brands':brands,
    }
    return render(request, "laptops/laptop_list.html", context)

def laptop_detail(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    latest = Laptop.objects.all().order_by('-created_at')[:4]
    context = {
        'laptop': laptop,
        'latest':latest,        
    }
    return render(request, "laptops/laptop_detail.html", context)

def laptops_by_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    laptops = Laptop.objects.filter(brand=brand)
    context = {
        'brand': brand,
        'laptops': laptops,
    }
    return render(request, "laptops/laptops_by_brand.html", context)

