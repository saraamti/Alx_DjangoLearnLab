from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_books, name='view_books'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
]
