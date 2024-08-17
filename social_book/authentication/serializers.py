from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import CustomUser
from rest_framework import serializers

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = (
            'id', 'username', 'password', 'first_name', 'last_name', 'email', 
            'phone_number', 'address', 'birth_date', 'user_type', 'bio', 
            'public_visibility', 'age'
        )

    def create(self, validated_data):
        user = super().create(validated_data)
        return user

class CustomUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = (
            'id', 'username', 'email', 'phone_number', 'address', 'birth_date', 
            'user_type', 'bio', 'public_visibility', 'age', 'first_name', 'last_name', 'date_joined', 'is_verified'
        )

class ProfileEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'first_name', 'last_name', 'username', 'email', 'phone_number',
            'address', 'birth_date', 'bio', 'public_visibility',
            'age', 'date_joined'
        )

    def validate(self, data):
        # Custom validation logic if needed
        return data