from rest_framework.views import APIView
from .serializers import TraderSerializer, TradeHistorySerializer
from .models import TradeHistory, Trader
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


class TraderView(APIView):
    """Lists out all the traders in the DB"""
    permission_classes = [AllowAny]
    serializer_class = TraderSerializer

    def get(self, request):
        trader = Trader.objects.all()
        serializer = TraderSerializer(trader, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )


class TradeHistoryView(APIView):
    """Lists out all trading histories of a particular trader"""
    permission_classes = [AllowAny]
    serializer_class = TradeHistorySerializer

    def get(self, request):
        trader_history = TradeHistory.objects.all()
        serializer = TradeHistorySerializer(trader_history, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
