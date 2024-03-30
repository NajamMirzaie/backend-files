from django.urls import path
from .views import TreadmillDataListCreateAPIView, WorkoutHistoryAPIView

urlpatterns = [
    path('treadmill-data/', TreadmillDataListCreateAPIView.as_view(), name='treadmill-data-list-create'),
    path('workout-history/', WorkoutHistoryAPIView.as_view(), name='workout-history'),
]
