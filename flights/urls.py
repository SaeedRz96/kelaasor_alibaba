from django.urls import path
from .views import list, list2, test_list, detail,AirportList

urlpatterns = [
    path('list', list, name='list'),
    path('test-list', test_list, name='test_list'),
    path('list2', list2, name='list2'),
    path('airport-list', AirportList.as_view(), name='airport-list'),
    path('<str:code>', detail, name='detail'),
]
