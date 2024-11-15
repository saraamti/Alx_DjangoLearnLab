from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import LibraryDetailView 

urlpatterns = [
    path('books/', views.list_books, name='book-list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', views.admin_view, name='admin-view'),
    path('librarian/', views.librarian_view, name='librarian-view'),
    path('member/', views.member_view, name='member-view'),
    path('add_book/', views.add_book, name='add-book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit-book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete-book'),
]
