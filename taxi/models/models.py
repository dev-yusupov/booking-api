"""
Model for Taxi App.
04.07.2023
"""
from uuid import uuid4
from django.db import models
from django.conf import settings

from taxi.functions.measure_length import Distance

class OrderTaxi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    from_location = models.CharField(max_length=254)
    to_location = models.CharField(max_length=254)

    @property
    def price(self):
        price = Distance(self.from_location, self.to_location)
        return price.price

    def __str__(self):
        return f"{self.from_location}-{self.to_location}"
