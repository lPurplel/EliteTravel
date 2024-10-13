from django.db import models

# Create your models here.

class Booking_flight(models.Model):
    PLANE_CHOICES = [
        ('light1', 'Cessna C525 Citation'),
        ('light2', 'Embraer Phenom 300E'),
        ('airline1', 'A380'),
        ('airline2', 'A320'),
        ('heavy1', 'Gulfstream G300'),
        ('heavy2', 'Bombardier Global 7500')
    ]

    AIRPORT_CHOICES = [
        ('JFK', 'John F. Kennedy International Airport'),
        ('LAX', 'Los Angeles International Airport'),
        ('ATL', 'Atlanta Hartsfield-Jackson International Airport')
    ]

    BOOKING_TIME_CHOICES = [
        ('4h', '4 hour'),
        ('8h', '8 hours'),
        ('16h', '16 hours')
    ]

    plane_name = models.CharField(max_length=50, choices=PLANE_CHOICES)
    email = models.EmailField()
    airport = models.CharField(max_length=50, choices=AIRPORT_CHOICES)
    booking_time = models.CharField(max_length=50, choices=BOOKING_TIME_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000)

    def __str__(self):
        return f"{self.plane_name} at {self.airport}"
