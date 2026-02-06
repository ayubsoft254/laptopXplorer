from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    # Django-allauth URLs
    path('', include('allauth.urls')),
    
    # Custom profile URLs
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('favorites/', views.favorites, name='favorites'),
    path('favorite/<int:laptop_id>/toggle/', views.toggle_favorite, name='toggle_favorite'),
]

