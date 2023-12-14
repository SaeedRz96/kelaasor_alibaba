from django.contrib.admin import ModelAdmin, register
from .models import Flight, Airport


@register(Flight)
class FlightAdmin(ModelAdmin):
    pass


@register(Airport)
class AirportAdmin(ModelAdmin):
    pass