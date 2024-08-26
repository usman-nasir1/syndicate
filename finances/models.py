import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from base_model import BaseModel
from employees.models import Employee

class FinanceBase(BaseModel):
    """Base Model for all the models related to finance"""
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, related_name='%(class)s_salary')
    # When user is deleted, DO_NOTHING. Other options are models.PROTECT, models.SET_NULL, models.SET_DEFAULT, models.CASCADE
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_salary', null=True, blank=True)
    updated_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING,related_name='updated_from')
    is_active = models.BooleanField(default=True)
    effective_from = models.DateField(default=datetime.date.today)

    class Meta(BaseModel.Meta):
        """
        Meta class for FinanceBase
        """
        abstract = True


class Salary(FinanceBase):
    """
    Salary Model. It is used to manage the Salaries of the employees and salary revisions
    """
    gross_salary = models.FloatField(_("Gross Salary"), default=0.0)
    

    class Meta(BaseModel.Meta):
        """
        Meta class for Salary Model
        """
        db_table = "salaries"

class Benefit(FinanceBase):
    """
    Benefits Model
    """
    CATEGORY_CHOICES = {
        "travel" : "Travel",
        "residence" : "Residence",
        "food" : "Food",
        "vending_machine" : "Vending Machine",
        "telecom" : "Telecom Balance",
        "insurance" : "Insurance"
    }
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True)
    benefit_amount = models.FloatField(_("Benefit Amount"), default=0, null=True)


    class Meta(BaseModel.Meta):
        """
        Meta class for Benefit Model
        """
        db_table = "benefits"