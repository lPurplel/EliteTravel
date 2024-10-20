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

    booking = Booking_flight.objects.filter(pk=request.session.get('last_booking_id')).first()

    first_flight = None
    second_flight = None
    third_flight = None
    
    if flights.exists():
        first_flight = flights[0] if flights.count() > 0 else None
        second_flight = flights[1] if flights.count() > 1 else None
        third_flight = flights[2] if flights.count() > 2 else None

    return render(request, 'booked.html', {
        'ff': first_flight,
        'sf': second_flight,
        'tf': third_flight,
        'booking_id': booking.id if booking else None,
        'BF': flights
    })



def booking(request):
    if request.method == 'POST':
        form = Booking_Form(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            
            plane_name = booking.plane_name
            
            plane_image = next((choice[2] for choice in Booking_flight.PLANE_CHOICES if choice[0] == plane_name), '')
            booking.plane_image = plane_image
            plane_price = next((choice[3] for choice in Booking_flight.PLANE_CHOICES if choice[0] == plane_name), 0)
            booking.total_price = plane_price * booking.booking_time
            
            booking.save()
            request.session['last_booking_id'] = booking.id
            return redirect('booked')
        else:
            print(form.errors)
    else:
        form = Booking_Form()
    return render(request, 'booking.html', {'form': form})

