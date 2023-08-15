from rest_framework import serializers
from . models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    """
    employee serializer to serializer account data.
    """    
    class Meta:
        model = Attendance
        fields = ('employee', 'date', 'present')

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)


class AttendanceDetailSerializer(serializers.ModelSerializer):
    """
    employee serializer to serializer account data.
    """    
    class Meta:
        model = Attendance
        fields = ('date', 'present')