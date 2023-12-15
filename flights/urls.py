from django.urls import path
from .views import list, list2

urlpatterns = [
    path('list', list, name='list'),
    path('list2', list2, name='list2')
]
