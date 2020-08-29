from django.db import models
from django.utils import timezone


class PersonalDetails(models.Model):
    name = models.CharField(default='', max_length=100)
    dob = models.DateField(default=timezone.now)
    email = models.CharField(default='', max_length=100)

class Education(models.Model):
    institution = models.CharField(default='', max_length=100)
    grades = models.TextField(default='')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
