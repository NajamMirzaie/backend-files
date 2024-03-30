from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import TreadmillData
from .serializers import TreadmillDataSerializer, WorkoutHistorySerializer

class TreadmillDataListCreateAPIView(generics.ListCreateAPIView):
    queryset = TreadmillData.objects.all()
    serializer_class = TreadmillDataSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WorkoutHistoryAPIView(generics.ListAPIView):
    queryset = TreadmillData.objects.all()
    serializer_class = WorkoutHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(user=user)
