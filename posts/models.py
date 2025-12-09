from django.db import models

# Create your models here.

class Post(models.Model):
    tiltle = models.CharField(max_length=75)
    body
    slug
    date