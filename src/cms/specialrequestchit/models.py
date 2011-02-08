from django.db import models

# Create your models here.
REQUEST_TYPES = (
                 ('W','Weekend Liberty'),
                 ('D','Dining Out'),
                 ('L','Leave'),
                 ('O','Other'),
                 )
CHIT_REQUEST_LEVEL = (
                   ('SUPE','VADM M.H. Miller, USN'),
                   ('DANT','CAPT R.E. Clark II, USN'),
                   ('DDNT','CAPT B.P. O Donnell, USN'),
                   ('BATO','CAPT A. Jerrett, USN'),
                   ('CO','LT K. Igawa, USN'),
                   ('CSEL','AECS Morring, USN'),
                   )
class SpecialRequestChit(models.Model):
    mid = models.ForeignKey("MID.Mid")
    date = models.DateField()
    toLine = models.CharField(max_length=4, choices=CHIT_REQUEST_LEVEL)
    fromLine = models.CharField(max_length=50)
    viaLine = models.CharField(max_length=50)
    requestType = models.CharField(max_length=1, choices=REQUEST_TYPES)
    otherRequestType = models.CharField(max_length=30)
    justification = models.TextField()
    def __unicode__(self):
        return self.RequestType + " - " + self.Date
