"""

Test cases for Retrieving Hotel data for Hotel Model.
06.07.2023

"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

from hotel.models.hotel_models import (
    Hotel,
)
from hotel.serializers.hotel_model_api_serializers import (
    HotelsSerializer,
    HotelDetailSerializer,
)

HOTEL_URL = reverse('hotel:hotel-list')

def create_hotel(**params):
    payload = {
        'hotel_name': 'Test',
        'hotel_location': 'https://example.com/',
        'min_price': 400,
        'max_price': 600,
    }

    payload.update(**params)

    hotel = Hotel.objects.create(**payload)
    return hotel

def hotel_detail(hotel_id):
    """Create and return a hotel's details."""
    return reverse('hotel:hotel-detail', args=[hotel_id])

class PublicApiRequestsTest(TestCase):
    """Test cases for authorized user requests."""

    def setUp(self):
        self.client = APIClient()
    
    def test_auth_required(self):
        """Test auth is required to call API."""
        response = self.client.get(HOTEL_URL)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateApiRequestsTests(TestCase):
    """Test cases for authorized user requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="info@info.com",
            password='1234test',
        )
        
        self.client.force_authenticate(self.user)

    def test_retrieve_hotel_list(self):
        """Retrieve all hotel objects."""
        response = self.client.get(HOTEL_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_permission_not_allowed(self):
        """Test created for testing whether user is superuser or user. And User does not have permission to the operation in test."""
        payload = {
            'hotel_name': 'Test',
            'hotel_location': 'https://google.com/maps/',
            'min_price': 100,
            'max_price': 500,
        }

        response = self.client.post(HOTEL_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    
    def test_retrieve_hotel_detail(self):
        """Test creates a hotel and returns its details."""
        hotel = create_hotel()

        url = hotel_detail(hotel.id)
        response = self.client.get(url)
        serializer = HotelDetailSerializer(hotel)

        self.assertEqual(response.data, serializer.data)