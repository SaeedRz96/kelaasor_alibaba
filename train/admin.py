from django.contrib.admin import register, ModelAdmin
from .models import Station, Train


@register(Station)
class StationAdmin(ModelAdmin):
    pass


@register(Train)
class TrainAdmin(ModelAdmin):
    pass
