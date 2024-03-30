from django.contrib import admin
from .models import TreadmillData

@admin.register(TreadmillData)
class TreadmillDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'timestamp', 'distance', 'duration', 'speed', 'heart_rate', 'calories_burned']
    search_fields = ['user__username', 'timestamp']
    list_filter = ['user', 'timestamp']
    readonly_fields = ['timestamp']
