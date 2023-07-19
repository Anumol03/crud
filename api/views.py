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


# class EmployeeView(ModelViewSet):
#     serializer_class=EmployeeSerializer
#     model=Employee
#     queryset=Employee.objects.all()
#     http_method_names=['get','post']
#     def list(self, request, *args, **kwargs):
#         try:
#             courses = self.get_queryset()
#             total_results = courses.count()

#             if total_results == 0:
#                 # If there are no courses, set the status as "error"
#                 response_data = {
#                     "status": "error",
#                     "error_message": "No courses found.",
#                     "totalResults": total_results
#                 }
#             else:
#                 # If there are courses, set the status as "ok"
#                 serialized_courses = self.serializer_class(courses, many=True)
#                 response_data = {
#                     "status": "ok",
#                     "courses": serialized_courses.data,
#                     "totalResults": total_results
#                 }
#         except Exception as e:
#             # If there is an exception, set the status as "error" and print the error message
#             response_data = {
#                 "status": "error",
#                 "error_message": str(e),
#                 "totalResults": total_results
#             }
        
#         return Response(response_data)
    
class AddEmployeeView(GenericViewSet,CreateModelMixin,ListModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
    queryset = AddEmployee.objects.all()
    serializer_class = AddEmployeeSerializer
    http_method_names=['get','post','put','delete']
    def list(self, request, *args, **kwargs):
        try:
            employees = self.get_queryset()
            total_results = employees.count()

            if total_results == 0:
                
                response_data = {
                    "status": "error",
                    "error_message": "No employee found.",
                    "totalResults": total_results
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
from django.http import JsonResponse

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

    return JsonResponse(response_data)
