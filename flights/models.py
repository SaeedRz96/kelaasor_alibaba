from django.db import models


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
    name = models.CharField(max_length=255)
    no = models.CharField(max_length=10, verbose_name="Code")
    capacity = models.IntegerField()
    price = models.FloatField(help_text="Price in Rial")

    def __str__(self) -> str:
        return "{} - {}".format(self.name,self.no)

    class Meta:
        verbose_name = "Kelaasor Flight"