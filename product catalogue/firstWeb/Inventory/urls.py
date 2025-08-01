from django.urls import path
from Inventory.views import home_inventory , edit , delete

urlpatterns = [
    path('', home_inventory, name='home_inventory'),
    path('/edit<int:id>',edit , name='edit' ),
    path('/delete<int:id>',delete , name='delete' ),
]
