from django.http.response import HttpResponse, JsonResponse
from .models import Flight

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
    return HttpResponse(flight_list)