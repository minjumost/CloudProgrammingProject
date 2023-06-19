from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('stock/', views.ViewIngredients.as_view()),
    path('stock/create/', views.CreateIngredient.as_view()),
    path('stock/update/<int:pk>/', views.UpdateIngredient.as_view()),
    path('stock/delete/<int:pk>/', views.DeleteIngredient.as_view()),
]
