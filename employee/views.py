from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from employee.models import Employee


from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework import generics, permissions
from .serializers import EmployeeLoginSerializer, EmployeeSerializer

from rest_framework.response import Response

class EmployeeLoginView(generics.GenericAPIView):
    """
    Employee Login View
    """
    serializer_class = EmployeeLoginSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            
            refresh = RefreshToken.for_user(user)
            return Response({  
                'user':EmployeeSerializer(user).data, 
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def logout_view(request):
    logout(request)
    return redirect('login')

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.filter(group = Employee.normal_employee).all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'username'


