from django.urls import path
from . import views

urlpatterns = [
    path('', views.ingredient),
    path('<int:pk>/', views.stock),
]