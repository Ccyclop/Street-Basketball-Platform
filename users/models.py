from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users',default='users/default-user-avatar.png', blank=True)

# TODO Registration/Authentication 