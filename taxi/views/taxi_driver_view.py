"""
View for Taxi Driver profiles
03.07.2023
"""
from rest_framework.generics import (
    CreateAPIView,
)

from taxi.serializers.taxi_serializers import(
    TaxiDriverSerializer,
) 

class CreateTaxiDriverAccout(CreateAPIView):
    """Create a new Taxi Driver Account."""
    serializer_class = TaxiDriverSerializer