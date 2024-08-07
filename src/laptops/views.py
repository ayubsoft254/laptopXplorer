from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Laptop, Rating
from .forms import RatingForm
from django.contrib.auth.decorators import login_required

def landing_view(request):
    return render(request, "land.html", {})

def laptops_list(request):
    laptops = Laptop.objects.all()
    for laptop in laptops:
        laptop.avg_rating = Rating.objects.filter(laptop=laptop).aggregate(Avg('rating'))['rating__avg'] or 0

    context = {
        'laptops': laptops
    }
    return render(request, "laptops/laptop_list.html", context)

def laptop_detail(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    ratings = Rating.objects.filter(laptop=laptop)
    avg_rating = ratings.aggregate(Avg('rating'))['rating__avg'] or 0

    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(laptop=laptop, user=request.user).first()

    context = {
        'laptop': laptop,
        'ratings': ratings,
        'avg_rating': avg_rating,
        'user_rating': user_rating,
        'form': RatingForm(instance=user_rating)
    }
    return render(request, "laptops/laptop_detail.html", context)

@login_required
def rate_laptop(request, laptop_id):
    laptop = get_object_or_404(Laptop, id=laptop_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating, created = Rating.objects.update_or_create(
                laptop=laptop,
                user=request.user,
                defaults={'rating': form.cleaned_data['rating'], 'comment': form.cleaned_data['comment']}
            )
            return redirect('laptop_detail', laptop_id=laptop_id)
    else:
        form = RatingForm()

    context = {
        'laptop': laptop,
        'form': form
    }
    return render(request, 'laptops/rate_laptop.html', context)
