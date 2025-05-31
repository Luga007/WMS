from django.urls import path
from . views import (store, create_store, update_store,
                     delete_store, employees, create_employee, update_employee, delete_employee)

urlpatterns = [
    path('', store, name='store'),
    path('create/', create_store, name='create_store'),
    path('update/<int:pk>', update_store, name='update_store'),
    path('delete/<int:pk>', delete_store, name='delete_store'),

    path('employees/', employees, name='employees'),
    path('create_employee/', create_employee, name='create_employee'),
    path('update_employee/<int:pk>', update_employee, name='update_employee'),
    path('delete_employee/<int:pk>', delete_employee, name='delete_employee')
]