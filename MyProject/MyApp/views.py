from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def jets(request):
    return render(request, "jets.html")

def about_us(request):
    return render(request, "about_us.html")

def booked_flights(request):
    return render(request, "booked_flights.html")
