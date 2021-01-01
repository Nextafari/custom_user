from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from .models import TradeHistory, Trader
from apex_api.models import User
from .serializers import (
    TradeHistorySerializer, TraderProfileSerializer,
    TraderSerializer, RegisterUserSerializer
)


class RegisterUserView(CreateAPIView):
    custom_model = get_user_model()
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if request.method == "POST":
            serializer.is_valid(raise_exception=True)
            user = User.objects.create(
                email=serializer.validated_data.get('email'),
                full_name=serializer.validated_data.get('full_name'),
                investor=serializer.validated_data.get('investor')
            )
            user.set_password(serializer.validated_data.get('password'))
            user.save()
            return Response(
                {
                    "data": "User created"
                },
                status=status.HTTP_201_CREATED
            )


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


class TraderProfileHistoryView(ListAPIView):
    """Lists out a traders alongside their
    individual transaction histories in the same endpoint
    """
    permission_classes = [AllowAny]
    serializer_class = TraderProfileSerializer
    queryset = Trader.objects.all()

    def get(self, request, pk):
        queryset = Trader.objects.filter(pk=pk)
        serializer = TraderProfileSerializer(
            queryset,
            context={"request": request},
            many=True
        )
        return Response(
            serializer.data
        )


class TraderAndHistoryView(ListAPIView):
    """Lists out all the traders alongside their
    individual transaction histories in the same endpoint
    """
    permission_classes = [AllowAny]
    serializer_class = TraderProfileSerializer
    queryset = Trader.objects.all()

    def get(self, request):
        queryset = Trader.objects.all()
        serializer = TraderProfileSerializer(
            queryset,
            context={"request": request},
            many=True
        )
        return Response(
            serializer.data
        )
