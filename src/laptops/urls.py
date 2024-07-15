from django.urls import path
from laptops.views import landing_view

urlpatterns = [
    path('', landing_view, name=landing_view),
]