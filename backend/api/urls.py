from django.urls import include, path
from api import views

# router = routers.DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.api_root),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]
