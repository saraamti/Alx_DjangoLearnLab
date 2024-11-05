# Delete Operation

```python
# Delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by checking if any books exist
Book.objects.all()
