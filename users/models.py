from unicodedata import name
from django.db import models

# # Create your models here.
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# class CustomUser(AbstractUser):
#     # Any extra fields would go here
#     def __str__(self):
#         return self.email
class Item(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
