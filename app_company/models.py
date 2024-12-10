from django.db import models
from django.contrib.auth import get_user_model

from app_common.models import BaseModel

User = get_user_model()


class RestaurantModel(BaseModel):
    """
    Represents a restaurant in the system.
    Attributes:
        name (str): The name of the restaurant unique.
        manager (User): The manager of the restaurant.
        phone_number (str): The phone number of the restaurant.
        logo (ImageField): The logo of the restaurant.
        is_active (bool): Indicates whether the restaurant is active or not.
    """
    name = models.CharField(max_length=100, verbose_name='Name', unique=True)
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="restaurants",
        verbose_name='Manager'
    )
    phone_number = models.CharField(max_length=20, verbose_name='Phone Number')
    logo = models.ImageField(upload_to="restaurant_logos/", verbose_name='Logo')
    is_active = models.BooleanField(default=True, verbose_name='Is Active')

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

    def __str_(self):
        return self.name
