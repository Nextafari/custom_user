from rest_framework import serializers
from .models import Trader, TradeHistory
from apex_api.models import User


class TraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trader
        fields = "__all__"


class TradeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeHistory
        fields = "__all__"


class TraderProfileSerializer(serializers.ModelSerializer):
    tradehistory_set = TradeHistorySerializer(many=True)

    class Meta:
        model = Trader
        fields = [
            "name", "socials", "commission_type", "commission_fixed_per_lot",
            "commission_revshare", "avatar", "experience", "account_created",
            "country", "country_code", "gain", "profit", "loss",
            "minimum_value", "floating_profit", "balance",
            "master_traders_bonus", "leverage", "copiers_count",
            "copiers_delta", "time_with_us_days", "is_subscribed", "equity",
            "about", "strategy_description", "tradehistory_set"
        ]


class RegisterUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'email', 'full_name', 'investor', 'password'
        ]

        def validate(self, attrs):
            email = attrs["email"]
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({
                    'email': 'This email already exits'
                    })
            return super().validate(attrs)
