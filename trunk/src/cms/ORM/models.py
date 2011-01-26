from django.db import models

# Create your models here.

class ORM_Chit(models.Model):
    mid = models.ForeignKey("MID.Mid")
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
    
class Leisure_Activites(models.Model):
    ORM_CHIT = models.ForeignKey(ORM_Chit)
    Activity = models.CharField(max_length=20)
    Duration = models.TimeField()
    RAC = models.IntegerField()
    
class Methods_of_Travel(models.Model):
    ORM_CHIT = models.ForeignKey(ORM_Chit)
    EstimatedDepartTime = models.DateTimeField()
    EstimatedArrivalTime = models.DateTimeField()
    Method_of_Travel = models.CharField(max_length=20)
    RAC = models.IntegerField()
    Risk_management_plan = models.TextField()
 