from django.contrib import admin
from django.urls import path, include
from vms_backend.views import swagger_schema_view

urlpatterns = [
    path('api/', include('api.urls')),
    path('auth/', include('auth.urls')),
    path('docs/', swagger_schema_view.with_ui('swagger'), name='schema-swagger-ui'),
]
