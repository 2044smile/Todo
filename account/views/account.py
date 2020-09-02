from rest_framework import viewsets

from account.models import Account
from account.serializers import AccountSerializer

class AccountModelViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer