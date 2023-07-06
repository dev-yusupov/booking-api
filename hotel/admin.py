from django.contrib import admin

from hotel.models.hotel_models import (
    Hotel,
    HotelRoomOrder,
    )

# Register your models here.
admin.site.register(Hotel)
admin.site.register(HotelRoomOrder)