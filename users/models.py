from django.db import models
from django.contrib.auth.models import User

from .choices import CITIES


class MyUser(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False)
    photo = models.ImageField(
        upload_to="users/images", default=None, null=True, blank=True)
    city = models.CharField(
        max_length=64, choices=CITIES, default=None, null=True, blank=True)
