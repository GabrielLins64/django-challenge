from django.urls import include, path
from api import views

urlpatterns = [
    path('', views.api_root, name='API Health check'),
    path('login/', views.login),
    path('logout/', views.logout),
]
