"""

Views for user authentication user
03.07.2023

"""
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView, 
    )
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from accounts.serializers.user_api_serializers import (
    UserSerializer,
    AuthTokenSerializer,
    )

class CreateUserView(CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(RetrieveUpdateAPIView):
    """Manage authorized user."""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_object(self):
        return self.request.user