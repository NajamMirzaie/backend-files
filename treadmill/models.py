from django.db import models
from account.models import User

class TreadmillData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    distance = models.FloatField()  # Distance counting
    duration = models.DurationField()  # Time counting
    speed = models.FloatField()  # Speed counting
    heart_rate = models.IntegerField()  # Heart rate
    calories_burned = models.FloatField()  # Calories burned

    def __str__(self):
        return f"TreadmillData: User={self.user}, Timestamp={self.timestamp}"
