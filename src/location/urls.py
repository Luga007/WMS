from django.urls import path
from .views import location_view, create_location, delete_location, update_location
urlpatterns = [
    path('view_l/', location_view, name='location_v'),
    path('create_location/', create_location, name='create_location'),
    path('delete_location/<int:pk>', delete_location, name='delete_location'),
    path('update_location/<int:pk>', update_location, name='update_location'),
]