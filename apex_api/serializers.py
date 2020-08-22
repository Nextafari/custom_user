from rest_framework import serializers
from .models import User as UserSignUp
from django.contrib.auth import get_user_model  # If used custom user model


UserSignUP = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserSignUp.objects.create(
            email=validated_data['email'],
            full_name=validated_data['full_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserSignUp
        # Tuple of serialized model fields (see link [2])
        fields = [
            'email', 'referral_code', 'full_name', 'password'
        ]

        def validate(self, attrs):
            email = attrs["email"]
            if UserSignUp.objects.filter(email=email).exists():
                raise serializers.ValidationError({
                    'email': 'This email already exits'
                    })
            return super().validate(attrs)
