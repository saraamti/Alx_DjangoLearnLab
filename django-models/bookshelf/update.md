# Update Operation

```python
# Update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book  # This will output the updated book instance
