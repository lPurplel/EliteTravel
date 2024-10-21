from django import forms
from .models import Booking_flight
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_confirm = forms.CharField(
        label="Confirm password", widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("This email is already used")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise ValidationError("Password do not match")


class Booking_Form(forms.ModelForm):
    class Meta:
        model = Booking_flight
        fields = ['plane_name', 'email', 'airport',
                  'booking_time', 'total_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'id': 'id_email'})
        self.fields['plane_name'].widget.attrs.update({'id': 'id_plane_name'})
        self.fields['airport'].widget.attrs.update({'id': 'id_airport'})
        self.fields['booking_time'].widget.attrs.update(
            {'id': 'id_booking_time', 'min': 1, 'max': 720})
