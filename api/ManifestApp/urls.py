from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('',views.index, name="homepage"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/all-nodes/', views.NodeList.as_view(), name="all-nodes"),
]