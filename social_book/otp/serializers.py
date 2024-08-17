from rest_framework import serializers

class OTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
