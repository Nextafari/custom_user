# from django.contrib.auth import authenticate
# from django.shortcuts import render
from django.contrib.auth import get_user_model, login
from knox.views import LoginView as knox_login_view
from rest_framework import permissions, status
# from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import (
    RecentTransaction, User, UserTransaction
)
from .serializers import (
    RecentTransactionSerializer, UserLoginSerializer,
    UserSerializer, UserTranactionSerializer, ProfileSerializer
)
from drf_yasg.utils import swagger_auto_schema


class CreateUserView(CreateAPIView):
    custom_model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if request.method == "POST":
            serializer.is_valid(raise_exception=True)
            user = User.objects.create(
                email=serializer.validated_data.get('email'),
                full_name=serializer.validated_data.get('full_name'),
            )
            user.set_password(serializer.validated_data.get('password'))
            user.save()
            return Response(
                {
                    "data": "User created"
                },
                status=status.HTTP_201_CREATED
            )


class UserLogin(knox_login_view):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(
        request_body=UserLoginSerializer,
        operation_description="Logs user in.",
        responses={200: 'login_response'}
    )
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


# class LogoutView(APIView):
#     """Custom logout view"""
#     authentication_classes = [TokenAuthentication]

#     def post(self, request):
#         print("this is my story 1")
#         try:
#             request.user.auth_token.delete()
#         except (AttributeError, ObjectDoesNotExist):
#             pass
#         print("this is my story 2")
#         logout(request)
#         print("this is my story 3")
#         return Response(
#             {'message': "Logout successful"},
#             status=status.HTTP_204_NO_CONTENT
#         )


class UserTransactionView(APIView):
    """Retrieves User's personal Transaction"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user
        transactions = UserTransaction.objects.filter(user=user)
        serializer = UserTranactionSerializer(transactions, many=True)
        return Response(serializer.data)


# class UserDetail(RetrieveUpdateDestroyAPIView):
#     """Retrieve's user"""
#     permission_classes = [IsAuthenticated]
#     serializer_class = UserSerializer
#     lookup_field = 'id'

#     def get_queryset(self):
#         user = self.request.user
#         return User.objects.filter(full_name=user)


class UserProfile(APIView):
    """Retrieves user profile"""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        full_name = self.request.user.full_name
        email = self.request.user.email
        image = self.request.user.profile.image.url
        trading_code = self.request.user.profile.trading_code
        return Response(
            {"data":
                {
                    "full_name": full_name,
                    "email": email,
                    "image": image,
                    "trading_code": trading_code
                }},
            status=status.HTTP_200_OK
        )


class EditUserProfile(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(full_name=user)


class UserId(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        user_id = self.request.user.id
        return Response(user_id)


class UserAccountLinkage(generics.ListAPIView):
    """
    A boolean field that is used to link a user's account to an
    external account
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = self.request.user

        if user.is_authenticated:
            get_account_linkage = User.objects.filter(
                pk=user.id).values_list(
                    "account_linked"
                )
            return Response(get_account_linkage)
