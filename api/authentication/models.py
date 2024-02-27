from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
class Users(AbstractUser):
    password=models.CharField(max_length=255)
    role=models.CharField(max_length=255)

    



