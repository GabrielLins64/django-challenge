from django.urls import include, path
from auth import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
]
