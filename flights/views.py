from django.http.response import HttpResponse, JsonResponse
from .models import Flight, Airport, Ticket
from django.shortcuts import render
from datetime import datetime
import random
from .serializers import AirportSerializer, FlightSerializer, TicketSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from user.authentication import JWTAuthentication


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
            'flights' : flights, 
            'flag' : False
        }
        return render(request, 'flights/detail.html', context=f_list)
    if request.method == 'POST':
        current_flight = Flight.objects.get(no=code)
        email=request.POST['email']
        name=request.POST['name']
        lastname=request.POST['lastname']
        nationalid=request.POST['nationalid']
        seat=request.POST['seat']
        # check available seat
        if name == '':
            return HttpResponse('Error: Name should not be empty')
        if int(current_flight.capacity) < int(seat):
            return HttpResponse("Error: There is no enough seat. max seat available is :{}".format(current_flight.capacity))
        Ticket.objects.create(
            flight=current_flight,
            name=name,
            lastname=lastname,
            email = email,
            nationalid=nationalid,
            seat=seat,
            reservation_code=generate_reservation_code()
        )
        current_flight.capacity = current_flight.capacity - int(seat)
        current_flight.save()
        f_list = {
            'flights' : current_flight,
            'flag' : True
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
    
    return JsonResponse(airport_list)


class AirportList(generics.ListAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class CreateAirport(generics.CreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportView(generics.ListCreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportDelete(generics.DestroyAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportRetrieve(generics.RetrieveAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportUpdate(generics.UpdateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class AirportView2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class FlightList(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class TicketCreate(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = [JWTAuthentication,]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = self.perform_create(serializer, request)
        headers = self.get_success_headers(serializer.data)
        return Response("Ticket Reserved with {} reservation code!".format(code), status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer, request):
        code = generate_reservation_code()
        serializer.save(
            reservation_code = code,
            user = request.user
        )
        return code
        

class TicketList(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = [JWTAuthentication,]

    def list(self, request, *args, **kwargs):
        self.queryset = Ticket.objects.filter(user=request.user)
        return super().list(request, *args, **kwargs)

