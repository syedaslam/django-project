from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=50)
    disc = models.CharField(max_length=50)
    summary = models.TextField()

    def __str__(self):
        return self.name