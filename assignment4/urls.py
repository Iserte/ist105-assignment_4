from django.urls import path
from calculator.views import calculate_view

urlpatterns = [
    path('', calculate_view, name='calculate'),
]