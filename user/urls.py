from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from user.views import AccountModelViewSet

router = DefaultRouter()
router.register(r'user', AccountModelViewSet)

urlpatterns = [
    # Endpoints
    path('', include(router.urls)),

    path('', include('rest_auth.urls')),
    path('obtain_token/', obtain_jwt_token, name='obtain-jwt'),
    path('refresh_token/', refresh_jwt_token, name='refresh-jwt'),

    path('registration/', include('rest_auth.registration.urls')),
]
