from rest_framework import permissions
from rest_framework.views import APIView
from django.http import HttpResponse
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    authenticate
)


API_DEFAULT_RESPONSE = "VMS API v1.0"


class APIRoot(APIView):
    """
    Root API View. It's usable as API Health check,
    version info and authentication status.
    """
    permission_classes = [permissions.AllowAny]
    swagger_tags = ['Index']

    def get(self, request, format=None):
        response = API_DEFAULT_RESPONSE

        if request.user.is_authenticated:
            response += f"\nYou're logged in as \"{request.user.username}\"!"

        return HttpResponse(response)


class Login(APIView):
    """
    API View for users login. Requires a json body with the
    properties "username" and "password".
    """
    permission_classes = [permissions.AllowAny]
    swagger_tags = ['Auth']

    def post(self, request, format=None):
        body = request.data
        username = body.get('username')
        password = body.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return HttpResponse("Successfully logged in!")

        else:
            return HttpResponse("Invalid credentials", status=401)


class Logout(APIView):
    """
    API View for user logout.
    """
    permission_classes = [permissions.AllowAny]
    swagger_tags = ['Auth']

    def get(self, request):
        if request.user.is_authenticated:
            auth_logout(request)
            return HttpResponse("Successfully logged out!")
        
        else:
            return HttpResponse("You are not logged in.")
