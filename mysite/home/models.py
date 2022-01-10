from django.db import models

# Create your models here.


class Groups(models.Model):
    name = models.CharField(max_length=100)
    personList = models.CharField(max_length=100)
