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

class BaseModelManager(models.Manager):
    """
    Base Model Manager.
    """
    def get_queryset(self):
        """
        Return a new QuerySet object after filtering the soft deleted objects.
        """
        return super().get_queryset().filter(is_deleted=False)
class BaseModel(models.Model):
    """
    Base Model. It is used to manage the common fields for all models
    """
    id = models.CharField(primary_key=True, default=generate_nanoid, editable=False, max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False, editable=False)
    # TODO Set editable to False so that modified_by and created_by are populated automatically with logged in user
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_modified_by', editable=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_created_by', editable=True)
    # Use the custom manager when Model.objects is used e.g. Model.objects.all()
    objects = BaseModelManager()

    def delete(self, using=None, keep_parents=False, hard_delete = False):
        if hard_delete:
            super().delete(using=using, keep_parents=keep_parents)
        else:
            self.is_deleted = True
            self.save(using=using)

    class Meta:
        """
        Meta class so that Django does not create table for this model
        """
        abstract = True