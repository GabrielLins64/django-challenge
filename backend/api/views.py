from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django.http import HttpResponse


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
        response += f"\nYou're logged in as \"{request.user.username}\"!"

    return HttpResponse(response)


