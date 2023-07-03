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
        payload = {
            'email': "taxi@test.com",
            'first_name': "Taxi",
            'last_name': 'Taxiov',
            'phone_number': '222334455',
            'password': 'taxi1234',
        }
        
        response = self.client.post(CREATE_TAXI_PROFILE_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)