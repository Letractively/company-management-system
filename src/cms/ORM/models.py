from django.db import models

# Create your models here.

class OrmChit(models.Model):
    Mid = models.ForeignKey("MID.Mid")
    DateTime = models.DateTimeField()
    L_Street1 = models.CharField(max_length=20)
    L_Street2 = models.CharField(max_length=20)
    L_City = models.CharField(max_length=30)
    L_State = models.CharField(max_length=2)
    l_Zip = models.CharField(max_length=5)
    Prim_Phone = models.CharField(max_length=10)
    Alt_Phone = models.CharField(max_length=10)
    DateDepart = models.DateField()
    DateReturn = models.DateField()
    Days_Travel = models.IntegerField()
    Days_Leave = models.IntegerField()
    Travel_Ratio = models.IntegerField()
    def __unicode__(self):
        return self.DateTime
    
class LeisureActivites(models.Model):
    ORM_CHIT = models.ForeignKey(OrmChit)
    Activity = models.CharField(max_length=20)
    Duration = models.TimeField()
    RAC = models.IntegerField()
    def __unicode__(self):
        return self.Activity
    
class MethodsOfTravel(models.Model):
    ORM_CHIT = models.ForeignKey(OrmChit)
    EstimatedDepartTime = models.DateTimeField()
    EstimatedArrivalTime = models.DateTimeField()
    Method_of_Travel = models.CharField(max_length=20)
    RAC = models.IntegerField()
    Risk_management_plan = models.TextField()
    def __unicode__(self):
        return self.Method_of_Travel