from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import landing_view, laptops_list, laptop_detail

urlpatterns = [
    path('', landing_view, name='landing_view'),
    path('laptops', laptops_list, name='laptop_list' ),
    path('laptops/<int:laptop_id>/', laptop_detail, name='laptop_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)