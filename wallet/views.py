from django.shortcuts import render
from rest_framework.views import APIView
from apex_api.models import UserTransaction
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserWalletSerializer
from drf_yasg.utils import swagger_auto_schema
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

"""
Find a way to connect the wallet to the User Transaction table database

This is more like going to be creating a transaction for the user and sending a notification to admin
to update recent transactions, this will have permission classes enabled
"""
class Deposit(APIView):
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
                amount_in_btc=serializer.validated_data.get("amount_in_btc")
            )
            deposit.save()
            user = request.user
            amount = serializer.validated_data.get("amount")
            amount_in_btc = serializer.validated_data.get("amount_in_btc")
            send_mail(
                "Deposit Alert",
                f'{user} just created a deposit of ${amount} equivalent to BTC{amount_in_btc} change status from pending to approved',
                settings.EMAIL_HOST_USER,
                ['chinedue16@gmail.com']
            )
            return Response(
                {
                    'data': "Done!! Awaiting approval"
                }
            )
