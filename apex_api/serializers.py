from rest_framework import serializers
from .models import User, RecentTransaction
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model  # If used custom user model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = [
            'email', 'full_name', 'password'
        ]

        def validate(self, attrs):
            email = attrs["email"]
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError({
                    'email': 'This email already exits'
                    })
            return super().validate(attrs)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=32)

    def validate(self, validated_data):
        user = authenticate(**validated_data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Email or Password")


class RecentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentTransaction
        fields = [
            "status", "date", "merchant", "transaction_type", "amount", 
            "currency", "tokens", "details"
        ]
