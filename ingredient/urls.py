from django.urls import path
from . import views

urlpatterns = [
    path('stock/', views.ingredient),
    path('', views.home),
]