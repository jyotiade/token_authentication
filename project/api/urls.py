from django.urls import path,include
from rest_framework import routers 
from .views import MovieViewSet
from rest_framework.authtoken import views 
# define the router
router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet, basename='movie')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
    # path('api-auth/', include('rest_framework.urls')) 
]