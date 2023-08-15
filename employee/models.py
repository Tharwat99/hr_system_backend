from django.db import models
from django.contrib.auth.models import AbstractUser
from . manager import EmployeeManager

class Employee(AbstractUser):
    """
    Employee model extends abstract user.
    extend user model for create acount model.
    """
    hr_employee = 0
    normal_employee = 1
    
    ROLE_CHOICES = (
          (hr_employee, 'hr'),
          (normal_employee, 'normal'),
    )
    email = models.EmailField(unique=True)
    group =  models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=False, null=False, default= normal_employee)
    groups = None
    user_permissions = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = EmployeeManager()
    
    class Meta:
        db_table = "Employee"
