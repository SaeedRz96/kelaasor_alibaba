from django.http.response import HttpResponse, JsonResponse
from .models import Flight, Airport

def list(request):
    flights = Flight.objects.all()
    flight_list = []
    for item in flights:
        dictionary = {
            "name" : item.name,
            "origin" : item.origin.name,
            "destination" : item.destination.name,
            "price" : item.price
        }
        flight_list.append(dictionary)
    return JsonResponse(flight_list, safe=False)


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