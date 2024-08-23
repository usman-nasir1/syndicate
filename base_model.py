from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from nanoid import generate


def generate_nanoid():
    """
    Generate nano id
    using lambda function as the default value causes following:
    ValueError: Cannot serialize function: lambda
    """
    return generate(size=20)
class BaseModel(models.Model):
    """
    Base Model. It is used to manage the common fields for all models
    """
    id = models.CharField(primary_key=True, default=generate_nanoid, editable=False, max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_modified_by')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_created_by')

    class Meta:
        """
        Meta class so that Django does not create table for this model
        """
        abstract = True