"""

Test cases for Taxi Drivers.
07.03.2023
Bobur Yusupov

"""
from django.test import TestCase
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_TAXI_PROFILE_URL = reverse("taxi:create-taxi-account")
# TOKEN_URL = reverse("accounts:token")
# TAXI_PROFILE_URL = reverse("taxi:taxi-profile")

def create_taxi_account(**params):
    return get_user_model().objects.create_taxi(**params)

class PublicTaxiTests(TestCase):
    """Test cases for unauthorized Taxi Drivers."""
    def setUp(self):
        self.client = APIClient()
    
    def test_create_taxi_account_successful(self):
        """Test Create and returns a Taxi Driver Account successful."""
        payload = {
            'email': "taxi@test.com",
            'first_name': "Taxi",
            'last_name': 'Taxiov',
            'phone_number': '222334455',
            'password': 'taxi1234',
        }
        
        response = self.client.post(CREATE_TAXI_PROFILE_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_taxi_profile_exist_email_error(self):
        """Test return error if email exists."""
        payload = {
            'email': "taxi@test.com",
            'first_name': "Taxi",
            'last_name': 'Taxiov',
            'phone_number': '222334455',
            'password': 'taxi1234',
        }

        create_taxi_account(**payload)
        response = self.client.post(CREATE_TAXI_PROFILE_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_password_too_short(self):
        """Test return error if password is less than 5 charachers."""
        payload = {
            'email': "taxi@test.com",
            'first_name': "Taxi",
            'last_name': 'Taxiov',
            'phone_number': '222334455',
            'password': 'pw',
        }
        
        response = self.client.post(CREATE_TAXI_PROFILE_URL, payload)
        user_exists = get_user_model().objects.filter(email=payload['email']).exists()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(user_exists)
    
    def test_no_phone_number_error(self):
        """Test returns error if phone number is not provided."""
        payload = {
            'email': "taxi@test.com",
            'first_name': "Taxi",
            'last_name': 'Taxiov',
            'phone_number': '',
            'password': 'taxi1234',
        }
        
        response = self.client.post(CREATE_TAXI_PROFILE_URL, payload)
        user_exists = get_user_model().objects.filter(phone_number=payload['phone_number']).exists()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(user_exists)
