from django.db import models

# Create your models here.

class OrmChit(models.Model):
    mid = models.ForeignKey("mid.Mid")
    dateTime = models.DateTimeField()
    LStreet1 = models.CharField(max_length=20)
    LStreet2 = models.CharField(max_length=20)
    LCity = models.CharField(max_length=30)
    LState = models.CharField(max_length=2)
    lZip = models.CharField(max_length=5)
    primaryPhone = models.CharField(max_length=10)
    altPhone = models.CharField(max_length=10)
    dateDepart = models.DateField()
    dateReturn = models.DateField()
    daysTravel = models.IntegerField()
    daysLeave = models.IntegerField()
    travelRatio = models.IntegerField()
    def __unicode__(self):
        return self.DateTime
    
class LeisureActivites(models.Model):
    OrmChit = models.ForeignKey(OrmChit)
    activity = models.CharField(max_length=20)
    duration = models.TimeField()
    RAC = models.IntegerField()
    def __unicode__(self):
        return self.Activity
    
class MethodsOfTravel(models.Model):
    OrmChit = models.ForeignKey(OrmChit)
    estimatedDepartTime = models.DateTimeField()
    estimatedArrivalTime = models.DateTimeField()
    methodOfTravel = models.CharField(max_length=20)
    RAC = models.IntegerField()
    RiskManagementPlan = models.TextField()
    def __unicode__(self):
        return self.Method_of_Travel