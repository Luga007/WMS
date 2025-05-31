from django.urls import path
from .views import (order_view, create_order, delete_order, update_order,
                    orderItem_view, create_orderItem, delete_orderItem, update_orderItem)

urlpatterns = [
    path('view_o/', order_view, name='order'),
    path('create_o/', create_order, name='create_order'),
    path('delete_o/<int:pk>', delete_order, name='delete_order'),
    path('update_o/<int:pk>', update_order, name='update_order'),

    path('view_ort/', orderItem_view, name='orderItem22'),
    path('create_ort/', create_orderItem, name='create_orderItem'),
    path('delete_ort/<int:pk>', delete_orderItem, name='delete_orderItem'),
    path('update_ort/<int:pk>', update_orderItem, name='update_orderItem')
]