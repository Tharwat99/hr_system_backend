
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from . models import Attendance
from .serializers import AttendanceSerializer


class AttendanceListCreateView(generics.ListCreateAPIView):
    """
    Attendance list create view  to serializer list and create attendace for employee.
    """    
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
