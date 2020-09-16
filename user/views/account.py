from rest_framework import viewsets

from user.models import Account
from user.serializers import AccountSerializer

class AccountModelViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
