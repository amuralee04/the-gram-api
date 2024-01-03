from django.db import models
from django.contrib.auth.models import AbstractUser
from app.manager import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=16)

    is_staff = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()