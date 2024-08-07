
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Laptop, Rating
from django.db.models import Avg

def landing_view(request):
    return render(request, "landing.html", {})

def laptop_list(request):
    laptops = Laptop.objects.annotate(avg_rating=Avg('rating__score'))
    return render(request, 'laptops/laptop_list.html', {'laptops': laptops})

def laptop_detail(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(user=request.user, laptop=laptop).first()
    return render(request, 'laptops/laptop_detail.html', {'laptop': laptop, 'user_rating': user_rating})

@login_required
def rate_laptop(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    if request.method == 'POST':
        score = int(request.POST.get('rating'))
        Rating.objects.update_or_create(
            user=request.user,
            laptop=laptop,
            defaults={'score': score}
        )
    return redirect('laptop_detail', pk=pk)