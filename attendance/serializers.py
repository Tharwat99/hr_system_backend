from rest_framework import serializers
from . models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    """
    employee serializer to serializer account data.
    """    
    class Meta:
        model = Attendance
        fields = ('employee', 'date', 'present')