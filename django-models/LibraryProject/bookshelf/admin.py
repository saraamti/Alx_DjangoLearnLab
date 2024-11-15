from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    list_filter = ('publication_year', 'author')            # Fields to filter by
    search_fields = ('title', 'author')                     # Fields to search in

admin.site.register(Book, BookAdmin)

