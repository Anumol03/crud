from django.http import HttpResponse
from django.shortcuts import render,redirect
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework import authentication,permissions
from api.models import Employee,AddEmployee
from api.serializers import EmployeeSerializer,AddEmployeeSerializer
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
class AddEmployeeView(GenericViewSet, CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin):
    queryset = AddEmployee.objects.all()
    serializer_class = AddEmployeeSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            response_data = {
                "status": "ok",
                "message": "Employee created successfully.",
                "data": serializer.data,
            }
            return Response(response_data)

        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e),
            }
            return Response(response_data)

    def list(self, request, *args, **kwargs):
        try:
            employees = self.get_queryset()
            total_results = employees.count()

            if total_results == 0:
                response_data = {
                    "status": "ok",
                    "employees": [],
                    "totalResults": 0
                }
            else:
                serialized_employees = self.serializer_class(employees, many=True)
                response_data = {
                    "status": "ok",
                    "employees": serialized_employees.data,
                    "totalResults": total_results
                }
        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e),
                "totalResults": total_results
            }

        return Response(response_data)

    

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            response_data = {
                "status": "ok",
                "message": "Employee deleted successfully.",
            }
            return Response(response_data)

        except ObjectDoesNotExist:
         
            try:
                instance = self.get_object()
            except ObjectDoesNotExist:
               
                response_data = {
                    "status": "error",
                    "error_message": "Employee not found or already deleted.",
                }
                return Response(response_data)

        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e),
            }
            return Response(response_data)
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            response_data = {
                "status": "ok",
                "message": "Employee updated successfully.",
                "data": serializer.data,
            }
            return Response(response_data)

        except Exception as e:
            response_data = {
                "status": "error",
                "error_message": str(e),
            }
            return Response(response_data)
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            response_data = {
                "status": "ok",
                "data": serializer.data,
            }
            return Response(response_data, status=200)  

        except Exception as e:
            response_data = {
                "status": "ok",
                "error_message": "data already deleted",
            }
            return Response(response_data)

def clear_all_employees(request):
    try:
        AddEmployee.objects.all().delete()

        response_data = {
            "status": "ok",
            "message": "All employee data cleared successfully."
        }
    except Exception as e:
        response_data = {
            "status": "error",
            "error_message": str(e)
        }
        return Response(response_data)
