from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializers
from .models import Room
# Create your views here.

class Roomview(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class= RoomSerializers
