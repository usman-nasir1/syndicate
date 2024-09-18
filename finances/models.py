import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from base_model import BaseModel

class Salary(BaseModel):
    """
    Salary Model. It is used to manage the Salaries of the employees and salary revisions
    """
    id = models.AutoField(_("Salary id"), primary_key=True)
    # employee_id
    # When user is deleted, DO_NOTHING. Other options are models.PROTECT, models.SET_NULL, models.SET_DEFAULT, models.CASCADE
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='salary')
    gross_salary = models.FloatField(_("Gross Salary"), default=0.0)
    updated_to = models.ForeignKey('self', null=True, blank=True, on_delete=models.DO_NOTHING,related_name='updated_from')
    is_active = models.BooleanField(default=True)
    effective_from = models.DateField(default=datetime.date.today)
