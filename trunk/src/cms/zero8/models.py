#zero8 models.py
# Author: Michael Harrison
# Editor: Michael Laws


from django.db import models

# Create your models here.

class Zero8(models.Model):
    offgoingCDO = models.ForeignKey("mid.mid", related_name='+')
    oncomingCDO = models.ForeignKey("mid.mid", related_name='+')
    reportDate = models.DateField()
    FORCE_PROTECTION_CHOICES = (
                                ('A','Alpha'),
                                ('B','Bravo'),
                                ('C','Charlie'),
                                ('D','Delta'),                                
                                )
    forceProtectionCondition = models.CharField(max_length=1, choices=FORCE_PROTECTION_CHOICES)
    workOrderActive = models.IntegerField()
    workOrderClosed = models.IntegerField()
    workOrderOverdue = models.IntegerField()
    def __unicode__(self):
        return unicode(self.reportDate) + " - " + self.offgoingCDO.LName
    
class SignificantEvents(models.Model):
    zero8 = models.ForeignKey(Zero8)
    SECTION_CHOICES=(
                     ('A','Family Crisis/Hospitalization/Death Notifications'),
                     ('B','Major Conduct Offenses that occured this date'),
                     ('C','Bancroft Hall Thefts'),
                     )
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)
    name = models.ForeignKey("mid.Mid")
    description = models.CharField(max_length=60)
    adminNote = models.CharField(max_length=300)
    
#FOR YOUR WEEKENDS LIST GO TO THE WEEKENDS APPLICATION

#FOR YOUR CHITS GO TO YOUR MED_CHIT APPLICATION

class Candidates(models.Model):
    name = models.CharField(max_length=30)
    host = models.ForeignKey("mid.Mid")
    source = models.CharField(max_length=40)
    adminNote = models.CharField(max_length=90)
    arriveDate = models.DateField()
    departDate = models.DateField()
    
class Inspections(models.Model):
    zero8 = models.ForeignKey(Zero8)
    TYPE_CHOICES=(
                  ('W','WATCH SECTION'),
                  ('R','ROOM'),
                  ('B','BED'),
                  ('S','STUDY HOUR'),
                  ('C','RESTRICTEE'),
                  ('A','BAC'),
                  )
    type = models.CharField(max_length=1,choices=TYPE_CHOICES)
    inspector = models.ForeignKey("mid.Mid", related_name='+')
    inspectee = models.ForeignKey("mid.Mid", related_name='+', null = True, blank = True)
    room = models.ForeignKey('mid.Room',null=True,blank=True)
    time = models.TimeField()
    scoreEarned = models.IntegerField(null=True,blank=True)
    scorePossible = models.IntegerField(null=True,blank=True)
    SAT = models.BooleanField()
    comment = models.CharField(max_length=100, null=True,blank=True)
    
class OtherMaterialDiscrepancies(models.Model):
    zero8 = models.ForeignKey(Zero8)
    location = models.CharField(max_length=50)
    issue = models.TextField()
    adminNote = models.CharField(max_length=90)
    
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
    
class InturmuralResults(models.Model):
    zero8 = models.ForeignKey(Zero8)
    sport = models.CharField(max_length=30)
    oponant = models.CharField(max_length=2,choices=COMPANIES)
    Win = models.BooleanField()
    scoreUs = models.IntegerField()
    scoreThem = models.IntegerField()
    adminNote = models.CharField(max_length=90)
    
class NextDayEvents(models.Model):
    event = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    dateTime = models.DateTimeField()
    POC = models.CharField(max_length=50)
    adminNote = models.CharField(max_length=90)
