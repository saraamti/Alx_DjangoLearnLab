from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):  # Explicitly using ListAPIView
    """
    API view to retrieve a list of books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer



