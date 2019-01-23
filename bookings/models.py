from django.db import models
from django import template
# Create your models here.


class AvailableTime(models.Model):
    date = models.DateField()
    time = models.TimeField()
    register = template.Library()

    def __str__(self):
        return str(self.time)


class Type(models.Model):
    type_title = models.CharField(max_length=50)
    category = models.IntegerField()
    price = models.FloatField(default=20)
    duration_in_min = models.PositiveIntegerField(default=30)
    image = models.FileField()
    details = models.CharField(default=None, max_length=200)

    def __str__(self):
        return self.type_title


class Booking(models.Model):

    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING)
    booking_time = models.ForeignKey(AvailableTime, on_delete=models.DO_NOTHING)
    client_name = models.CharField(max_length=200)
    client_email = models.EmailField(blank=True)
    client_phone = models.CharField(max_length=20)


class ContactUs(models.Model):

    email = models.EmailField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)



