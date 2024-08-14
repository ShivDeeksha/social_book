# books/models.py

from django.db import models
from authentication.models import CustomUser

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publish_date = models.DateField()
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=50)
    pages = models.IntegerField()
    published_in = models.CharField(max_length=100)
    series = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=500)  # Store multiple genres as a comma-separated string
    description = models.TextField()
    message_from_author = models.TextField(blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='book_images/')
    book_pdf = models.FileField(upload_to='book_pdfs/')
    visibility = models.CharField(max_length=10, choices=[('public', 'Public'), ('private', 'Private')])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
