from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from user.views import AccountModelViewSet

router = DefaultRouter()
router.register(r'user', AccountModelViewSet)

urlpatterns = [
    # Endpoints
    path('', include(router.urls)),

    path('auth/token/', obtain_jwt_token),
    path('auth/token/verify_jwt_token/', verify_jwt_token),
    path('auth/token/refresh/', refresh_jwt_token)
]
