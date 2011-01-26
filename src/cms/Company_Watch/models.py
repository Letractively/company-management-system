from django.db import models

# Create your models here.
WATCHBILL_TYPE_CHOICES = (
                          ('W','Work day'),
                          ('H','Holiday'),
                          )

WATCH_TYPE_CHOICES = (
                      ('CMDO','Company Mate of the Deck'),
                      ('ACDO','Asistant Company Duty Officer'),
                      ('CDO','Company Duty Officer'),
                      )

class WatchBill(models.Model):
    Date = models.DateField()
    Type = models.CharField(max_length=1, choices=WATCHBILL_TYPE_CHOICES)
    
class Watch(models.Model):
    WatchBill = models.ForeignKey(WatchBill)
    Mid = models.ForeignKey("MID.Mid")
    Post = models.CharField(max_length=20)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Type = models.CharField(max_length=4,choices=WATCH_TYPE_CHOICES)
