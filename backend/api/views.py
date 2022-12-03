from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.http import HttpResponse
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    authenticate
)
from django.contrib.auth.models import User
from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from api.models import Vulnerability
from api.serializers import VulnerabilitySerializer, UserSerializer


API_DEFAULT_RESPONSE = "VMS API v1.0"


class APIRoot(APIView):
    """
    Root API View. It's usable as API Health check,
    version info and authentication status.
    """
    permission_classes = [permissions.AllowAny]
    swagger_tags = ['Index']

    def get(self, request):
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

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ))
    def post(self, request):
        body = request.data
        username = body.get('username')
        password = body.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            db_user = User.objects.get(id=request.user.id)
            serializer = UserSerializer(db_user)
            return Response(serializer.data)

        else:
            return HttpResponse("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)


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


class VulnerabilityList(APIView, PageNumberPagination):
    """
    List all vulnerabilities, or create a new one.
    """
    permissions_classes = [permissions.IsAuthenticated]
    swagger_tags = ['Vulnerability']

    def get(self, request):
        vulnerabilities = Vulnerability.objects.all()
        result = self.paginate_queryset(vulnerabilities, request, view=self)
        serializer_context = {'request': request}
        serializer = VulnerabilitySerializer(
            result,
            many=True,
            context=serializer_context
        )
        return self.get_paginated_response(serializer.data)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'asset_hostname': openapi.Schema(type=openapi.TYPE_STRING),
            'asset_ip_address': openapi.Schema(type=openapi.TYPE_STRING),
            'title': openapi.Schema(type=openapi.TYPE_STRING),
            'severity': openapi.Schema(type=openapi.TYPE_STRING),
            'cvss': openapi.Schema(type=openapi.TYPE_NUMBER),
            'publication_date': openapi.Schema(type=openapi.TYPE_STRING),
        }
    ))
    def post(self, request):
        if not request.user.is_staff:
            return HttpResponse("Higher privileges are required", status=403)

        serializer_context = {'request': request}
        serializer = VulnerabilitySerializer(data=request.data,
                                             context=serializer_context)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VulnerabilityDetail(APIView):
    """
    API View that show details of a Vulnerability, update its
    status or delete it (this one requires admin privileges).
    """
    permissions_classes = [permissions.IsAuthenticated]
    swagger_tags = ['Vulnerability']

    def get_object(self, pk):
        try:
            return Vulnerability.objects.get(pk=pk)
        except Vulnerability.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        vulnerability = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = VulnerabilitySerializer(vulnerability,
                                             context=serializer_context)
        return Response(serializer.data)

    def delete(self, request, pk):
        if not request.user.is_staff:
            return HttpResponse("Higher privileges are required", status=403)

        vulnerability = self.get_object(pk)
        vulnerability.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
