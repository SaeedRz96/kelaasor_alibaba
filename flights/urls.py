from django.urls import path
from .views import list, list2, test_list, detail

urlpatterns = [
    path('list', list, name='list'),
    path('<str:code>', detail, name='detail'),
    path('test-list', test_list, name='test_list'),
    path('list2', list2, name='list2')
]
