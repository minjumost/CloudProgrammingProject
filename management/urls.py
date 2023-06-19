from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('staff/', views.staff),
    path('sale/', views.sale),
]
