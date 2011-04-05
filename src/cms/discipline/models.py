#orm models.py
# Author: Michael Harrison

from django.db import models

 
class Restriction(models.Model):
    mid = models.ForeignKey('mid.Mid')
    conductHonor = models.BooleanField()
    dateOffence = models.DateField()
    startDate = models.DateField()
    daysAwarded = models.IntegerField()
    daysRemaining = models.IntegerField()
    adminNotes = models.CharField(max_length=90)
    checked = models.DateField()
    
class Tours(models.Model):
    mid = models.ForeignKey('mid.Mid')
    conductHonor = models.BooleanField()
    dateOffence = models.DateField()
    startDate = models.DateField()
    toursAwarded = models.IntegerField()
    toursRemaining = models.IntegerField()
    adminNotes = models.CharField(max_length=90)
    
class Separation(models.Model):
    zero8 = models.ForeignKey("zero8.Zero8")
    mid = models.ForeignKey('mid.Mid')
    pending = models.BooleanField()
    adminNote = models.CharField(max_length=90)
    
class Probation(models.Model):
    mid = models.ForeignKey('mid.Mid')
    startDate = models.DateField()
    daysAwarded = models.IntegerField()
    description = models.CharField(max_length=50)