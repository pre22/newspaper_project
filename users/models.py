from django.db import models
from django.contrib.auth.models import AbstractUser


# null is database-related while blank is validation-related
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)