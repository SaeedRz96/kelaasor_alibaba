from django.http.response import HttpResponse, JsonResponse
from .models import Flight, Airport, Ticket
from django.shortcuts import render
from datetime import datetime
import random


def list(request):
    flights = Flight.objects.all()
    f_list = {
        'flights' : flights
    }
    return render(request, 'flights/list.html', context=f_list)


def generate_reservation_code():
    # this is a function to generate random unique reservation code
    random_code = random.randint(10000000,99999999)
    try:
        Ticket.objects.get(reservation_code=random_code)
        generate_reservation_code()
    except:
        return random_code


def detail(request, code):
    if request.method == 'GET':
        try:
            flights = Flight.objects.get(no=code)
        except:
            flights = None
        f_list = {
            'flights' : flights
        }
        return render(request, 'flights/detail.html', context=f_list)
    if request.method == 'POST':
        email=request.POST['email']
        name=request.POST['name']
        lastname=request.POST['lastname']
        nationalid=request.POST['nationalid']
        seat=request.POST['seat']
        Ticket.objects.create(
            flight=Flight.objects.get(no=code),
            name=name,
            lastname=lastname,
            email = email,
            nationalid=nationalid,
            seat=seat,
            reservation_code=generate_reservation_code()
        )
        return HttpResponse('The ticket reserved!')
    


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