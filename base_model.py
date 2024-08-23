from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from nanoid import generate

class BaseModel(models.Model):
    """
    Base Model. It is used to manage the common fields for all models
    """
    id = models.CharField(primary_key=True, default=lambda: generate(size=20), editable=False, max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='modified_by')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_by')

    class Meta:
        """
        Meta class so that Django does not create table for this model
        """
        abstract = True