"""
Test cases for ordering taxi.
"""
# Django Packages
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

#REST FRAMEWORK PACKAGES
from rest_framework.test import APIClient
from rest_framework import status

#Internal Packages
from taxi.models.models import OrderTaxi

TAXI_ORDER_URL = reverse('taxi:order-list')

def create_user(**params):
    """create and return a user"""
    return get_user_model().objects.create_user(**params)

def order_taxi(user, **params):
    """Create and return a taxi order."""
    order = OrderTaxi.objects.create(user=user, **params)
    return order

class PublicOrderTaxiTests(TestCase):
    """Test cases for unauthorized users."""
    def setUp(self):
        self.client = APIClient()
    
    def test_order_taxi_unavailable(self):
        """Test ordering Taxi is Unavailable for unauthorized users."""
        payload = {
            'from_location': 'TestLocation',
            'to_location': 'TestDestination',
        }

        response = self.client.post(TAXI_ORDER_URL, payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateOrderTaxiTests(TestCase):
    """Test cases for authorized users."""
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            first_name='Test',
            last_name='Testov',
            phone_number='887776655',
            password='1234test',
        )
        self.client.force_authenticate(self.user)
    
    def test_order_taxi(self):
        """Test case for ordering taxi for authorized user."""
        taxi_order = OrderTaxi.objects.create(
            user=self.user,
            from_location='TestLocation',
            to_location='TestDestination',
        )

        self.assertEqual(str(taxi_order), f"{taxi_order.from_location}-{taxi_order.to_location}")
    
    def test_orders_by_user(self):
        """Test lists taxi orders by a user."""