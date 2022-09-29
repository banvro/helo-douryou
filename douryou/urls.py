from django.contrib import admin
from django.urls import path, include
from douryou import views



urlpatterns = [
    path("", views.home, name='home'),
]