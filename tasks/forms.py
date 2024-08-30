from django.forms import ModelForm
from tasks.models import Task

class TaskForm(ModelForm):
    """
    TaskForm class
    """
    class Meta:
        """
        TaskForm meta class
        """
        model = Task
        fields = ['title', 'description', 'status', 'assigned_to']
    