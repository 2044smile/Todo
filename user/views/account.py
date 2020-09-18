from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from user.models import Account
from common.permissions import IsOwner
from user.serializers import AccountSerializer


class AccountModelViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAdminUser | IsOwner,)
