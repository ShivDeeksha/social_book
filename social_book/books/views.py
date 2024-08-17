# from django.shortcuts import render
# from django.core.paginator import Paginator
# from .models import Book
# from authentication.models import CustomUser

# def shop(request):
#     # Fetch data for all sections
#     book_list = Book.objects.all()
#     authors_list = CustomUser.objects.filter(user_type='author', public_visibility=True)
#     readers_list = CustomUser.objects.filter(user_type='reader', public_visibility=True)
#     sellers_list = CustomUser.objects.filter(user_type='seller', public_visibility=True)

#     # Set up pagination
#     book_paginator = Paginator(book_list, 9)
#     author_paginator = Paginator(authors_list, 6)
#     reader_paginator = Paginator(readers_list, 6)
#     seller_paginator = Paginator(sellers_list, 6)

#     # Get current page numbers from query parameters
#     book_page_number = request.GET.get('book_page')
#     author_page_number = request.GET.get('author_page')
#     reader_page_number = request.GET.get('reader_page')
#     seller_page_number = request.GET.get('seller_page')

#     # Get page objects
#     books_page_obj = book_paginator.get_page(book_page_number)
#     authors_page_obj = author_paginator.get_page(author_page_number)
#     readers_page_obj = reader_paginator.get_page(reader_page_number)
#     sellers_page_obj = seller_paginator.get_page(seller_page_number)

#     context = {
#         'books_page_obj': books_page_obj,
#         'authors_page_obj': authors_page_obj,
#         'readers_page_obj': readers_page_obj,
#         'sellers_page_obj': sellers_page_obj,
#     }
#     return render(request, 'shop.html', context)

# def book_detail(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     recent_books = Book.objects.exclude(id=book_id).order_by('-publish_date')[:3]
#     return render(request, 'book-detail.html', {'book': book, 'recent_books': recent_books})
from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from django.utils.dateparse import parse_date


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

# Fetch a specific book's details
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'pk'  # Set the lookup field to 'book_id'

    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs['pk'])

class UploadBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        
        # Ensure date format is correct
        if 'publish_date' in data:
            publish_date_str = data['publish_date']
            try:
                parsed_date = parse_date(publish_date_str)
                if parsed_date:
                    data['publish_date'] = parsed_date
                else:
                    return Response({'success': False, 'message': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
            except ValueError:
                return Response({'success': False, 'message': 'Invalid date format. Use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        # Add the user to the data
        data['user'] = request.user.id
        
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'redirect_url': '/success/'}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'message': 'Error in form submission', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)