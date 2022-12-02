from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse


API_DEFAULT_RESPONSE = "VMS API v1.0"


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return HttpResponse(API_DEFAULT_RESPONSE, content_type="text/plain")
