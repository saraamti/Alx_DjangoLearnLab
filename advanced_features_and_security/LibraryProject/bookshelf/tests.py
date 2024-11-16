from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from .models import Book

class PermissionTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title="Test Book", author="Author Name")
        self.view_group = Group.objects.create(name="Viewers")

    def test_view_permission(self):
        self.client.login(username="viewer", password="password")
        response = self.client.get(reverse('view_books'))
        self.assertEqual(response.status_code, 403)  # Permission denied without group

