from django.test import TestCase
from .models import Booking

# Create your tests here.
class BookingTests(TestCase):
    """Booking model test cases."""
    @classmethod
    def setUpTestData(self):
        self.booking = Booking.objects.create(
            first_name = "Test",
            last_name = "Testov",
            phone_number = "992004772410",
            date_time = "2023-06-20 09:11:02"
        )
    
    def test_booking_content(self):
        self.assertEqual(self.booking.first_name, "Test")
        self.assertEqual(self.booking.last_name, "Testov")
        self.assertEqual(self.booking.phone_number, "992004772410")
        self.assertEqual(str(self.booking), "Test Testov")