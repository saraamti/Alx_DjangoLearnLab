from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<in :pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
    path('login/', LoginView.as_view(template_name= 'relationship_app/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name = 'logout'),
    path('register/', views.register.as_view(), name = "register"),
]
