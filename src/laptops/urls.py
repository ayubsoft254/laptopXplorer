from django.urls import path
from . import views

app_name = 'laptops'

urlpatterns = [
    path('', views.laptop_list, name='laptop_list'),
    path('autocomplete/', views.autocomplete_search, name='autocomplete_search'),
    path('laptop/<slug:slug>/', views.laptop_detail, name='laptop_detail'),
    path('brands/', views.brand_list, name='brand_list'),
    path('brand/<slug:slug>/', views.brand_detail, name='brand_detail'),
    path('compare/', views.compare_laptops, name='compare'),
    path('articles/', views.article_list, name='article_list'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
]
