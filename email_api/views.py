from django.conf import settings
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SendEmailSerializer
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema


class SendEmailAPI(APIView):
    """Sends a user an email when it is triggered"""
    permission_classes = [AllowAny]
    
    @swagger_auto_schema(
        request_body=SendEmailSerializer,
        operation_description="Send Email",
        responses={200: 'Sent!'}
    )
    def post(self, request):
        serializer = SendEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        send_mail(
            serializer.validated_data.get("subject"),
            f"{serializer.validated_data.get('message')} \n \n This email was sent by {serializer.validated_data.get('user_email')}",
            settings.EMAIL_HOST_USER,
            ["1zero.0one@protonmail.com"]
        )
        return Response("Email Delivered", status=status.HTTP_200_OK)
