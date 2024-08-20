"""
views for the employee app
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

class EmployeesIndex(View):
    """
    CBV for employees index
    """
    def get(self, request, employee_id):
        """
        employees index handler for GET
        """
        return HttpResponse("Usman" + employee_id)