from .models import Airport
from rest_framework.serializers import ModelSerializer


class AirportSerializer(ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'