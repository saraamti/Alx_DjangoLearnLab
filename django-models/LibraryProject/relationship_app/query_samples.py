import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def query_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by {author_name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with name {author_name}")

# 2. List all books in a library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()  # Access the ManyToManyField relationship
        print(f"Books in {library_name} library:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")

# 3. Retrieve the librarian for a library
def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian  # Access the OneToOneField relationship
        print(f"Librarian for {library_name} library: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with name {library_name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for the {library_name} library")

# Run sample queries
query_books_by_author("George Orwell")
list_books_in_library("Central Library")
retrieve_librarian_for_library("Central Library")
