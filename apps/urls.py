from django.urls import path
from apps.views import index, contacts, location, price, team

urlpatterns = [
    path('', index),
    path('contacts/<str:header>/', contacts),
    path('location/<str:header>/', location),
    path('price/<str:header>/', price),
    path('team/<str:header>/', team),
]