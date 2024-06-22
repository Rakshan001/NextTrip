from django.db import models
from django.contrib.auth.models import User
from nextbus.models import Station, Bus

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    origin = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='origin_tickets')
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='destination_tickets')
    date = models.DateField()
    time = models.TimeField()
    cost = models.FloatField()
    ticket_number = models.CharField(max_length=10, unique=True)
    is_verified = models.BooleanField(default=False)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)  # ForeignKey to Bus model
