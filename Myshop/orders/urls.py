from django.conf.urls import include
from django.contrib import admin
from . import views
from django.urls import path

app_name = 'orders'

urlpatterns = [

    path('basket_adding/', views.basket_adding, name='basket_adding'),
    path('checkout/', views.checkout, name='checkout'),

]

