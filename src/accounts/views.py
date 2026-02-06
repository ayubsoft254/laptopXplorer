from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile
from laptops.models import Laptop, Review


@login_required
def profile(request):
    """User profile page"""
    user_profile = request.user.profile
    favorites = user_profile.favorites.all()[:6]  # Show 6 recent favorites
    reviews = Review.objects.filter(email=request.user.email).order_by('-created_at')[:5]
    
    context = {
        'user_profile': user_profile,
        'favorites': favorites,
        'reviews': reviews,
    }
    
    return render(request, 'accounts/profile.html', context)


@login_required
def edit_profile(request):
    """Edit user profile"""
    user_profile = request.user.profile
    
    if request.method == 'POST':
        # Update user fields
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.save()
        
        # Update profile fields
        user_profile.bio = request.POST.get('bio', '')
        user_profile.location = request.POST.get('location', '')
        user_profile.website = request.POST.get('website', '')
        user_profile.newsletter_subscription = request.POST.get('newsletter_subscription') == 'on'
        user_profile.email_notifications = request.POST.get('email_notifications') == 'on'
        
        # Handle avatar upload
        if request.FILES.get('avatar'):
            user_profile.avatar = request.FILES['avatar']
        
        user_profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('accounts:profile')
    
    context = {
        'user_profile': user_profile,
    }
    
    return render(request, 'accounts/edit_profile.html', context)


@login_required
def dashboard(request):
    """User dashboard with overview"""
    user_profile = request.user.profile
    favorites = user_profile.favorites.all()
    reviews = Review.objects.filter(email=request.user.email).order_by('-created_at')
    
    # Get statistics
    stats = {
        'favorites_count': favorites.count(),
        'reviews_count': reviews.count(),
        'avg_rating': sum(r.rating for r in reviews) / reviews.count() if reviews.count() > 0 else 0,
    }
    
    context = {
        'user_profile': user_profile,
        'favorites': favorites[:6],
        'recent_reviews': reviews[:5],
        'stats': stats,
    }
    
    return render(request, 'accounts/dashboard.html', context)


@login_required
def favorites(request):
    """User's favorite laptops"""
    user_profile = request.user.profile
    favorites = user_profile.favorites.select_related('brand', 'category', 'processor').all()
    
    context = {
        'favorites': favorites,
    }
    
    return render(request, 'accounts/favorites.html', context)


@login_required
def toggle_favorite(request, laptop_id):
    """Add/remove laptop from favorites"""
    laptop = get_object_or_404(Laptop, id=laptop_id)
    user_profile = request.user.profile
    
    if laptop in user_profile.favorites.all():
        user_profile.favorites.remove(laptop)
        messages.success(request, f'{laptop.name} removed from favorites')
        favorited = False
    else:
        user_profile.favorites.add(laptop)
        messages.success(request, f'{laptop.name} added to favorites')
        favorited = True
    
    # Return JSON for AJAX requests
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        from django.http import JsonResponse
        return JsonResponse({'favorited': favorited})
    
    # Redirect back for regular requests
    return redirect(request.META.get('HTTP_REFERER', 'laptops:laptop_list'))

