from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
class BookingList(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer