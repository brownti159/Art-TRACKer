from django.db import models
from django.db.models.fields import DecimalField, IntegerField, TextField, URLField
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Work(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    creators = models.ManyToManyField(Artist, related_name="works")
    year = models.IntegerField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # artistStatement = soundbyte?
    photo = models.ImageField
    artistWebsite = models.URLField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    wheelchairAccessible = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.title