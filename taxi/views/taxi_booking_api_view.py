"""
Views for OrderTaxi Model
"""
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from taxi.models.models import OrderTaxi
from taxi.serializers.taxi_order_serializer import OrderTaxiSerializer

class TaxiOrderViewSet(ModelViewSet):
    """Viewset for manage ordering taxi."""
    serializer_class = OrderTaxiSerializer
    queryset = OrderTaxi.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = self.queryset

        return queryset.filter(
            user=self.request.user
        ).order_by("-id").distinct()
    
    def perform_create(self, serializer):
        """Create a new taxi order."""
        serializer.save(user=self.request.user)
    
    def get_serializer_class(self):
        return self.serializer_class