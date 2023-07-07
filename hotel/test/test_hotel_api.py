"""

Test cases for Retrieving Hotel data for Hotel Model.
06.07.2023

"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

from hotel.serializers.hotel_model_api_serializers import (
    HotelsSerializer,
    HotelDetailSerializer,
    )
from hotel.models.hotel_models import (
    Hotel,
    HotelRoomOrder,
)

HOTELS_URL = reverse('hotel:hotel-list')

def create_user(email='test@test.com', password="1234test",**params):
    """Create and return a user."""
    user = get_user_model().objects.create_user(email=email, password=password, **params)
    return user

def create_hotel(hotel_name, min_price, max_price, **params):
    """Create and return hotel."""
    hotel = Hotel.objects.create(hotel_name=hotel_name, min_price=min_price, max_price=max_price, **params)
    return hotel

def hotel_detail(hotel_id):
    """Returns details of a hotel."""
    return reverse('hotel:hotel-detail', args=[hotel_id])

# class PublicHotelAPITests(TestCase):
#     """Test Unauth API request."""
#     def setUp(self):
#         self.client = APIClient()

#     def test_auth_required(self):
#         """Test auth is required for retrieving hotel object."""
#         response = self.client.get(HOTELS_URL)

#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateHotelAPITests(TestCase):
    """Test cases for authorized requests. Retrieving list of hotels."""
    
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(email="test@test.com", password="1234test")
        self.client.force_authenticate(self.user)
    
    def test_retrieve_hotels(self):
        """Test retrieves list of hotels."""
        create_hotel(hotel_name="Testing", min_price=200, max_price=500)
        create_hotel(hotel_name="Testov", min_price=200, max_price=500)

        response = self.client.get(HOTELS_URL)

        hotels = Hotel.objects.order_by('-name')
        serializer = HotelsSerializer(hotels, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_retrieve_hotel_details(self):
        """Test retrieves hotel details."""
        hotel = create_hotel(hotel_name="Testing", min_price=200, max_price=500)

        url = hotel_detail(hotel.id)
        response = self.client.get(url)

        serializer = HotelDetailSerializer(hotel)

        self.assertEqual(response.data, serializer.data)