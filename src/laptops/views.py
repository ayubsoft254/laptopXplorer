from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop, Brand, Rating
from .forms import RatingForm
from django.contrib import messages
from django.db.models import Q

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
        'user': request.user,        
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

def rate_laptop(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    if request.method == 'POST':
        score = int(request.POST.get('score'))
        comment = request.POST.get('comment', '')
       
        if 1 <= score <= 5:
            rating, created = Rating.objects.update_or_create(
                laptop=laptop,
                user=request.user,
                defaults={'score': score, 'comment': comment}
            )            
        else:
            messages.error(request, 'Invalid score. Please enter a score between 1 and 5.')            

    return redirect('laptop_detail', laptop_id=laptop_id)

def laptop_rating_form(request, laptop_id):
    laptop = Laptop.objects.get(id=laptop_id)
    form = RatingForm()
    return render(request, 'forms/rate.html', {'laptop': laptop, 'form': form})

def laptop_search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = Laptop.objects.filter(
            Q(name__icontains=query) |
            Q(brand__name__icontains=query) |
            Q(model__icontains=query)
        )

     
    return render(request, 'laptops/searchresults.html', {'results': results, 'query': query})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render (request, 'contact.html')  