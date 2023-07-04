"""
Serializers for ordering taxi
04.07.2023
"""
from rest_framework.serializers import ModelSerializer

from taxi.models.models import OrderTaxi

class OrderTaxiSerializer(ModelSerializer):
    """OrderTaxi Serializer."""
    class Meta:
        model = OrderTaxi
        fields = ['id', 'from_location', 'to_location', 'price']
        read_only_fields = ['id']
    
    def create_taxi_order(self, validated_data):
        taxi_order = OrderTaxi.objects.create(**validated_data)

        return taxi_order