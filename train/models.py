from django.db import models


class Station(models.Model):
    name = models.CharField(max_length = 100)
    city = models.CharField(
        max_length=200,
        choices = [
            ("TEH", "Tehran"),
            ("ISF", "Isfahan"),
            ("MSHD", "Mashhad")
        ]
    )
    phone_number = models.CharField(max_length=200)
    address = models.TextField()
    open_time = models.TimeField()
    close_time = models.TimeField()


class Train(models.Model):
    origin = models.ForeignKey(
        Station, 
        on_delete=models.CASCADE,
        related_name = "train_origin"
    )
    destination = models.ForeignKey(
        Station,
        on_delete = models.CASCADE,
        related_name = 'train_destination'
    )
    name = models.CharField(max_length = 100)
    number = models.IntegerField()
    price = models.FloatField()
    date = models.DateField()
    time = models.TimeField()

