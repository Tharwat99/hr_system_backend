from django.db import models
from employee.models import Employee

class Attendance(models.Model):
    """
    Attendance model linked with Employee model.
    """
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField(unique=True)
    present = models.BooleanField(default=True)