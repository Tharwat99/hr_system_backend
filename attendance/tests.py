from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from . models import Employee

class AttendanceListCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Employee.objects.create_user(username='testuser', email = 'test@email.com', password='testpassword')
        self.super_user = Employee.objects.create_superuser(username='hruser', email = 'hruser@email.com', password='hruserpassword')
        self.token = self.get_token()

    def get_token(self):
        refresh = RefreshToken.for_user(self.super_user)
        return str(refresh.access_token)

    def test_attendance_list_view(self):
        url = reverse('list-create-attendance')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # TODO Add assertions to check the response data and permissions
    
    def test_attendance_create_view(self):
        url = reverse('list-create-attendance')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        data= {
            'employee':self.user.id,
            'date': datetime.now().date()
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # TODO Add assertions to check the response data and permissions