from django.urls import path
from .views import KindleBookListView, KindleBookDetailView

urlpatterns = [
    path('books/', KindleBookListView.as_view(), name='kindle-book-list'),
    path('books/<int:pk>/', KindleBookDetailView.as_view(), name='kindle-book-detail'),
]
