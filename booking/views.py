from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
class BookingList(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer