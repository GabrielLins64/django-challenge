from django.urls import include, path
from api import views

urlpatterns = [
    path('', views.APIRoot.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
]
