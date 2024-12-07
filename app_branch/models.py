from django.db import models
from django.contrib.auth import get_user_model

from app_common.models import BaseModel
from app_company.models import RestaurantModel

User = get_user_model()


class BranchModel(BaseModel):
    """
    Represents a branch of a restaurant.
    Attributes:
        name (str): Name of the branch unique.
        address (str): Address of the branch.
        phone_number (str): Phone number of the branch.
        longitude (float): Longitude of location of the branch.
        latitude (float): Latitude of location of the branch.
        manager (User): Manager of the branch.
        restaurant (RestaurantModel): Restaurant the branch belongs to.
        is_active (bool): Indicates whether the branch is active or not.
    """
    name = models.CharField(max_length=64, verbose_name="Name", unique=True)
    address = models.CharField(max_length=255, verbose_name="Address")
    phone_number = models.CharField(max_length=255, verbose_name="Phone Number")
    longitude = models.FloatField()
    latitude = models.FloatField()
    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="branches",
        verbose_name="Manager"
    )
    restaurant = models.ForeignKey(
        RestaurantModel,
        on_delete=models.CASCADE,
        related_name="branches",
        verbose_name="Restaurant"
    )
    is_active = models.BooleanField(default=True, verbose_name="Is Active")

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.name
