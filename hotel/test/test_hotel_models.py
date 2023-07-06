"""
Test cases for testing Hotel and HotelRoomOrder models
06.07.2023
"""

from django.test import TestCase
from hotel.models.hotel_models import (
    Hotel,
    HotelRoomOrder,
)

def create_hotel(name="Test Hotel"):
    """Function creates a hotel object."""
    return Hotel.objects.create(hotel_name=name, min_price=1, max_price=2)

class HotelModelTests(TestCase):
    """Test cases for tesing Hotel model."""
    def test_create_object_in_model(self):
        """Test case creates an object in Hotel model"""
        payload = {
            'hotel_name': 'Test hotel',
            'hotel_location': 'https://www.google.com/maps/test',
            'min_price': 100,
            'max_price': 1000,
            'phone_number': '+992009998877',
        }
        hotel = Hotel.objects.create(**payload)

        self.assertEqual(hotel.hotel_name, payload['hotel_name'])
        self.assertEqual(hotel.hotel_location, payload['hotel_location'])
        self.assertEqual(hotel.min_price, payload['min_price'])
        self.assertEqual(hotel.max_price, payload['max_price'])
        self.assertEqual(hotel.phone_number, payload['phone_number'])
        self.assertEqual(str(hotel), payload['hotel_name'])
    
    def test_create_room_order(self):
        """Test creates a hotel object and orders a room."""
        hotel = create_hotel()
        payload = {
            'room_number': 1,
            'people_number': 2,
            'date_start': '2023-08-08 18:00:00',
            'date_end': '2023-09-09 19:00:00',
        }

        room_order = HotelRoomOrder.objects.create(hotel_name=hotel, **payload)

        self.assertEqual(room_order.room_number, payload['room_number'])
        self.assertEqual(room_order.people_number, payload['people_number'])
        self.assertEqual(str(room_order), f'{hotel.hotel_name} ({payload["people_number"]}people)')