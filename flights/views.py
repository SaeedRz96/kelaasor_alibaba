from django.http.response import HttpResponse, JsonResponse
from .models import Flight, Airport
from django.shortcuts import render
from datetime import datetime


def list(request):
    flights = Flight.objects.all()
    f_list = {
        'flights' : flights
    }
    return render(request, 'flights/list.html', context=f_list)


def detail(request, code):
    try:
        flights = Flight.objects.get(no=code)
    except:
        flights = None
    f_list = {
        'flights' : flights
    }
    return render(request, 'flights/detail.html', context=f_list)


def test_list(request):
    # flights = Flight.objects.filter(origin__city='tehran', destination__city='mashhad')
    # flights = Flight.objects.filter(price__gte=450000)
    # flights = Flight.objects.all().order_by('-price')
    # flights = Flight.objects.all().order_by('time')
    today = datetime.today().date()
    # flights = Flight.objects.filter(time__date=today)
    flights = Flight.objects.filter(origin__city='tehran', destination__city='mashhad', time__date=today, price__lte=450000).order_by('time')
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