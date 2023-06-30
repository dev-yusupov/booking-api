"""
Test for Django Admin modification.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
    """Tests for Django admin."""

    def setUp(self):
        """Create a user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="superuser@example.com",
            password="1234test",
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="1234test",
            first_name="Test",
            last_name="Testov"
        )
    
    def test_user_list(self):
        """Tests that users are in list."""
        url = reverse("admin:accounts_user_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.user.first_name)
        self.assertContains(response, self.user.last_name)

    def test_user_edit_page(self):
        """Test Edit page."""
        url = reverse("admin:accounts_user_change", args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
    
    def test_user_create_page(self):
        """Test Create user page."""
        url = reverse("admin:accounts_user_add")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)