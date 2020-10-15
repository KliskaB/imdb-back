from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    verification_code = models.TextField(max_length=4, blank=False)
    is_verified = models.BooleanField(default=False)
    profile_picture = models.TextField(blank=True)
