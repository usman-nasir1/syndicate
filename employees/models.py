from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from base_model import BaseModel

class Employee(BaseModel):
    """
    Employee Model
    """
    EMPLOYEE_GROUPS = {
        "exec" : "Executive",
        "tech" : "Technical",
        "staff" : "Office Staff",
        "marketing" : "Marketing",
        "sales" : "Sales"
    }
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=20)
    address_street = models.TextField(max_length=100)
    address_city = models.TextField(max_length=20)
    # Pakistani ID card has 13 chars
    cnic = models.CharField(_("CNIC"),max_length=13)
    emp_group = models.CharField(max_length=10, choices=EMPLOYEE_GROUPS)
    joining_date = models.DateTimeField(default=datetime.now)
    resignation_date = models.DateTimeField(null=True, blank=True)

    @property
    def full_address(self):
        """
        Get full address
        """
        return f"{self.address_street} {self.address_city}"

    class Meta(BaseModel.Meta):
        """
        Meta class
        """
        db_table = 'employees'
