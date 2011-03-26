#orm models.py
# Author: Michael Harrison
# Editor: Michael Laws

from django.db import models

# Create your models here.

class OrmChit(models.Model):
    mid = models.ForeignKey("mid.Mid")
    date = models.DateField()
    street1 = models.CharField(max_length=20)
    street2 = models.CharField(max_length=20)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    altPhone = models.CharField(max_length=10)
    dateDepart = models.DateField()
    dateReturn = models.DateField()
    daysTravel = models.IntegerField()
    daysLeave = models.IntegerField()
    travelRatio = models.IntegerField()
    riskMitigationPlan = models.TextField()
    
    #the approvalLevel is an int which should be set at run time after checking
    #the toLine for the level to which the chit needs to go.s
    approvalLevel = models.IntegerField()
    approvalStatus = models.IntegerField()
    safetyOfficerApproval = models.NullBooleanField()
    companyOfficerApproval = models.NullBooleanField()
    platoonCommander = models.NullBooleanField()
    squadLeader = models.NullBooleanField()
    def __unicode__(self):
        return unicode(self.reportDate) + " - " + self.mid.LName
    
    
class LeisureActivites(models.Model):
    OrmChit = models.ForeignKey(OrmChit)
    activity = models.CharField(max_length=20)
    duration = models.TimeField()
    RAC = models.IntegerField()
    def __unicode__(self):
        return self.activity
    
class MethodsOfTravel(models.Model):
    OrmChit = models.ForeignKey(OrmChit)
    estimatedDepartTime = models.DateTimeField()
    estimatedArrivalTime = models.DateTimeField()
    methodOfTravel = models.CharField(max_length=20)
    RAC = models.IntegerField()
    RiskManagementPlan = models.TextField()
    def __unicode__(self):
        return self.methodOfTravel