from django.urls import path 
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("edit/<str:pk>/", views.edit, name="edit"),
    path("delete/<str:pk>/", views.delete, name='delete'),
    

    path("register/", views.register, name="register"),
    path("loginpage", views.loginView, name="login_view"),
    path('logout/', views.logoutView, name='logout'),
    
]