from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library  # Ensure this line is included

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Ensure the template path is correct

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Ensure the template path is correct
    context_object_name = 'library'

