from django.db import models

# Create your models here.

class Weekend(models.Model):
    mid = models.ForeignKey("MID.Mid")
    Startdate = models.DateField()
    Enddate = models.DateField()
    Location = models.CharField(max_length=40)
    ContactNumber = models.CharField(max_length=10)