from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
    def validate_genre(self, value):
        # Ensure genres are stored as a comma-separated string
        if isinstance(value, list):
            return ','.join(value)
        return value
