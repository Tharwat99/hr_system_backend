from rest_framework import serializers
from . models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    """
    Attendance serializer to serializer create attendace for employee.
    """    
    class Meta:
        model = Attendance
        fields = ('employee', 'date', 'present')


class AttendanceDetailSerializer(serializers.ModelSerializer):
    """
    Attendance serializer to serializer detaial attendace data for employee.
    """    
    class Meta:
        model = Attendance
        fields = ('date', 'present')