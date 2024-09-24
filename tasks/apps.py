from django.apps import AppConfig
from django.core.signals import request_finished, request_started
from django.core.handlers.wsgi import WSGIHandler
from django.dispatch import receiver

class TasksConfig(AppConfig):
    """
    Configuration for the tasks app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        request_started.connect(request_started_handler, sender=WSGIHandler)

def request_started_handler(sender, **kwargs):
    """
    Request Started Handler
    """
    print(".............Request Started.............")

@receiver(request_finished, sender=WSGIHandler)
def request_finished_handler(sender, **kwargs):
    """
    Request Finished Handler
    """
    print(".............Request Finished.............")