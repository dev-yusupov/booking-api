"""

Serializers for Taxi App APIs.
03.07.2023
Bobur Yusupov

"""
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import (
    Serializer, 
    ModelSerializer,
)

class TaxiDriverSerializer(ModelSerializer):
    """Serializer for Taxi Driver Profile."""
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True, 
                'min_length': 5
                },
            'phone_number': {
                'max_length': 13,
            }
        }
    
    def create(self, validated_data):
        """Create and return a taxi profile."""
        return get_user_model().objects.create_taxi(**validated_data)