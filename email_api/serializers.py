from rest_framework import serializers

class SendEmailSerializer(serializers.Serializer):
    user_email = serializers.CharField(
        max_length=None, min_length=None,
    )
    subject = serializers.CharField(
        max_length=None, min_length=None,
    )
    message = serializers.CharField(
        max_length=None,min_length=None,
    )
