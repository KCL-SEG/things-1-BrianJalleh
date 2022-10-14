from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Thing(AbstractUser):
    name = models.CharField(
        max_length = 50, blank = False
    )

    description = models.CharField(
        max_length = 520, blank = False
    )

    quantity = models.IntegerField()
