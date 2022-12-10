from rest_framework import permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser
from django.http import HttpResponse
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
    authenticate
)
from django.contrib.auth.models import User
from django.core.exceptions import FieldError
from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from api.models import Vulnerability, RequestAudit
from api.serializers import (
    VulnerabilitySerializer,
    VulnerabilityStatusSerializer,
    UserSerializer,
    FileUploadSerializer,
    VulnerabilityCSVSerializer,
    RequestAuditSerializer,
)
from api.filters import VulnerabilitySearchFilter


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
            token, _ = Token.objects.get_or_create(user=db_user)
            return Response({
                'user': serializer.data,
                'token': token.key,
            })

        else:
            return HttpResponse("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)


class Logout(APIView):
    """
    API View for user logout.
    """
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    swagger_tags = ['Auth']

    def get(self, request):
        request.user.auth_token.delete()
        auth_logout(request)
        return HttpResponse("Successfully logged out!")


class VulnerabilityList(APIView, PageNumberPagination):
    """
    API View for listing all vulnerabilities or
    adding a brand new one.
    """
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    swagger_tags = ['Vulnerability']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            'page',
            in_=openapi.IN_QUERY,
            description="(Optional) Pagination control",
            type=openapi.TYPE_INTEGER
        ),
        openapi.Parameter(
            'asset_hostname',
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="(Optional) Query filter parameter"
        ),
        openapi.Parameter(
            'title',
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="(Optional) Query filter parameter"
        ),
        openapi.Parameter(
            'severity',
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="(Optional) Query filter parameter"
        ),
        openapi.Parameter(
            'asset_ip_address',
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="(Optional) Query filter parameter"
        ),
        openapi.Parameter(
            'publication_date',
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="(Optional) Query filter parameter"
        ),
        openapi.Parameter(
            'fixed',
            openapi.IN_QUERY,
            type=openapi.TYPE_BOOLEAN,
            description="(Optional) Query filter parameter"
        ),
        openapi.Parameter(
            'order_by',
            openapi.IN_QUERY,
            type=openapi.TYPE_STRING,
            description="(Optional) Order by column. Example: ?order_by=id,desc"
        ),
    ])
    def get(self, request):
        """
        List all vulnerabilities.
        """
        vulnerabilities = VulnerabilitySearchFilter.find(request.query_params)

        try:
            result = self.paginate_queryset(vulnerabilities, request, view=self)
        except FieldError as err:
            return Response(err.__str__(),
                            status=status.HTTP_400_BAD_REQUEST)

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
        """
        Create a new vulnerability.
        """
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
    API View that handles a specific Vulnerability.
    """
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    swagger_tags = ['Vulnerability']

    def get_object(self, pk):
        try:
            return Vulnerability.objects.get(pk=pk)
        except Vulnerability.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Fetch details of a vulnerability.
        """
        vulnerability = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = VulnerabilitySerializer(vulnerability,
                                             context=serializer_context)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'fixed': openapi.Schema(type=openapi.TYPE_BOOLEAN),
        }
    ))
    def patch(self, request, pk):
        """
        Update vulnerability's status (fixed or not).
        """
        vulnerability = self.get_object(pk)
        serializer_context = {'request': request}
        serializer = VulnerabilityStatusSerializer(vulnerability,
                                                   data=request.data,
                                                   context=serializer_context,
                                                   partial=True)
        if serializer.is_valid():
            serializer.save()
            full_serializer = VulnerabilitySerializer(vulnerability)
            return Response(full_serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a vulnerability.
        """
        if not request.user.is_staff:
            return HttpResponse("Higher privileges are required", status=403)

        vulnerability = self.get_object(pk)
        vulnerability.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UploadVulnerabilitiesCSV(APIView):
    """
    API View that handles Vulnerabilities inserted through
    a CSV file upload.
    """
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    swagger_tags = ['Vulnerability']
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(manual_parameters=[openapi.Parameter(
        name="file",
        in_=openapi.IN_FORM,
        type=openapi.TYPE_FILE,
        required=True,
    )])
    @action(detail=False, methods=['post'], parser_classes=(MultiPartParser,))
    def post(self, request):
        """
        POST a CSV file with vulnerabilities.
        """
        if not request.user.is_staff:
            return HttpResponse("Higher privileges are required", status=403)

        serializer_context = {'request': request}
        file_serializer = FileUploadSerializer(data=request.data,
                                          context=serializer_context)
        file_serializer.is_valid(raise_exception=True)

        file = file_serializer.validated_data['file']
        vulnerability_serializer = VulnerabilityCSVSerializer(file,
                                                              context=serializer_context)

        if vulnerability_serializer.is_valid():
            vulnerability_serializer.save()
            return Response("File successfully imported", status=status.HTTP_201_CREATED)

        return Response(vulnerability_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestAuditList(APIView, PageNumberPagination):
    """
    API View for listing the request audit log.
    """
    permissions_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    swagger_tags = ['Audit Log']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter(
            'page',
            in_=openapi.IN_QUERY,
            description="Pagination control",
            type=openapi.TYPE_INTEGER
        )
    ])
    def get(self, request):
        """
        List the request audit log.
        """
        if not request.user.is_staff:
            return HttpResponse("Higher privileges are required", status=403)

        requests = RequestAudit.objects.all()
        result = self.paginate_queryset(requests, request, view=self)
        serializer_context = {'request': request}
        serializer = RequestAuditSerializer(
            result,
            many=True,
            context=serializer_context
        )
        return self.get_paginated_response(serializer.data)
