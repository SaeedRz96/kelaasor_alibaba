import jwt, datetime
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import exceptions


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)
            try:
                current_user = User.objects.get(pk=id)
                return (current_user, None)
            except:
                raise exceptions.AuthenticationFailed('unauthenticated')
        else:
            raise exceptions.AuthenticationFailed('unauthenticated')


def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')
        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')
    

def create_access_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow()
    }, 'access_secret', algorithm='HS256')

def create_refresh_token(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=3),
        'iat': datetime.datetime.utcnow()
    }, 'refresh_secret', algorithm='HS256')


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256')

        return payload['user_id']
    except:
        raise exceptions.AuthenticationFailed('unauthenticated')