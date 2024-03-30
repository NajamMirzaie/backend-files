from rest_framework import serializers
from .models import TreadmillData

class TreadmillDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreadmillData
        fields = '__all__'

class WorkoutHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TreadmillData
        fields = ['timestamp', 'distance', 'duration', 'speed', 'heart_rate', 'calories_burned']
