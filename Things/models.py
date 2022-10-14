from django.db import models
from django.core import validators

# Create your models here.
class Thing(models.Model):
    name = models.CharField(
        unique = True, max_length = 30
    )

    description = models.TextField(
        max_length = 120, blank = True
    )

    quantity = models.IntegerField(
        validators = [validators.MinValueValidator(0), validators.MaxValueValidator(100)]
    )
