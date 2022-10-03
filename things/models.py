from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Thing(models.Model):
    name =models.CharField(max_length = 30, unique = True)
    description =models.CharField(max_length = 120, unique = False)
    quantity = models.IntegerField()
