from django.db import models
import uuid
from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from utils.types import TokenType

def default_expiry():
    return timezone.now() + timedelta(days=7)

class User(AbstractBaseUser):
    id = models.CharField(primary_key=True, max_length=36, default=uuid.uuid4)
    username = models.CharField(max_length=100, unique=True)
    admission_no = models.CharField(max_length=12, unique=True, editable=False, default=f'ADM-{uuid.uuid4().hex[:8].upper()}')
    current_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    password = models.CharField(max_length=200, blank=True, null=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username


class Token(models.Model):
    TOKEN_TYPE_CHOICES = [
        (TokenType.ACCESS, TokenType.ACCESS),
        (TokenType.REFRESH, TokenType.REFRESH)
        ]
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    token = models.TextField(null=False)
    token_type = models.CharField(max_length=20,choices=TOKEN_TYPE_CHOICES,null=False)
    expiry = models.DateTimeField(default=default_expiry)

class Booking(models.Model):
    WASHING_MODES = [
        # ('Eco', 'Eco Mode'),
        ('Quick Washing', 'Quick Washing'),
        ('Steam Ironing', 'Steam Ironing'),
        ('Normal Washing', 'Normal Washing'),
    ]

    STATUS_CHOICES = [
        ('booked', 'Booked'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Unique booking ID
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")  # Link to the user
    date = models.DateField()  # Date of booking
    timeslot = models.CharField(max_length=50,null=True)
    # time = models.TimeField()  # Time of booking
    mode = models.CharField(max_length=30, choices=WASHING_MODES)  # Washing mode
    # estimated_cloth_weight = models.DecimalField(max_digits=5, decimal_places=2)  # Estimated weight in kilograms
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set to now when the object is created
    # ironing = models.BooleanField(null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='booked')  # New field for status


    def __str__(self):
        return f"Booking {self.id} by {self.user.username} on {self.date} "

