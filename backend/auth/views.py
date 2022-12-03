from django.http import HttpResponse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    authenticate
)
import json
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING),
    },
    tags=['auth']
))
@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def login(request):
    """
    API View for users login. Requires a json body with the
    properties "username" and "password".
    """
    body = request.data
    username = body.get('username')
    password = body.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return HttpResponse("Successfully logged in!")

    else:
        return HttpResponse("Invalid credentials", status=401)


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def logout(request):
    """
    API View for users logout.
    """
    if request.user.is_authenticated:
        auth_logout(request)
        return HttpResponse("Successfully logged out!")
    
    else:
        return HttpResponse("You are not logged in.")
