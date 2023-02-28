from django.db import models
class Movie(models.Model):
        name = models.CharField()
        year = models.IntegerField()
        descriptiom = models.TextField()