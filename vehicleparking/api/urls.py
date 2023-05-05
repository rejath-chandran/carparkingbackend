from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('slot/', include('api.slot.urls')),
    path('type/', include('api.category.urls')),
    path('book/', include('api.booking.urls')),
]
