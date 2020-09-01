from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo.views import *
from account.views import *


router = DefaultRouter()  # viewset 은 router 를 사용하여 URL 을 관리할 수 있습니다.
router.register(r'todo', TodoModelViewSet)
router.register(r'account', AccountModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('status_check/', status_check, name='status_check'),
    path('api/', include(router.urls)),
]
