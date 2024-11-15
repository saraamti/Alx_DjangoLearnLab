from django import forms
from .models import Book

class Meta:
    model = Book
    fields = '__all__'