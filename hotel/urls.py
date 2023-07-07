from django.urls import path, include

from rest_framework.routers import DefaultRouter

from hotel.views.hotel_views import (
    HotelView,
    )

router = DefaultRouter()

app_name = 'hotel'
router.register('hotel', HotelView)
# router.register('manage', CreateHotelView)


urlpatterns = [
    path('', include(router.urls)),
]
