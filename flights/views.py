from django.http.response import HttpResponse, JsonResponse
from .models import Flight, Airport
from django.shortcuts import render


def list(request):
    flights = Flight.objects.all()
    f_list = {
        'flights' : flights
    }
    return render(request, 'flights/list.html', context=f_list)


def list2(request):
    airports = Airport.objects.all()
    airport_list = []
    for item in airports:
        airport_dict = {
            "name" : item.name,
            "no" : item.no,
            "city" : item.city
        }
        airport_list.append(airport_dict)
    
    return HttpResponse(airport_list)