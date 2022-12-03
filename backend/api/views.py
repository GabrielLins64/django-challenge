from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    authenticate
)
from django.http import HttpResponse
import json
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


API_DEFAULT_RESPONSE = "VMS API v1.0"


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    """
    Root API View. It's usable as API Health check,
    version info and authentication status.
    """
    response = API_DEFAULT_RESPONSE

    if request.user.is_authenticated:
        response += "\nYou're logged in!"

    return HttpResponse(response)


@swagger_auto_schema(method='post', request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING),
        'password': openapi.Schema(type=openapi.TYPE_STRING),
    }
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
