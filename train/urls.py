from django.urls import path
from .views import train_list

urlpatterns = [
    path('list', train_list, name='train_list')
]