from django.urls import include, path
from api import views

urlpatterns = [
    path('', views.api_root, name='API Health check'),
]
