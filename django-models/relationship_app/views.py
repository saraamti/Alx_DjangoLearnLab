from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library  # Ensure this line includes Library as well as Book
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from .models import UserProfile


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # View for Admin role
@user_passes_test(lambda u: u.userprofile.role == 'Admin')
def admin_view(request):
    return HttpResponse("Welcome to the Admin page!")

# View for Librarian role
@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
def librarian_view(request):
    return HttpResponse("Welcome to the Librarian page!")

# View for Member role
@user_passes_test(lambda u: u.userprofile.role == 'Member')
def member_view(request):
    return HttpResponse("Welcome to the Member page!")



