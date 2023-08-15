from rest_framework import serializers, exceptions
from .models import Employee
from django.contrib.auth import authenticate
from attendance.serializers import AttendanceDetailSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    """
    employee serializer to serializer account data.
    """    
    attendances = AttendanceDetailSerializer(many = True)
    class Meta:
        model = Employee
        fields = ('id', 'email', 'username', 'group', 'attendances')
        read_only_fields = ['id']

class EmployeeLoginSerializer(serializers.ModelSerializer):
    """
    employee login serializer.
    """  
    email = serializers.EmailField(required = True)
    password = serializers.CharField(write_only = True)
    class Meta:
        model = Employee
        fields = ('email', 'password')
    
    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active and user.group == 0:
            data['user'] = user
        else:
            raise exceptions.AuthenticationFailed('Unable to log in with provided credentials.')
        return data
