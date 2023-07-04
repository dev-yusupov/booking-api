"""
Test cases for user APIs

Testing Creating, Updating and Deleting users
03.07.2023 
"""
from django.test import TestCase
from django.contrib.auth import (
    authenticate,
    get_user_model,
)
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse("accounts:signup")
TOKEN_URL = reverse("accounts:token")
LOGIN_URL = reverse("accounts:login")
ME_URL = reverse("accounts:profile")

def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test cases for unauthenticated users."""

    def setUp(self):
        self.client = APIClient()
    
    def test_create_user_successful(self):
        """Test creates user successful."""
        payload = {
            "email": "test@test.com",
            "first_name": "Test",
            "last_name": "Testov",
            "phone_number": "004772410",
            "password": "1234test",
        }

        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(email=payload["email"])

        self.assertEqual(user.first_name, payload["first_name"])
        self.assertEqual(user.last_name, payload["last_name"])
        self.assertEqual(user.phone_number, payload["phone_number"])
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", response.data)

    def test_user_with_exits_email_error(self):
        payload = {
            "email": "test@test.com",
            "first_name": "Testing",
            "last_name": "Testingov",
            "phone_number": "997772410",
            "password": "1234testing",
        }

        create_user(**payload)
        response = self.client.post(CREATE_USER_URL, payload)
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_too_short_password_error(self):
        """Test returns error if password is less than 5 charachters."""
        payload = {
            "email": "testing@test.com",
            "first_name": "Test",
            "last_name": "Testing",
            "phone_number": "889997733",
            "password": "ts",
        }

        response = self.client.post(CREATE_USER_URL, payload)
        user_exists = get_user_model().objects.filter(email=payload["email"]).exists()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(user_exists)
    
    def test_no_phone_number_error(self):
        """Test returns error if phone number isn't provided."""
        payload = {
            "email": "test@test.com",
            "first_name": "Test",
            "last_name": "Testov",
            "phone_number": "",
            "password": "1234test",
        }

        response = self.client.post(CREATE_USER_URL, payload)
        user_exists = get_user_model().objects.filter(email=payload["email"])

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(user_exists)
    
    def test_create_token_for_user(self):
        """Test generates token for valid credentials."""
        user_detail = {
            "email": "test@test.com",
            "first_name": "Test",
            "last_name": "Testov",
            "phone_number": "998887766",
            "password": "1234test",
        }

        create_user(**user_detail)

        payload = {
            "email": user_detail["email"],
            "password": user_detail["password"],
        }

        response = self.client.post(TOKEN_URL, payload)

        self.assertIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_token_bad_credentials(self):
        """Test returns error if credentials invalid."""
        create_user(email="test@test.com", password="1234test")

        payload = {
            "email": "",
            "password": "badresponse",
        }

        response = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_token_blank_password(self):
        """Test posting a blank password returns an error."""
        payload = {
            'email': 'test@test.com',
            'password': '',
        }

        response = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_retrieve_user_unauthorized(self):
        """Test returns error if user is not authorized."""
        response = self.client.get(ME_URL)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(TestCase):
    """Test cases for authenticated users."""
    def setUp(self):
        self.user = create_user(
            email="test@test.com",
            first_name="Test",
            last_name="Testov",
            phone_number="998887766",
            password="1234test",
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    
    def test_retrieve_profile_success(self):
        """Test retrieving profile for logged in user."""
        response = self.client.get(ME_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "phone_number": self.user.phone_number,
        })
    
    
    def test_post_me_not_allowed(self):
        """Test POST is not allowed to ME endpoint."""
        response = self.client.post(ME_URL, {})

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        
    
    def test_update_user_profile(self):
        """Test updating user data."""
        payload = {
            "email": "info@test.com",
            "first_name": "Update",
            "last_name": "Updatov",
            "phone_number": "111223344",
            "password": "test12345",
        }

        response = self.client.patch(ME_URL, payload)

        self.user.refresh_from_db()

        self.assertEqual(self.user.email, payload["email"])
        self.assertEqual(self.user.first_name, payload["first_name"])
        self.assertEqual(self.user.last_name, payload["last_name"])
        self.assertEqual(self.user.phone_number, payload["phone_number"])
        self.assertTrue(self.user.check_password(payload["password"]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)