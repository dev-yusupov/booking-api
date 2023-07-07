from rest_framework.mixins import (
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from rest_framework.viewsets import (
    GenericViewSet,
    ModelViewSet,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    )
from rest_framework.authentication import (
    TokenAuthentication,
)
from rest_framework.decorators import action

from hotel.serializers.hotel_model_api_serializers import (
    HotelDetailSerializer,
    HotelsSerializer,
    )
from hotel.models.hotel_models import (
    Hotel,
)


class HotelView(
    GenericViewSet,
    RetrieveModelMixin,
    ListModelMixin,
):
    """ViewSet for Hotel Model."""
    queryset = Hotel.objects.all()
    serializer_class = HotelDetailSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        """Retrieve list of hotels for authenticated users."""
        queryset = self.queryset.order_by('-hotel_name')
        
        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return HotelsSerializer
        
        return self.serializer_class
    


# class CreateHotelView(
#     GenericViewSet,
#     RetrieveModelMixin,
#     ListModelMixin, 
#     UpdateModelMixin,
#     CreateModelMixin,
#     DestroyModelMixin,
# ):
    
#     queryset = Hotel.objects.all()
#     serializer_class = HotelDetailSerializer
#     permission_classes = [IsAdminUser]
#     authentication_classes = [TokenAuthentication]
#     http_method_names = ['get', 'post', 'patch', 'delete']

#     def get_queryset(self):

#         queryset = self.queryset
#         return queryset.all().order_by('-hotel_name')

#     def perform_create(self, serializer):
#         serializer.save()