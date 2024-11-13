from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100)
    code = models.CharField(max_length=100, unique=True)
    