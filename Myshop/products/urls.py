from django.conf.urls import include
from products import views
from django.urls import path

app_name = 'products'

urlpatterns = [
    path('product/<int:product_id>/', views.product, name='product'),

]
