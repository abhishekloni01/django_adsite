from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('login',views.loginUser, name="loginUser"),
    path('register',views.register, name="register"),
    path('logout',views.logoutUser, name="logoutUser"),
    
    
    
]
