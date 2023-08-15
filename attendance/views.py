
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework import generics, permissions
from . models import Attendance
from .serializers import AttendanceSerializer

# Create your views here.

class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]