from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from app_common.models import BaseModel

User = get_user_model()


class RestaurantModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="restaurants",
        verbose_name=_('Manager')
    )
    phone_number = models.CharField(max_length=20, verbose_name=_('Phone Number'))
    logo = models.ImageField(upload_to="restaurant_logos/", verbose_name=_('Logo'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    class Meta:
        verbose_name = _("Restaurant")
        verbose_name_plural = _("Restaurants")

    def __str__(self):
        return self.name
