from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('cars/',views.cars,name="car"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
]