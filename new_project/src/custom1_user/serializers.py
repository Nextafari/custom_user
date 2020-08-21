from rest_framework import serializers
from .models import UserSignUp


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8, write_only=True
    )

    class Meta:
        model = UserSignUp
        fields = [
            "referral_code", "full_name", "email", "password"
        ]

    def validate(self, attrs):
        email = attrs["email"]
        if UserSignUp.objects.filter(email=email).exists():
            raise serializers.ValidationError({
                'email': 'This email already exits'
                })
        return super().validate(attrs)

    def create(self, validated_data):
        return UserSignUp.objects.create_user(**validated_data)
