from .models import OTP
from rest_framework.views import APIView
from rest_framework.response import Response
import json
import random
from rest_framework import exceptions


class OTPView(APIView):

    def post(self, request):
        body = request.body
        body = json.loads(body)
        phone_number = body['phone_number']
        otp = random.randint(10000,99999)
        OTP.objects.create(
            phone_number = phone_number,
            otp = otp
        )
        return Response(otp)


class LoginView(APIView):

    def post(self, request):
        body = request.body
        body = json.loads(body)
        phone = body['phone_number']
        otp = body['otp']
        try:
            saved_otp = OTP.objects.get(phone_number=phone)
            if saved_otp.otp == otp:
                saved_otp.delete()
                return Response("OK")
            else:
                raise exceptions.AuthenticationFailed()
        except Exception as e:
            print(e)
            return Response("Something is Wrong!")