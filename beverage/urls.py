from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu),
    path('<str:beverage_name>/', views.recipt),
]