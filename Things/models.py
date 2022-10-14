from django.db import models
from django.core import validators

# Create your models here.
class Thing(models.Model):
    name = models.SlugField(unique=True,validators=[validators.MinLengthValidator(1), validators.MaxLengthValidator(30)])
    description = models.TextField(blank=True, validators=[validators.MaxLengthValidator(120)])
    quantity = models.IntegerField(validators=[validators.MinValueValidator(0), validators.MaxValueValidator(100)])

    # name = models.SlugField(
    #     unique = True, max_length = 30, blank = False
    # )
    #
    # description = models.TextField(
    #     max_length = 120, blank = True
    # )
    #
    # quantity = models.IntegerField(
    #     validators = [validators.MinValueValidator(0), validators.MaxValueValidator(100)]
    # )
