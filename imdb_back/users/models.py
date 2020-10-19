from django.db import models
from django.contrib.auth.models import AbstractUser
import os


class User(AbstractUser):
    verification_code = models.CharField(max_length=4, blank=False)
    is_verified = models.BooleanField(default=False)
    profile_picture = models.FileField(blank=True, null=True, upload_to='profile_pictures/')
