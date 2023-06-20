from django.urls import path
from . import views

urlpatterns = [
    path('', views.ViewIngredients.as_view()),
    path('create/', views.CreateIngredient.as_view()),
    path('update/<int:pk>/', views.UpdateIngredient.as_view()),
    path('delete/<int:pk>/', views.DeleteIngredient.as_view()),
    path('order/<int:pk>/', views.order),
]
