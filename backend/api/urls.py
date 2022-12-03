from django.urls import include, path
from api import views

urlpatterns = [
    path('', views.APIRoot.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
]
