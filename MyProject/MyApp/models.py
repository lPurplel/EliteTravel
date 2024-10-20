from django.db import models

# Create your models here.


class Booking_flight(models.Model):
    PLANE_CHOICES = [
        ('light1', 'Cessna C525 Citation', 'images/light1.png', 2450),
        ('light2', 'Embraer Phenom 300E', 'images/light2.png', 3250),
        ('airline1', 'A380', 'images/airline1.png', 31520),
        ('airline2', 'A320', 'images/airline2.png', 21000),
        ('heavy1', 'Gulfstream G300', 'images/heavy1.png', 5800),
        ('heavy2', 'Bombardier Global 7500', 'images/heavy2.png', 8530)
    ]

    AIRPORT_CHOICES = [
        ('JFK', 'John F. Kennedy International Airport'),
        ('LAX', 'Los Angeles International Airport'),
        ('ATL', 'Atlanta Hartsfield-Jackson International Airport')
    ]

    plane_name = models.CharField(max_length=50, choices=[(choice[0], choice[1]) for choice in PLANE_CHOICES])
    email = models.EmailField()
    airport = models.CharField(max_length=50, choices=AIRPORT_CHOICES)
    booking_time = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    plane_image = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return f"{self.plane_name} at {self.airport}"
