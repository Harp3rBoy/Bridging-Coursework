from django.db import models
from django.utils import timezone


class Item(models.Model):
    text = models.TextField(default='')


class PersonalDetails(models.Model):
    name = models.CharField(default='', max_length=100)
    dob = models.DateField(default=timezone.now)
    email = models.CharField(default='', max_length=100)
