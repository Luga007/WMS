from django.urls import path
from .views import (supplier_view, create_supplier, update_supplier, delete_supplier,
                    product_view, create_product, delete_product, update_product)
urlpatterns = [
    path('view_s/', supplier_view, name='supplier'),
    path('create_s/', create_supplier, name='create'),
    path('update_s/<int:pk>', update_supplier, name='update'),
    path('delete_s/<int:pk>', delete_supplier, name='delete'),

    path('view_p/', product_view, name='product'),
    path('create_p/', create_product, name='create_p'),
    path('update_p/<int:pk>', update_product, name='update_p'),
    path('delete_p/<int:pk>', delete_product, name='delete_p'),
]