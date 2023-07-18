from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Employee,AddEmployee

class EmployeeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Employee
        fields=["id","user","password","mobile_no"]

class AddEmployeeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=AddEmployee
        fields="__all__"