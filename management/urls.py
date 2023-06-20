from django.urls import path
from . import views
from .views import Logout, Login

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard),
    path('sale/', views.sale),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('need_login/', views.need_login),
    path('permission_denied/', views.permission_denied),
]
