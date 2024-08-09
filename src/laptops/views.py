from django.shortcuts import render, get_object_or_404
from .models import Laptop


def landing_view(request):
    return render(request, "land.html", {})

def laptops_list(request):
    laptops = Laptop.objects.all()    

    context = {
        'laptops': laptops
    }
    return render(request, "laptops/laptop_list.html", context)

def laptop_detail(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    context = {
        'laptop': laptop,        
    }
    return render(request, "laptops/laptop_detail.html", context)

