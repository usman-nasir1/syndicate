"""
urls for the employees app
"""
from django.urls import path
from employees.views import EmployeesIndex

urlpatterns = [
    path('<employee_id>', EmployeesIndex.as_view()),
]
