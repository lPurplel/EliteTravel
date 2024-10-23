from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Booking_flight
from .forms import Booking_Form
import pdb
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
    }
    return render(request, 'index.html', context)


def signUp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    print(form.errors)
    return render(request, 'signUp.html', {'form': form})


def signIn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None

            if user:
                user = authenticate(username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    form.add_error('password', 'Incorrect password.')
            else:
                form.add_error(
                    'email', 'User not found')
    else:
        form = LoginForm()

    return render(request, 'signIn.html', {'form': form})


def jets(request):
    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
    }
    return render(request, 'jets.html', context)


def aboutUs(request):
    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
    }
    return render(request, 'aboutUs.html', context)


def light(request):
    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
    }
    return render(request, 'light.html', context)


def light1(request):
    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
    }
    return render(request, 'light1.html', context)


def light2(request):
    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
    }
    return render(request, 'light2.html', context)


def heavy(request):
    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
    }
    return render(request, 'heavy.html', context)


def heavy1(request):
    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
    }
    return render(request, 'heavy1.html', context)


def heavy2(request):
    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
    }
    return render(request, 'heavy2.html', context)


def airline(request):
    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
    }
    return render(request, 'airline.html', context)


def airline1(request):
    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
    }
    return render(request, 'airline1.html', context)


def airline2(request):
    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
    }
    return render(request, 'airline2.html', context)


@login_required()
def booked(request):
    flights = Booking_flight.objects.all()

    booking = Booking_flight.objects.filter(
        pk=request.session.get('last_booking_id')).first()

    first_flight = None
    second_flight = None
    third_flight = None

    if flights.exists():
        first_flight = flights[0] if flights.count() > 0 else None
        second_flight = flights[1] if flights.count() > 1 else None
        third_flight = flights[2] if flights.count() > 2 else None

    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
        'ff': first_flight,
        'sf': second_flight,
        'tf': third_flight,
        'booking_id': booking.id if booking else None,
        'BF': flights
    }
    return render(request, 'booked.html', context)


@login_required()
def booking(request):
    if request.method == 'POST':
        form = Booking_Form(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)

            plane_name = booking.plane_name

            plane_image = next(
                (choice[2] for choice in Booking_flight.PLANE_CHOICES if choice[0] == plane_name), '')
            booking.plane_image = plane_image
            plane_price = next(
                (choice[3] for choice in Booking_flight.PLANE_CHOICES if choice[0] == plane_name), 0)
            booking.total_price = plane_price * booking.booking_time

            booking.save()
            request.session['last_booking_id'] = booking.id
            return redirect('booked')
        else:
            print(form.errors)
    else:
        form = Booking_Form()

    if request.user.is_authenticated:
        first_letter = request.user.email[0].upper()
    else:
        first_letter = ''
    context = {
        'first_letter': first_letter,
        'form': form
    }
    return render(request, 'booking.html', context)
