from django.shortcuts import render
from rest_framework import viewsets
# from rest_framework import generics
from .serializer import UserSerializer, MenuSerialier, BookingSerialier
from django.contrib.auth.models import  User
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def index(request):
    return render(request,'index.html',{})


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerialier

class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class =  BookingSerialier
    permission_classes = [IsAuthenticated]
