from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser
from rest_framework import serializers

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'phone_number', 'address', 'birth_date', 'user_type', 'bio')

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'username', 'email', 'phone_number', 'address', 'birth_date', 'user_type', 'bio')

class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('phone_number', 'address', 'birth_date', 'user_type', 'bio')
