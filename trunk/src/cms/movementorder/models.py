#movementorder models.py
# Author: Michael Harrison
from django.db import models

class MovementOrder(models.Model):
    organization = models.CharField(max_length=30)
    movementOrderCode = models.CharField(max_length=7)
    departDate = models.DateField()
    returnDateProjected = models.DateField()
    returnDate = models.DateField(null=True,blank=True)
    adminNote = models.CharField(max_length=90)
    
class MOParticipant(models.Model):
    MO = models.ForeignKey(MovementOrder)
    participant = models.ForeignKey("mid.Mid")