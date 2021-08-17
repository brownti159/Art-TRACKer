from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    art_interest = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30,  blank=True)
    artist = models.BooleanField(blank=True)
