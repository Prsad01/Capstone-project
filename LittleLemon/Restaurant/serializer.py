from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class MenuSerialier(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class BookingSerialier(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'