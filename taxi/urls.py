from django.urls import path, include

from rest_framework.routers import DefaultRouter

from taxi.views.taxi_booking_api_view import TaxiOrderViewSet

app_name = 'taxi'
router = DefaultRouter()
router.register("", TaxiOrderViewSet)

urlpatterns = [
    path('order/', include(router.urls))
]
