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
