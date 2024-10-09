from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path("/jets", views.jets, name="jets"),
    path("/about_us", views.about_us, name="about_us"),
    path("/booked_flights", views.booked_flights, name="booked_flights")
    ]