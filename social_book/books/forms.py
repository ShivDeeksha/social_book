from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'author', 'publish_date', 'publisher', 'language',
            'pages', 'published_in', 'series', 'genre', 'description',
            'message_from_author', 'cost', 'image', 'book_pdf', 'visibility'
        ]
        widgets = {
            'publish_date': forms.DateInput(attrs={'class': 'form-control date-picker', 'placeholder': 'Select Date', 'type': 'text'}),
            'genre': forms.SelectMultiple(attrs={'class': 'selectpicker form-control', 'data-style': 'btn-outline-primary'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}),
            'message_from_author': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'cost': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'book_pdf': forms.FileInput(attrs={'class': 'form-control'}),
            'visibility': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_genre(self):
        genres = self.cleaned_data.get('genre')
        if genres:
            # Ensure it's a list and return as a comma-separated string
            return ', '.join(genres) if isinstance(genres, list) else genres
        return ''

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Split the genre field from the instance into a list for the form
            self.initial['genre'] = self.instance.genre.split(', ')
