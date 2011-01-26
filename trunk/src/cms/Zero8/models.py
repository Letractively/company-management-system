from django.db import models

# Create your models here.

class Zero8(models.Model):
    Offgoing_CDO = models.ForeignKey("MID.Mid", related_name='+')
    Oncoming_CDO = models.ForeignKey("MID.Mid", related_name='+')
    Report_Date = models.DateField()
    FORCE_PROTECTION_CHOICES = (
                                ('A','Alpha'),
                                ('B','Bravo'),
                                ('C','Charlie'),
                                ('D','Delta'),                                
                                )
    Force_Protection_Condition = models.CharField(max_length=1, choices=FORCE_PROTECTION_CHOICES)
    Work_Order_Active = models.IntegerField()
    Work_Order_Closed = models.IntegerField()
    Work_Order_Overdue = models.IntegerField()
    
class SIG_EVENTS(models.Model):
    Zero8 = models.ForeignKey(Zero8)
    SECTION_CHOICES=(
                     ('A','Family Crisis/Hospitalization/Death Notifications'),
                     ('B','Major Conduct Offenses that occured this date'),
                     ('C','Bancroft Hall Thefts'),
                     )
    Section = models.CharField(max_length=1, choices=SECTION_CHOICES)
    Name = models.ForeignKey("MID.Mid")
    Description = models.CharField(max_length=30)
    Admin_Note = models.CharField(max_length=90)
    
class Absencs(models.Model):
    Zero8 = models.ForeignKey(Zero8)
    Name = models.ForeignKey("MID.Mid")
    Authorized = models.BooleanField()
    Description = models.CharField(max_ength=20)
    Admin_Note = models.CharField(max_length=90)
    REASON_CHOICES = (
                     ('AA','Authorized Absence'),
                     ('UA','Unauthorized Absence'),
                     ('WE','Weekend'),
                     ('MO','Movement Order'),
                     )
    Reason = models.CharField(max_length=2,choices=REASON_CHOICES)
    
class MO(models.Model):
    Zero8 = models.ForeignKey(Zero8)
    Organization = models.CharField(max_length=30)
    MO_Code = models.ForeignKey("MID.Mid")
    Depart = models.DateField()
    Return = models.DateField()
    Admin_Note = models.CharField(max_length=90)
    

    
