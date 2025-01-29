from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import User, Booking
from rest_framework import serializers

class UserCUDSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model=User
        fields=['username','password']
    
    def create(self,validated_data):
        password = validated_data.pop("password")
        hashed_password = make_password(password)
        validated_data["password"] = hashed_password
        
        return super().create(validated_data)

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model, including CustomModeSettings if mode is 'Custom'.
    """
    class Meta:
        model = Booking
        fields = ['id', 'user', 'date', 'timeslot', 'mode', 'created_at', 'status']
        read_only_fields = ['id', 'created_at', 'status']

