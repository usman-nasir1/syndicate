"""
views for the employee app
"""
# from django.shortcuts import render
import logging
from django.http import HttpResponse
from django.views import View

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

class EmployeesIndex(View):
    """
    CBV for employees index
    """
    def get(self, request, employee_id):
        """
        employees index handler for GET
        """
        logger.debug(type(request))
        return HttpResponse("Usman" + employee_id)