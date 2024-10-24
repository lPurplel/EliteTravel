from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path("signUp", views.signUp, name="signUp"),
    path("signIn", views.signIn, name="signIn"),
    path('signIn', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path("account", views.account, name="account"),
    path("jets", views.jets, name="jets"),
    path("aboutUs", views.aboutUs, name="aboutUs"),
    path("booked", views.booked, name="booked"),
    path("booking", views.booking, name="booking"),
    path("light", views.light, name="light"),
    path("light1", views.light1, name="light1"),
    path("light2", views.light2, name="light2"),
    path("heavy", views.heavy, name="heavy"),
    path("heavy1", views.heavy1, name="heavy1"),
    path("heavy2", views.heavy2, name="heavy2"),
    path("airline", views.airline, name="airline"),
    path("airline1", views.airline1, name="airline1"),
    path("airline2", views.airline2, name="airline2")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
