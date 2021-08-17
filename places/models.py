from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
