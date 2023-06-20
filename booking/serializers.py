from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "date_time"
        )