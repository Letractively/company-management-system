#specialrequestchit models.py
# Author: Michael Harrison
# Editor: Michael Laws


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
                   ('CC','Company Commander'),
                   ('PL','Platoon Commander'),
                   ('SL','Squad Leader')
                   )
class SpecialRequestChit(models.Model):
    mid = models.ForeignKey("mid.Mid")
    date = models.DateField()
    #This is the level to which the chit must be approved.  
    toLine = models.CharField(max_length=4, choices=CHIT_REQUEST_LEVEL)
    fromLine = models.CharField(max_length=50)
    viaLine = models.CharField(max_length=50)
    requestType = models.CharField(max_length=1, choices=REQUEST_TYPES)
    otherRequestType = models.CharField(max_length=30)
    justification = models.TextField()
    squadLeaderApproval = models.NullBooleanField()
    platoonLeaderApproval = models.NullBooleanField()
    companyCommanderApproval = models.NullBooleanField()
    companySELApproval = models.NullBooleanField()
    companyOfficer = models.NullBooleanField()
    #the approvalLevel is an int which should be set at run time after checking
    #the toLine for the level to which the chit needs to go.s
    approvalLevel = models.IntegerField()
    approvalStatus = models.IntegerField()
    
    def __unicode__(self):
        return self.RequestType + " - " + self.Date
