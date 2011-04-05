#mid models.py
# Author: Michael Harrison
# Editor: Michael Laws


from django.db import models

RANK_CHOICES = (
                ('1','1/C'),
                ('2','2/C'),
                ('3','3/C'),
                ('4','4/C'),
                )
BILLET_CHOICES = (
    ('CC','Company Commander'),
    ('XO','Executive Officer'),
    ('HA','Honor Advisor'),
    ('OPS','Operations Officer'),
    ('ADJ','Adjutant'),
    ('PMO','Physical Mission Officer'),
    ('AC','Academics Officer'),
    ('SAF','Safety Officer'),
    ('APT','Aptitiude/Conduct Officer'),
    ('ADEO','ADEO'),
    ('ATFP','ATFP'),
    ('TRN','Training Officer'),
    ('FLT','1st LT'),
    ('ADM','Administrative Officer'),
    ('PRO','Protocol Officer'),
    ('WRD','Wardroom'),
    ('DRL','Drill Officer'),
    ('SAVI','SAVI'),
    ('CMEO','CMEO'),
    ('FIN','Financial Officer'),
    ('FSGT','1st Sergeant'),
    ('TRNS1','Training Sgt'),
    ('TRNS2','Training Sgt'),
    ('DRLS','Drill Sgt'),
    ('ADMC','Admin Chief'),
    ('MISLO','MISLO'),
    ('PC','Platoon CDR'),
    ('SL','Squad Leader'),
    ('PLTS','Platoon Sgt'),
    ('OOC','Out of Company'),
    ('MIR','Midshipman in Ranks'),
    )
CO_CHOICES = (
              ('1','1st Company'),
              ('2','2nd Company'),
              ('3','3rd Company'),
              ('4','4th Company'),
              ('5','5th Company'),
              ('6','6th Company'),
              ('7','7th Company'),
              ('8','8th Company'),
              ('9','9th Company'),
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
              ('-1','No Company'),            
              )
PLT_CHOICES = (
    ('1','1st Platoon'),
    ('2','2nd Platoon'),
    ('3','3rd Platoon'),
    ('4','4th Platoon'),
    ('O','Out of Company'),
    ('S','Company Staff'),
    )
SQD_CHOICES = (
    ('1','1st Squad'),
    ('2','2nd Squad'),
    ('3','3rd Squad'),
    ('O','Out of Company'),
    ('S','Company Staff'),
    )
DS_CHOICES = (
    ('1','Duty Section 1'),
    ('2','Duty Seciton 2'),
    ('3','Duty Section 3'),
    ('4','Duty Section 4'),
    ('5','Duty Section 5'),
    ('6','Duty Section 6'),
    ('7','Duty Section 7'),
    ('8','Duty Section 8'),
    ('O','Out of Company'),              
              )
class Room(models.Model):
    roomNumber = models.CharField(max_length=4,primary_key=True)
    maxOccupants = models.CharField(max_length=1)
    company = models.CharField(max_length=2, choices=CO_CHOICES)
    def __unicode__(self):
        return u'%s' % (self.roomNumber)
    
class Mid(models.Model):
    alpha = models.CharField(max_length=6,primary_key=True)
    LName = models.CharField(max_length=30)
    mName = models.CharField(max_length=3, null=True, blank=True)
    fName = models.CharField(max_length=30)
    rank = models.CharField(max_length=1,choices=RANK_CHOICES,null=True, blank=True)
    company = models.CharField(max_length=2, choices=CO_CHOICES)
    platoon = models.CharField(max_length=1, choices=PLT_CHOICES,null=True, blank=True)
    squad = models.CharField(max_length=1, choices=SQD_CHOICES,null=True, blank=True)
    dutySection = models.CharField(max_length=1, choices=DS_CHOICES, null=True, blank=True)
    roomNumber = models.ForeignKey(Room,null=True,blank=True)
    phoneNumber = models.CharField(max_length=10,null=True,blank=True)
    weekends = models.IntegerField(null=True,blank=True)
    weekendsComment = models.CharField(max_length=300, null=True,blank=True)
    acSAT = models.NullBooleanField(null=True,blank=True)
    PRTSat = models.NullBooleanField(null=True,blank=True)
    CQPR = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    SQPR = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    performanceGrade = models.CharField(max_length=1,null=True,blank=True)
    conductGrade = models.CharField(max_length=1,null=True,blank=True)
    PRT = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    def __unicode__(self):
        return u'%s - %s, %s %s' % (self.alpha,self.LName,self.fName,self.mName)
        
class Grade(models.Model):
    mid = models.ForeignKey(Mid)
    className = models.CharField(max_length=50)
    courseCode = models.CharField(max_length=5,null=True,blank=True)
    courseSection = models.CharField(max_length=4,null=True,blank=True)
    courseHours = models.IntegerField(max_length=1)
    grade6 = models.CharField(max_length=1,null=True,blank=True)
    grade12 = models.CharField(max_length=1,null=True,blank=True)
    grade16 = models.CharField(max_length=1,null=True,blank=True)
    gradeFinal = models.CharField(max_length=1,null=True,blank=True)
    SEMESTER_CHOICES = (
                        ('S','Spring'),
                        ('F','Fall')
                        )
    classSemester = models.CharField(max_length=1,choices=SEMESTER_CHOICES)
    classYear = models.IntegerField(max_length=4)
    
class Billet(models.Model):
    mid = models.ForeignKey(Mid)
    billet = models.CharField(max_length=5,choices=BILLET_CHOICES)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True,blank=True)
    evaluation = models.TextField(null=True,blank=True)
    current = models.NullBooleanField()
    def __unicode__(self):
        return u'%s' % (self.billet)

class PRT(models.Model):
    mid = models.ForeignKey(Mid)
    date = models.DateField()
    pushUps = models.IntegerField(null=True,blank=True)
    sitUps = models.IntegerField(null=True,blank=True)
    runTime = models.TimeField(null=True,blank=True)
    score = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)