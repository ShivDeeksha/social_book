# books/urls.py
from django.urls import path
from .views import shop, book_detail

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('book/<int:book_id>/', book_detail, name='book_detail'),
]
