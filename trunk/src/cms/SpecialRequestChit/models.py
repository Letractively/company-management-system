from django.db import models

# Create your models here.

class SpecialRequestChit(models.Model):
    mid = models.ForeignKey(Mid)
    Date = models.DateField()
    toLine = models.CharField(max_length=4, choices=CHIT_REQUEST_LEVEL)
    fromLine = models.CharField(max_length=50)
    viaLine = models.CharField(max_length=50)
    RequestType = models.CharField(max_length=1, choices=REQUEST_TYPES)
    otherRequestType = models.CharField(max_length=30)
    Justification = models.TextField()
