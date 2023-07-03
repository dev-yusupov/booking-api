"""

Serializers for the USER APIs

Create, Update and Delete users using this serializers.
03.07.2023

"""
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import (
    get_user_model,
    authenticate,
    )

from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    ValidationError
    )
from rest_framework import serializers

class UserSerializer(ModelSerializer):
    """Serializer for the user objects."""
    class Meta:
        model = get_user_model()
        fields = ["email", "first_name", "last_name", "phone_number", "password"]
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}, "phone_number": {"max_length": 13}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        
        return user

class AuthTokenSerializer(Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style = {
            'input_type': 'password'
        },
        trim_whitespace = False,
    )

    def validate(self, attrs):
        """Validate and authenticate the users."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise ValidationError(msg, code="authorization")
        
        attrs['user'] = user
        return attrs

