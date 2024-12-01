from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    role = models.CharField(default='user', max_length=100)
    status = models.CharField(default='active', max_length=100)
