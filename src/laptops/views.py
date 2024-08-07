from django.shortcuts import render, get_object_or_404
from .models import Laptop

# Create your views here.
def landing_view(request):
    return render(request, "land.html", {})

def laptops_list(request):
    laptops = Laptop.objects.all()
    context = {
        'laptops': laptops  # Use the variable instead of string
    }
    return render(request, "laptops/laptop_list.html", context)

def laptop_detail(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)  # Use get_object_or_404 for better error handling
    context = {
        'laptop': laptop  # Use a singular form to represent a single laptop
    }
    return render(request, "laptops/laptop_detail.html", context)
