from rest_framework.views import APIView
from apex_api.models import UserTransaction
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserWalletSerializer, UserAmountSerializer
from drf_yasg.utils import swagger_auto_schema
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from .models import UserAmount
from apex_api.models import UserTransaction
from django.http import JsonResponse


class Deposit(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=UserWalletSerializer,
        operation_description="Deposit",
        responses={201: 'Created'}
    )
    def post(self, request):
        if request.method == "POST":
            serializer = UserWalletSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            deposit = UserTransaction.objects.create(
                user=request.user,
                status="Pending",
                transaction_type="Deposit",
                amount=serializer.validated_data.get("amount"),
                payment_method="BTC",
                amount_in_btc=serializer.validated_data.get("amount_in_btc"),
            )
            deposit.save()
            user = request.user
            amount = serializer.validated_data.get("amount")
            amount_in_btc = serializer.validated_data.get("amount_in_btc")
            send_mail(
                "Deposit Alert",
                f'{user} just created a deposit of ${amount} equivalent to BTC{amount_in_btc} change status from pending to approved',
                settings.EMAIL_HOST_USER,
                ['info@trddex.com']
            )
            return Response(
                {
                    "data": "Done!! Awaiting approval"
                },
                status=status.HTTP_200_OK
            )


class Withdraw(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=UserWalletSerializer,
        operation_description="Withdrawal",
        responses={201: 'Created'}
    )
    def post(self, request):
        if request.method == "POST":
            serializer = UserWalletSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            withdraw = UserTransaction.objects.create(
                user=request.user,
                status="Pending",
                transaction_type="Withdrawal",
                amount=serializer.validated_data.get("amount"),
                payment_method="BTC",
                amount_in_btc=serializer.validated_data.get("amount_in_btc")
            )
            withdraw.save()
            user = request.user
            amount = serializer.validated_data.get("amount")
            amount_in_btc = serializer.validated_data.get("amount_in_btc")
            send_mail(
                "Deposit Alert",
                f'{user} just created a Withdrawal of ${amount} equivalent to BTC{amount_in_btc} change status from pending to approved',
                settings.EMAIL_HOST_USER,
                ['info@trddex.com']
            )
            return Response(
                {
                    "data": "Done!! Awaiting approval"
                },
                status=status.HTTP_200_OK
            )


class UserAmountView(APIView):
    def get(self, request):
        user = self.request.user
        user_amount = UserAmount.objects.filter(user=user).values_list(
            "balance").last()
        # trans_type = UserAmount.objects.filter(user=user).values_list(
        #     "transaction_type").last()
        # return JsonResponse({"data": list(user_amount,)})
        return Response(
            {"data": {
                "user_amount": user_amount}}
        )
