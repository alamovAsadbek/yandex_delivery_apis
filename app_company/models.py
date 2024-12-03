from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from app_common.models import BaseModel

User = get_user_model()


class RestaurantModel(BaseModel):
    name = models.CharField(max_length=100)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="restaurants")
    phone_number = models.CharField(max_length=20)
    logo = models.ImageField(upload_to="restaurant_logos/")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Restaurant")
        verbose_name_plural = _("Restaurants")

    def __str__(self):
        return self.name
