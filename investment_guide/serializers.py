from rest_framework import serializers
from .models import Trader, TradeHistory


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
            "name", "commission_type", "commission_fixed_per_lot",
            "commission_revshare", "avatar", "experience", "account_created",
            "country", "country_code", "gain", "profit", "loss",
            "copiers_count", "copiers_delta", "time_with_us_days",
            "is_subscribed", "equity", "strategy_description", "tradehistory_set"
        ]
