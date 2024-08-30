from django.db import models
from django.contrib.auth.models import User
from base_model import BaseModel

class Task(BaseModel):
    """
    Task Model
    """
    STATUS_CHOICES = {
        "pending" : "Pending",
        "awaiting_assignment" : "Awaiting Assignment",
        "in_progress" : "In Progress",
        "done" : "Done",
        "closed" : "Closed",
    }
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
