# from django.shortcuts import render
#from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model


class CreateUserView(CreateAPIView):

    custom_model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


# {
#     "referral_code": "foo_b",
#     "full_name": "Foo bar",
#     "email": "f@example.com",
#     "password1": "foob2345",
#     "password2": "foob2345"
# }
