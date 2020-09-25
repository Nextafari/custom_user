from rest_framework import serializers
from apex_api.models import UserTransaction


class UserWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTransaction
        fields = [
            "amount", "amount_in_btc"
        ]


class UserAmount(serializers.ModelSerializer):
    class Meta:
        model = UserTransaction
        fields = [
            "amount"
        ]