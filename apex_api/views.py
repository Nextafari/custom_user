# from django.contrib.auth import authenticate
# from django.shortcuts import render
import json
from django.contrib.auth import get_user_model, login, logout
from django.core.serializers import serialize
from knox.views import LoginView as knox_login_view
from rest_framework import permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RecentTransaction, User, UserTransaction
from .serializers import (RecentTransactionSerializer, UserLoginSerializer,
                          UserSerializer, UserTranactionSerializer)


class CreateUserView(CreateAPIView):
    custom_model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


class UserLogin(knox_login_view):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        return super(UserLogin, self).post(request, format=None)


class RecentTransactions(APIView):
    def get(self, request):
        transactions = RecentTransaction.objects.all()
        serializer = RecentTransactionSerializer(transactions, many=True)
        return Response(serializer.data)


class LogoutView(APIView):
    """Custom logout view"""
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        logout(request)
        return Response(
            {'message': "Logout successful"},
            status=status.HTTP_204_NO_CONTENT
        )


class UserTransactionView(APIView):
    """Retrieves User's personal Transaction"""
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        transactions = UserTransaction.objects.filter(pk=pk)
        serializer = UserTranactionSerializer(transactions, many=True)
        return Response(serializer.data)


class UserDetail(RetrieveUpdateDestroyAPIView):
    """Retrieve's user"""
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(full_name=user)


# {
#     "referral_code": "foo_b",
#     "full_name": "Foo bar",
#     "email": "f@example.com",
#     "password1": "foob2345",
#     "password2": "foob2345"
# }
