from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.views import AccountModelViewSet

router = DefaultRouter()
router.register(r'account', AccountModelViewSet)

urlpatterns = [
    # Endpoints
    path('', include(router.urls)),
]
