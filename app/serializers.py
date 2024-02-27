from .models import User, Test
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from . import models
from jose import jwt

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "role"]

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test 
        fields = "__all__"

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)

    def create(self, validated_date):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, data):
        email = data['email']
        # user = models.User.objects.get(email = email)
        password = data['password']
        # password = user.password
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid login credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)
            # access_token.payload["role"] = user.role
            decoded_payload = jwt.decode(access_token, "vk", algorithms=["HS256"])
            decoded_payload["role"] = user.role
            access_token = jwt.encode(decoded_payload, "vk", algorithm="HS256")
        
            # access_token = str(access_token)
            
            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'email': user.email,
                'password':user.password,
                'role': user.role,
            }

            return validation
        except models.User.DoesNotExist:
            raise serializers.ValidationError("Invalid login credentials")