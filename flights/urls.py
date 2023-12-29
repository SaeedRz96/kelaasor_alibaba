from django.urls import path
from .views import (
    list, list2, test_list, 
    detail,AirportList, CreateAirport,
    AirportView, AirportDelete, 
    AirportRetrieve, AirportUpdate,
    AirportView2, FlightList, TicketCreate,
    TicketList
    )

urlpatterns = [
    path('list', list, name='list'),
    path('test-list', test_list, name='test_list'),
    path('list2', list2, name='list2'),
    path('airport-list', AirportList.as_view(), name='airport-list'),
    path('create-airport', CreateAirport.as_view(), name='create-airport'),
    path('airport', AirportView.as_view(), name='airport'),
    path('airport-delete/<int:pk>', AirportDelete.as_view(), name='airport-delete'),
    path('airport-retrieve/<int:pk>', AirportRetrieve.as_view(), name='airport-retrieve'),
    path('airport-update/<int:pk>', AirportUpdate.as_view(), name='airport-update'),
    path('airport2/<int:pk>', AirportView2.as_view(), name='airport2'),
    path('flight-list', FlightList.as_view(), name='flight-list'),
    path('ticket-create', TicketCreate.as_view(), name='ticket-create'),
    path('ticket-list', TicketList.as_view(), name='ticket-list'),
    path('<str:code>', detail, name='detail'),
]
