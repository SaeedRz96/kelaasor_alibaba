from django.contrib.admin import ModelAdmin, register
from .models import Flight, Airport, Ticket


@register(Flight)
class FlightAdmin(ModelAdmin):
    autocomplete_fields = ['origin','destination']
    list_display = ['name', 'origin', 'destination', 'time']


@register(Airport)
class AirportAdmin(ModelAdmin):
    list_display = ["name","no","city","phone_number"]
    search_fields = ["name",]
    list_filter = ['name','city']


@register(Ticket)
class TicketAdmin(ModelAdmin):
    list_display = ['name', 'lastname', 'reservation_code']