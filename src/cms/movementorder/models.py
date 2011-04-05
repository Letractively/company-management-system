#movementorder models.py
# Author: Michael Harrison
from django.db import models

class MovementOrder(models.Model):
    organization = models.CharField(max_length=30)
    movementOrderCode = models.CharField(max_length=7,primary_key=True)
    departDate = models.DateTimeField(null=True,blank=True)
    returnDateProjected = models.DateTimeField(null=True,blank=True)
    returnDate = models.DateTimeField(null=True,blank=True)
    adminNote = models.CharField(max_length=90)
    
    def __unicode__(self):
        return u'%s - %s %s' % (self.movementOrderCode,self.organization,self.departDate)
        
class MOParticipant(models.Model):
    MO = models.ForeignKey(MovementOrder)
    participant = models.ForeignKey("mid.Mid")
    
    def __unicode__(self):
        return u'%s %s' % (self.MO.movementOrderCode,self.participant.LName)