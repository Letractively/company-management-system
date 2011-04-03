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
                         ('M','MO'),
                         ('W','Weekend'),
                         )
CO_CHOICES = (
              ('1','1st Company'),
              ('2','2nd Company'),
              ('3','3rd Company'),
              ('4','4th Company'),
              ('5','5th Company'),
              ('6','6th Company'),
              ('7','7th Company'),
              ('8','8th Company'),
              ('9','9th Company'),
              ('10','10th Company'),
              ('11','11th Company'),
              ('12','12th Company'),
              ('13','13th Company'),
              ('14','14th Company'),
              ('15','15th Company'),
              ('16','16th Company'),
              ('17','17th Company'),
              ('18','18th Company'),
              ('19','19th Company'),
              ('20','20th Company'),
              ('21','21st Company'),
              ('22','22nd Company'),
              ('23','23rd Company'),
              ('24','24th Company'),
              ('25','25th Company'),
              ('26','26th Company'),
              ('27','27th Company'),
              ('28','28th Company'),
              ('29','29th Company'),
              ('30','30th Company'),              
              )
class Event(models.Model):
   dateTime = models.DateTimeField('Event Date and Time') 
   type = models.CharField(max_length=3, choices=EVENT_TYPE_CHOICES)
   location = models.CharField(max_length=30)
   company = models.CharField(max_length=2,choices=CO_CHOICES)
   platoonOneSubmitted = models.NullBooleanField()
   platoonTwoSubmitted = models.NullBooleanField()
   platoonThreeSubmitted = models.NullBooleanField()
   platoonFourSubmitted = models.NullBooleanField()
   companyComplete = models.NullBooleanField()
   def __unicode_(self):
        return u'%s at %s: %s' %(self.type,self.dateTime,self.location)
    
class Attendance(models.Model):
    event = models.ForeignKey(Event) 
    mid = models.ForeignKey("mid.Mid")
    status = models.CharField(max_length=1, choices=ATTEND_STATUS_CHOICES,null=True)
    comment = models.TextField(null=True)
    tempStatus = models.CharField(max_length=1, choices=ATTEND_STATUS_CHOICES,null=True)
    def __unicode__(self):
        return u'%s %s from: %s at %s' % (self.mid.LName,self.status,self.event.type,self.event.location)
    
class Absence(models.Model):
    zero8 = models.ForeignKey("zero8.Zero8")
    name = models.ForeignKey('mid.Mid')
    authorized = models.NullBooleanField()
    description = models.CharField(max_length=20)
    adminNote = models.CharField(max_length=90)
    REASON_CHOICES = (
                     ('AA','Authorized Absence'),
                     ('UA','Unauthorized Absence'),
                     ('WE','Weekend'),
                     ('MO','Movement Order'),
                     )
    reason = models.CharField(max_length=2,choices=REASON_CHOICES) 
