from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library  # Ensure this line includes Library as well as Book
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile , Book
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

   def get_object(self):
        return Library.objects.get(name = "Cairo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        books = library.books.all()
        context['books'] = books
        return context
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect(reverse_lazy('login'))  # Redirect to the login page
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})






