import logging
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from base_model import BaseModel

logger = logging.getLogger("finances")

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
    attachment = models.FileField(upload_to="tasks", blank=True, null=True)

@receiver(post_delete, sender=Task)
def task_post_delete(sender, instance, **kwargs):
    """
    Request Started Handler
    """
    print("TASK DELETED..............")
    # logger.debug("Task deleted %s %s ", sender, kwargs)

# @receiver(pre_save, sender=Task)
# def task_pre_save(sender, **kwargs):
#     """
#     Request Started Handler
#     """
#     print("TASK Saved..............")
#     print(sender)
#     print(kwargs)
    # logger.debug("Task deleted %s %s ", sender, kwargs)