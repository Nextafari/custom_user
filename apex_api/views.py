from django.shortcuts import render
#from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from knox.views import LoginView as knox_login_view
from django.contrib.auth import login, logout
from .models import RecentTransaction
from .serializers import (
    UserSerializer, UserLoginSerializer, RecentTransactionSerializer
)
from rest_framework.authentication import TokenAuthentication
from rest_framework import status


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
    authentication_classes = [TokenAuthentication]
    
    def post(self, request):
        logout(request)
        return Response(
            {'message': "Logout successful"}, status=status.HTTP_204_NO_CONTENT
        )



def template_view(request):
    return render(request, 'dashboard.html', {})


# {
#     "referral_code": "foo_b",
#     "full_name": "Foo bar",
#     "email": "f@example.com",
#     "password1": "foob2345",
#     "password2": "foob2345"
# }
