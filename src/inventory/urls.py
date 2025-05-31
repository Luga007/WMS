from django.urls import path
from .views import inventory_view, delete_inventory, create_inventory, update_inventory
urlpatterns = [
    path('view_i/', inventory_view, name='inventory_i'),

    path('delete_inventory/<int:pk>', delete_inventory, name='delete_inventory'),
    path('create_inventory/', create_inventory, name='create_inventory'),
    path('update_inventory/<int:pk>', update_inventory, name='update_inventory'),

]