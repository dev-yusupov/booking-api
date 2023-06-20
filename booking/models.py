from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"