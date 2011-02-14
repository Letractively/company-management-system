#accountability models.py
# Author: Michael Harrison

from django.db import models

# Create your models here.
EVENT_TYPE_CHOICES = (
                     ('MMF','Morning Meal'),
                     ('NMF','Noon Meal Formation'),
                     ('EMF','Evening Meal Formation'),
                     ('TAP','TAPS'),
                     ('FOR','Forrestal Lecture'),
                     ('DRL','Drill'),
                     ('CAL','Officers Call'),
                     ('OTH','Other Special Event'),
                    )

ATTEND_STATUS_CHOICES = (
                         ('P','Present'),
                         ('A','Absent'),
                         ('U','Unauthorized Absent'),
                         ('E','Excused'),
                         )
class Event(models.Model):
   dateTime = models.DateTimeField('Event Date and Time') 
   type = models.CharField(max_length=3, choices=EVENT_TYPE_CHOICES)
   location = models.CharField(max_length=30)
   def __unicode_(self):
        return type + " - " + dateTime + " - "+ location
    
class Attendance(models.Model):
    event = models.ForeignKey(Event) 
    mid = models.ForeignKey("mid.Mid")
    status = models.CharField(max_length=1, choices=ATTEND_STATUS_CHOICES,null=True)
    comment = models.TextField(null=True)
    tempStatus = models.CharField(max_length=1, choices=ATTEND_STATUS_CHOICES,null=True)
    def __unicode__(self):
        return self.mid + " - " + self.event 
