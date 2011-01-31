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
    def __unicode__(self):
        return self.Report_Date
    
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
    Description = models.CharField(max_length=20)
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
    
#FOR YOUR WEEKENDS LIST GO TO THE WEEKENDS APPLICATION

#FOR YOUR CHITS GO TO YOUR MED_CHIT APPLICATION

class Candidates(models.Model):
    Name = models.CharField(max_length=30)
    Host = models.ForeignKey("MID.Mid")
    Source = models.CharField(max_length=40)
    Admin_Note = models.CharField(max_length=90)
    
class Disipline(models.Model):
    Mid = models.ForeignKey("MID.Mid")
    Conduct_Honor = models.BooleanField()
    Date_Offence = models.DateField()
    Restriction_Days_Awarded = models.IntegerField()
    Restriction_Days_Remaining = models.IntegerField()
    Tours_Awarded = models.IntegerField()
    Tours_Remaining = models.IntegerField()
    Admin_Notes = models.CharField(max_length=90)
    Checked = models.DateField()
    
class Separations(models.Model):
    Zero8 = models.ForeignKey(Zero8)
    Mid = models.ForeignKey("MID.Mid")
    Pending = models.BooleanField()
    Admin_Note = models.CharField(max_length=90)
    
class Inspections(models.Model):
    Zero8 = models.ForeignKey(Zero8)
    TYPE_CHOICES=(
                  ('W','WATCH SECTION'),
                  ('R','ROOM'),
                  ('B','BED'),
                  ('S','STUDY HOUR'),
                  ('C','RESTRICTEE'),
                  ('A','BAC'),
                  )
    Type = models.CharField(max_length=1,choices=TYPE_CHOICES)
    Inspector = models.ForeignKey("MID.Mid", related_name='+')
    Inspectee = models.ForeignKey("MID.Mid", related_name='+')
    Time = models.TimeField()
    Score_Earned = models.IntegerField()
    Score_Possible = models.IntegerField()
    SAT = models.BooleanField()
    
class Other_Material_Discrepancies(models.Model):
    Zero8 = models.ForeignKey(Zero8)
    Location = models.CharField(max_length=50)
    Issue = models.TextField()
    Admin_Note = models.CharField(max_length=90)
    
COMPANIES=(
               ('01','1st Company'),
               ('02','2nd Company'),
               ('03','3rd Company'),
               ('04','4th Company'),
               ('05','5th Company'),
               ('06','6th Company'),
               ('07','7th Company'),
               ('08','8th Company'),
               ('09','9th Company'),
               ('10','10th Company'),
               ('11','11th Company'),
               ('12','12th Company'),
               ('13','13th Company'),
               ('14','14th Company'),
               ('15','15th Company'),
               ('16','16th Company'),
               ('17','17th Company'),
               ('18','18th Company'),
               ('19','19th Company'),
               ('20','20th Company'),
               ('21','21st Company'),
               ('22','22nd Company'),
               ('23','23rd Company'),
               ('24','24th Company'),
               ('25','25th Company'),
               ('26','26th Company'),
               ('27','27th Company'),
               ('28','28th Company'),
               ('29','29th Company'),
               ('30','30th Company'),
               ('31','31st Company'),
               ('32','32nd Company'),
               ('33','33st Company'),
               ('34','34th Company'),
               ('35','35th Company'),
               ('36','36th Company'),
               )    
    
class Inturmural_Results(models.Model):
    Zero8 = models.ForeignKey(Zero8)
    Sport = models.CharField(max_length=30)
    Oponant = models.CharField(max_length=2,choices=COMPANIES)
    WIN = models.BooleanField()
    Score_US = models.IntegerField()
    Score_THEM = models.IntegerField()
    Admin_Note = models.CharField(max_length=90)
    
class Next_Day_Event(models.Model):
    Event = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    DateTime = models.DateTimeField()
    POC = models.CharField(max_length=50)
    Admin_Note = models.CharField(max_length=90)
