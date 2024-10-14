from django.db import models

# Create your models here.


class Booking_flight(models.Model):
    PLANE_CHOICES = [
        ('light1', 'Cessna C525 Citation', 'light1.png'),
        ('light2', 'Embraer Phenom 300E', 'light2.png'),
        ('airline1', 'A380', 'airline2.png'),
        ('airline2', 'A320', 'airline2.png'),
        ('heavy1', 'Gulfstream G300', 'heavy1.png'),
        ('heavy2', 'Bombardier Global 7500', 'heavy2.png')
    ]

    AIRPORT_CHOICES = [
        ('JFK', 'John F. Kennedy International Airport'),
        ('LAX', 'Los Angeles International Airport'),
        ('ATL', 'Atlanta Hartsfield-Jackson International Airport')
    ]

    plane_name = models.CharField(max_length=50, choices=[(
        choice[0], choice[1]) for choice in PLANE_CHOICES])
    email = models.EmailField()
    airport = models.CharField(max_length=50, choices=AIRPORT_CHOICES)
    booking_time = models.CharField(max_length=50)


def __str__(self):
    return f"{self.plane_name} at {self.airport}"
