"""
Models for Hotel App
07.06.2023
"""
from uuid import uuid4
from django.db import models

from functions.id_key_generation import RandomID

class Hotel(models.Model):
    """Model for registering hotels."""
    random = RandomID()
    id = models.AutoField(primary_key=True, default=random.generate_six_digit_id(), editable=False, unique=True)
    hotel_name = models.CharField(max_length=254)
    hotel_location = models.URLField()
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    phone_number = models.CharField(max_length=13)
    start_of_work = models.TimeField(default="08:00")
    end_of_work = models.TimeField(default="20:00")

    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.hotel_name}"

class HotelRoomOrder(models.Model):
    """Model for booking room from hotel."""
    order_id = models.UUIDField(primary_key=True, editable=False, default=uuid4())
    hotel_name = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
    )
    room_number = models.IntegerField(default=1)
    people_number = models.IntegerField(default=1)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    additional_points = models.TextField(blank=True)

    def __str__(self):
        return f"{self.hotel_name} ({self.people_number}people)"