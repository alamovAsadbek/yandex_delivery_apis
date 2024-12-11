from django.db import models


class BaseModel(models.Model):
    """
    BaseModel is an abstract model that contains common fields for all models.
    It has fields for created_at, updated_at, and is_deleted.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
