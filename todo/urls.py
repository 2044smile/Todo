from django.urls import path

from todo.views import *


urlpatterns = [
    # Endpoints
    path('status_check/', status_check, name='status_check'),
    path('todo/craete/')
]
