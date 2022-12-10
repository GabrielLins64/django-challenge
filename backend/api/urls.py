from django.urls import include, path
from api import views

urlpatterns = [
    path('', views.APIRoot.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('vulnerabilities/', views.VulnerabilityList.as_view()),
    path('vulnerabilities/csv', views.UploadVulnerabilitiesCSV.as_view()),
    path('vulnerability/<int:pk>', views.VulnerabilityDetail.as_view()),
    path('request_log/', views.RequestAuditList.as_view()),
]
