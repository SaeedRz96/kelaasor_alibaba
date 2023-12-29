from django.db import models


class OTP(models.Model):
    phone_number = models.CharField(max_length=20)
    otp = models.CharField(max_length=5)
