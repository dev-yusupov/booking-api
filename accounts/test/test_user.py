"""
Test for User.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTest(TestCase):
    """Test cases for User model."""

    def test_create_user_with_email_successful(self):
        email = "test@test.com"
        password = "1234test"
        first_name = "Bob"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_user)
        self.assertTrue(user.check_password(password))
    
    def test_create_user_normalized_email(self):
        """Test creates a user with normalized email."""
        sample_emails = [
            ['test1@TEST.com', "test1@test.com"],
            ['Test2@Test.com', "Test2@test.com"],
            ['TEST3@TEST.com', "TEST3@test.com"],
            ['test4@Test.COM', "test4@test.com"],
        ]

        for email, expected_email in sample_emails:
            user = get_user_model().objects.create_user(email, "123test")
            self.assertEqual(user.email, expected_email)
        
    def test_create_super_user(self):
        """Test creates, returns and saves a superuser."""
        email = "test@admin.com"
        password="1234test"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, "test@admin.com")
        self.assertTrue(user.check_password(password))
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
    
    def test_new_user_returns_error_without_email(self):
        """Test create a user without email returns ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', '')
    
    def test_new_user_return_error_without_password(self):
        """Test create a user without password raises ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('test@test.com', '')