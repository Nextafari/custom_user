from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import UserSignUp


class UserRegisterSerializer(RegisterSerializer):

    email = serializers.EmailField(max_length=250, required=True)
    referral_code = serializers.CharField(max_length=30, required=False)
    full_name = serializers.CharField(max_length=50, required=True)
    password1 = serializers.CharField(write_only=True, required=True)

    def get_cleaned_data(self):
        super(UserRegisterSerializer, self).get_cleaned_data()

        return {
            'password1': self.validated_data.get('password1'),
            'email': self.validated_data.get('email'),
            'referral_code': self.validated_data.get('referral_code'),
            'full_name': self.validated_data.get('full_name'),
        }


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignUp
        fields = [
            'email', 'referral_code', 'full_name', 'last_name'
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




# from rest_framework import serializers
# from .models import UserSignUp
# class UserRegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         min_length=8, write_only=True
#     )

#     class Meta:
#         model = UserSignUp
#         fields = [
#             "referral_code", "full_name", "email", "password"
#         ]

#     def validate(self, attrs):
#         email = attrs["email"]
#         if UserSignUp.objects.filter(email=email).exists():
#             raise serializers.ValidationError({
#                 'email': 'This email already exits'
#                 })
#         return super().validate(attrs)

#     def create(self, validated_data):
#         return UserSignUp.objects.create_user(**validated_data)
