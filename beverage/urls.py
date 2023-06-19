from django.urls import path
from . import views

urlpatterns = [
    path('', views.BeverageList.as_view()),
    path('<int:pk>/', views.BeverageDetail.as_view()),
    path('create_beverage/', views.create),
    path('create_recipt/<int:pk>/', views.create_recipt),
    path('update_beverage/<int:pk>/', views.update_beverage),
    path('delete_beverage/<int:pk>/', views.delete_beverage)
]