#movementorder models.py
# Author: Michael Harrison
from django.db import models

class MovementOrder(models.Model):
    organization = models.CharField(max_length=30)
    movementOrderCode = models.CharField(max_length=7)
    departDate = models.DateTimeField()
    returnDateProjected = models.DateTimeField()
    returnDate = models.DateTimeField(null=True,blank=True)
    adminNote = models.CharField(max_length=90)
    
class MOParticipant(models.Model):
    MO = models.ForeignKey(MovementOrder)
    mid = models.ForeignKey("mid.Mid")