from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todo.views import *
from account.views import *


router = DefaultRouter()
router.register(r'todo', TodoModelViewSet)
router.register(r'account', AccountModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('status_check/', status_check, name='status_check'),
    path('api/', include(router.urls)),
]
