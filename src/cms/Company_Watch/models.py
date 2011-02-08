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
    date = models.DateField('Watchbill Date')
    type = models.CharField(max_length=1, choices=WATCHBILL_TYPE_CHOICES)
    def __unicode_(self):
        return type + " - " + date
    
class Watch(models.Model):
    watchBill = models.ForeignKey(WatchBill)
    mid = models.ForeignKey("MID.Mid")
    post = models.CharField(max_length=20)
    startTime = models.TimeField()
    endTime = models.TimeField()
    type = models.CharField(max_length=4,choices=WATCH_TYPE_CHOICES)
    def __unicode__(self):
        return self.Mid + " - " + self.WatchBill
