from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    role = models.CharField(default='user', max_length=100)
    status = models.CharField(default='active', max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
