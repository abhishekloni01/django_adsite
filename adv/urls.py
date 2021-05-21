from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    # path('login/', views.login, name="login"),
    # path('register/', views.register, name="register"),
    path('electronics', views.electronics, name="electronics"),
    # path('demo', views.demo, name="demo"),
    path('contact', views.contact, name="contact"),
    
]