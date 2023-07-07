"""
Serializer for Hotel model
"""
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from hotel.models.hotel_models import (
    Hotel,
)

class HotelsSerializer(ModelSerializer):
    """Serializer for Hotel model."""
    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name']

    def create(self, validated_data):
        hotel = Hotel.objects.create(**validated_data)

        return hotel
    

class HotelDetailSerializer(HotelsSerializer):
    """Serializer for details of a Hotel."""
    class Meta(HotelsSerializer.Meta):
        fields = HotelsSerializer.Meta.fields + ['hotel_location', 'min_price', 'max_price', 'phone_number', 'start_of_work', 'end_of_work', 'description']