from django.urls import path
from billmanagement.views import customer_create,order_create

urlpatterns = [
   path('', customer_create, name='customer_create'),
    path('createorder/',order_create, name='order_create'),
]
