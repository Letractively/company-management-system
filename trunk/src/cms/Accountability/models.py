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
   DateTime = models.DateTimeField() 
   Type = models.CharField(max_length=3, choices=EVENT_TYPE_CHOICES)
   Location = models.CharField(max_length=30)
   def __unicode_(self):
        return Type + " - " + DateTime + " - "+ Location
    
class Attendance(models.Model):
    Event = models.ForeignKey(Event) 
    Mid = models.ForeignKey("MID.Mid")
    Status = models.CharField(max_length=1, choices=ATTEND_STATUS_CHOICES)
    Comment = models.TextField()
    Temp_Status = models.CharField(max_length=1, choices=ATTEND_STATUS_CHOICES)
    def __unicode_(self):
        return Mid + " - " + Event 
