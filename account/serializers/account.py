from rest_framework import serializers

from account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email', 'password', 'nickname', 'date_joined']  # TODO(Account): Password -> HiddenSerializer
