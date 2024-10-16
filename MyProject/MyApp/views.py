from django.shortcuts import render, redirect
from .models import Booking_flight
from .forms import Booking_Form

# Create your views here.


def home(request):
    return render(request, "index.html")


def jets(request):
    return render(request, "jets.html")


def aboutUs(request):
    return render(request, "aboutUs.html")


def booked(request):
    return render(request, "booked.html")


def light(request):
    return render(request, "light.html")


def light1(request):
    return render(request, "light1.html")


def light2(request):
    return render(request, "light2.html")


def heavy(request):
    return render(request, "heavy.html")


def heavy1(request):
    return render(request, "heavy1.html")


def heavy2(request):
    return render(request, "heavy2.html")


def airline(request):
    return render(request, "airline.html")


def airline1(request):
    return render(request, "airline1.html")


def airline2(request):
    return render(request, "airline2.html")


def booked(request):
    flights = Booking_flight.objects.all()
    first_flight = flights[0] if flights else None
    second_flight = flights[1] if len(flights) > 1 else None
    third_flight = flights[2] if len(flights) > 2 else None
    return render(request, 'booked.html', {
        'first_flight': first_flight,
        'second_flight': second_flight,
        'third_flight': third_flight
    })
def booking(request):
    if request.method == 'POST':
        form = Booking_Form(request.POST)
        if form.is_valid():
            booking = form.save()
            plane_name = booking.plane_name
            plane_image = next((choice[2] for choice in Booking_flight.PLANE_CHOICES if choice[0] == plane_name), '')
            booking.plane_image = plane_image
            plane_price = next((choice[3] for choice in Booking_flight.PLANE_CHOICES if choice[0] == plane_name), 0)
            booking.total_price = plane_price * booking.booking_time
            booking.save(update_fields=['plane_image', 'total_price'])
            return redirect('booked')
        else:
            print(form.errors)
    else:
        form = Booking_Form()

    return render(request, 'booking.html', {'form': form})

