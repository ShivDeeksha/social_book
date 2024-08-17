from rest_framework.permissions import AllowAny
from rest_framework import generics
from .models import KindleBook
from .serializers import KindleBookSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class KindleBookListView(generics.ListAPIView):
    queryset = KindleBook.objects.all()
    serializer_class = KindleBookSerializer
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]

class KindleBookDetailView(generics.RetrieveAPIView):
    queryset = KindleBook.objects.all()
    serializer_class = KindleBookSerializer
    permission_classes = [AllowAny]  # Allows access without authentication
