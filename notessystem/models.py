from django.db import models

# Create your models here.
class add(models.Model):
    Date=models.CharField(max_length=12)
    Note=models.CharField(max_length=100)