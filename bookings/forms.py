from django import forms
from .models import *


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['client_name', 'client_email', 'client_phone']


# class ContactForm(forms.ModelForm):
#
#     class Meta:
#         model = ContactUs
#         fields = '__all__'
#

