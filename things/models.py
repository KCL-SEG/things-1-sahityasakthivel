from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Thing():
    name =models.CharField(max_length = 30, unique = True)
    description =models.CharField(max_length = 120, unique = False)
    quantity = models.IntegerField()
