from django import forms
from .models import Booking_flight


class Booking_Form(forms.ModelForm):
    class Meta:
        model = Booking_flight
        fields = ['plane_name', 'email', 'airport', 'booking_time', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'id': 'id_email'})
        self.fields['plane_name'].widget.attrs.update({'id': 'id_plane_name'})
        self.fields['airport'].widget.attrs.update({'id': 'id_airport'})
        self.fields['booking_time'].widget.attrs.update(
            {'id': 'id_booking_time'})
