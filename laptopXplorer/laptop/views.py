from django.shortcuts import render
from laptop.models import Laptop

# Create your views here.
def site_home(request):
    laptops = Laptop.objects.all()
    context = {'laptops':laptops}         
    return render(request, 'index.html', context)
