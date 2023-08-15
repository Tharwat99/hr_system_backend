from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from . models import Employee

class EmployeeLoginViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.super_user = Employee.objects.create_superuser(username='hruser', email = 'hruser@email.com', password='hruserpassword')
        
    def test_employee_login(self):
        url = reverse('login-employee')
        data = {
            'email': 'hruser@email.com',
            'password': 'hruserpassword'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # TODO Add assertions to check the response data and token generation

class EmployeeListCreateViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Employee.objects.create_user(username='testuser', email = 'test@email.com', password='testpassword')
        self.super_user = Employee.objects.create_superuser(username='hruser', email = 'hruser@email.com', password='hruserpassword')
        self.token = self.get_token()

    def get_token(self):
        refresh = RefreshToken.for_user(self.super_user)
        return str(refresh.access_token)

    def test_employee_list_view(self):
        url = reverse('list-create-employee')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # TODO Add assertions to check the response data and permissions
    
    def test_employee_create_view(self):
        url = reverse('list-create-employee')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        data = {
            'username':'test1',
            'email': 'test1@email.com',
            'password': 'test1password'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Add TODO assertions to check the response data and permissions

class EmployeeDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = Employee.objects.create_user(username='testuser', email = 'test@email.com', password='testpassword')
        self.super_user = Employee.objects.create_superuser(username='hruser', email = 'hruser@email.com', password='hruserpassword')
        self.token = self.get_token()

    def get_token(self):
        refresh = RefreshToken.for_user(self.super_user)
        return str(refresh.access_token)

    def test_employee_detail_view(self):
        url = reverse('details-employee', args=['testuser'])
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # TODO Add assertions to check the response data and permissions