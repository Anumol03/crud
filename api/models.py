from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    mobile_no=models.CharField(max_length=10)
    def __str__(self) :
        return self.user
class AddEmployee(models.Model):
    employee_name=models.CharField(max_length=200)
    designation=models.CharField(max_length=200)
    def __str__(self):
        return self.employee_name
