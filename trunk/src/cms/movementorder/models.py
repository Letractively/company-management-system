from django.db import models

# Create your models here.
class MovementOrder(models.Model):
    zero8 = models.ForeignKey(Zero8)
    organization = models.CharField(max_length=30)
    movementOrderCode = models.CharField(max_length=7)
    departDate = models.DateField()
    returnDate = models.DateField()
    adminNote = models.CharField(max_length=90)
    
class MOParticipant(models.Model):
    MO = models.ForeignKey(MovementOrder)
    mid = models.ForeignKey("mid.Mid")