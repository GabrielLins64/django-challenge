from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from vms_backend.generators import CustomOpenAPISchemaGenerator


swagger_schema_view = get_schema_view(
    openapi.Info(
        title="VMS API Documentation",
        default_version='v1.0',
        description="Vulnerability Management System API",
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=CustomOpenAPISchemaGenerator,
)
