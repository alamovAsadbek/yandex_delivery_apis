from django.db import models
from django.contrib.auth import get_user_model

from app_common.models import BaseModel

User = get_user_model()


class RestaurantModel(BaseModel):
    """
    Represents a restaurant in the system.
    Attributes:
        name (str): The name of the restaurant unique.
        logo (ImageField): The logo of the restaurant.
        is_active (bool): Indicates whether the restaurant is active or not.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="branch", null=True)
    name = models.CharField(max_length=100, verbose_name='Name', unique=True)
    logo = models.ImageField(upload_to="restaurant_logos/", verbose_name='Logo')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

    def __str_(self):
        return self.name
