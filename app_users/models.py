from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    """
    UserModel is a custom user model that extends the AbstractUser model provided by Django.
    It has additional fields such as role, status, phone_number, first_name, and last_name.
    The role field is a CharField with choices to specify the user's role in the system.
    The status field is a CharField to specify the user's status in the system.
    The phone_number field is a CharField to store the user's phone number.
    The first_name and last_name fields are CharFields to store the user's first and last names.
    """

    # choices for role
    CHOOSE_ROLE = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('restaurant', 'Restaurant'),
        ('delivery', 'Delivery'),
    )

    # choices for status
    CHOOSE_STATUS = (
        ('active', 'Active'),
        ('delete', 'Delete'),
        ('inactive', 'Inactive'),
    )
    # fields
    role = models.CharField(default='user', max_length=100, choices=CHOOSE_ROLE)
    status = models.CharField(default='active', max_length=100, choices=CHOOSE_STATUS)
    phone_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
