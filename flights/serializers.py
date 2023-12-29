from .models import Airport, Flight, Ticket
from rest_framework.serializers import ModelSerializer, CharField


class AirportSerializer(ModelSerializer):
    class Meta:
        model = Airport
        fields = ('city',)


class FlightSerializer(ModelSerializer):
    origin = AirportSerializer()
    destination = AirportSerializer()
    class Meta:
        model = Flight
        fields = '__all__'


class TicketSerializer(ModelSerializer):
    reservation_code = CharField(required=False)
    user = CharField(required=False)
    class Meta:
        model = Ticket
        fields = '__all__'