from django.conf.urls import include
from django.contrib import admin
from landing import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('landing/', views.landing, name='landing'),
]