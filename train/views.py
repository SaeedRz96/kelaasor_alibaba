from django.http.response import JsonResponse
from .models import Train

def train_list(request):
    trains = Train.objects.all()
    train_lis = []
    for item in trains:
        dict = {
            'origin' : item.origin.city,
            'destination' : item.destination.city,
            'price' : item.price,
            'date' : item.date,
            'time' : item.time
        }
        train_lis.append(dict)
    
    return JsonResponse(train_lis, safe=False)