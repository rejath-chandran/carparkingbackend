from django.urls import path

from .views import *

urlpatterns = [
    path('pay/', start_payment, name="payment"),
    path('success/', handle_payment_success, name="payment_success"),
    path('add/', add_bookin, name="add_bookin")
]