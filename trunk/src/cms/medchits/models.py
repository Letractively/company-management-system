#medchits models.py
# Author: Michael Harrison
# Editor: Michael Laws
# Editor: Dimitri Hatley

from django.db import models

DISPOSITION_CHOICES = (
                           ("SIQ","SIQ"),
                           ("CLA","SIQ with Class Option"),
                           ("LLD","Light/Limited Duty"),
                           )

# Create your models here.
class Chit(models.Model):
    mid = models.ForeignKey("mid.Mid")
    diagnosis = models.TextField()
    startDate = models.DateField('Start Date')
    endDate = models.DateField('End Date')
    disposition = models.CharField(max_length=3, choices=DISPOSITION_CHOICES)
    adminNotes = models.TextField()
    
    def __unicode__(self):
        return self.mid.LName + " - " + self.diagnosis + "(" + unicode(self.startDate) + " - " + unicode(self.endDate) + ")"