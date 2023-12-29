from django.db import models
from django.contrib.auth.models import User


class Airport(models.Model):
    name = models.CharField(max_length=400)
    no = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=11)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Kelaasor Airport"


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination_airport')
    name = models.CharField(max_length=255)
    no = models.CharField(unique=True,max_length=10, verbose_name="Code")
    time = models.DateTimeField()
    capacity = models.IntegerField()
    price = models.FloatField(help_text="Price in Rial")

    def __str__(self) -> str:
        return "{} - {}".format(self.name,self.no)

    class Meta:
        verbose_name = "Kelaasor Flight"


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    flight = models.ForeignKey(Flight, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    nationalid = models.CharField(max_length=10)
    seat = models.PositiveIntegerField()
    reservation_code = models.CharField(max_length=8, unique=True)

    def __str__(self) -> str:
        return '{} {}'.format(self.name, self.lastname)