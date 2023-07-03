from django.urls import path

from rest_framework.routers import DefaultRouter

from taxi.views.taxi_driver_view import (
    CreateTaxiDriverAccout,
)

app_name = 'taxi'

urlpatterns = [
    path("create/", CreateTaxiDriverAccout.as_view(), name="create-taxi-account"),
]
