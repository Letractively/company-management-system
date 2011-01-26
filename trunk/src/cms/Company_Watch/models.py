from django.db import models

# Create your models here.

class WatchBill(models.Model):
    Date = models.DateField()
    Type = models.CharField(max_length=1, choices=WATCHBILL_TYPE_CHOICES)
    
class Watch(models.Model):
    WatchBill = models.ForeignKey(WatchBill)
    Mid = models.ForeignKey(Mid)
    Post = models.CharField(max_length=20)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Type = models.CharField(max_length=4,choices=WATCH_TYPE_CHOICES)
