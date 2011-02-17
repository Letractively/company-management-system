#weekends models.py
# Author: Michael Harrison
# Editor: Michael Laws

from django.db import models

# Create your models here.
STATUS_CHOICES = (
                  ('P','Pending'),
                  ('A','Approved'),
                  ('D','Disapproved'),
                  )

class Weekend(models.Model):
    mid = models.ForeignKey("mid.Mid")
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)
    location = models.CharField(max_length=40)
    contactNumber = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.mid + " - " + self.Startdate