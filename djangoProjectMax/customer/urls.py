from django.urls import path
from .views import customer, customer_general

urlpatterns = [
    path('', customer_general),
    path('<int:customer_number>/', customer),
]