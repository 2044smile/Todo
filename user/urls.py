from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user.views import AccountModelViewSet

router = DefaultRouter()
router.register(r'user', AccountModelViewSet)

urlpatterns = [
    # Endpoints
    path('', include(router.urls)),
]
