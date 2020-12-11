from rest_framework import seralizers
from .models import Trader, TradeHistory


class TraderSerializer(seralizers.ModelSerializer):
    class Meta:
        model = Trader
        fields = "__all__"


class TradeHistorySerializer(seralizers.ModelSerializer):
    class Meta:
        model = TradeHistory
        fields = "__all__"
