# Admin Setup for Book Model

## 1. Registering the Book Model
To manage the `Book` model in the Django admin interface, we registered it by adding the following code in `bookshelf/admin.py`:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
