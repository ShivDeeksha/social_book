from rest_framework import serializers
from .models import KindleBook

class KindleBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = KindleBook
        fields = '__all__'

    def validate(self, data):
        # Example of custom validation logic if needed
        if data['price'] < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return data
