from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from app_common.models import BaseModel

User = get_user_model()


class CourierModel(BaseModel):
    """
    Courier model represents a courier in the application.
    field name for unique
    """
    name = models.CharField(max_length=64, verbose_name=_("Name"), unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="couriers",
        verbose_name=_("User")
    )

    class Meta:
        verbose_name = _("Courier")
        verbose_name_plural = _("Couriers")

    def __str__(self):
        return self.name