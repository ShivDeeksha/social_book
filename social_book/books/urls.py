# # books/urls.py
# from django.urls import path
# from .views import shop, book_detail

# urlpatterns = [
#     path('shop/', shop, name='shop'),
#     path('book/<int:book_id>/', book_detail, name='book_detail'),
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookDetailView, UploadBookView

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('upload-book/', UploadBookView.as_view(), name='upload_book'),
]
