from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name=models.CharField(max_length=200)
    bio=models.TextField(null=True)
    avatar=models.ImageField(default='avatar.svg',null=True)
    email=models.EmailField(unique=True,null=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']



