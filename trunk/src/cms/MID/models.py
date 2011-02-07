from django.db import models

# Create your models here.
BILLET_CHOICES = (
    ('CC','Company Commander'),
    ('XO','Executive Officer'),
    ('HA','Honor Advisor'),
    ('OPS','Operations Officer'),
    ('ADJ','Adjutant'),
    ('PMO','Physical Mission Officer'),
    ('AC','Academics Officer'),
    ('SAF','Safety Officer'),
    ('A/C','Aptitiude/Conduct Officer'),
    ('ADEO','ADEO'),
    ('ATFP','ATFP'),
    ('TRN','Training Officer'),
    ('1LT','1st LT'),
    ('ADM','Administrative Officer'),
    ('PRO','Protocol Officer'),
    ('WRD','Wardroom'),
    ('DRL','Drill Officer'),
    ('SAVI','SAVI'),
    ('CMEO','CMEO'),
    ('FIN','Financial Officer'),
    ('1SGT','1st Sergeant'),
    ('TRNS','Training Sgt'),
    ('DRLS','Drill Sgt'),
    ('ADMC','Admin Chief'),
    ('MISLO','MISLO'),
    ('PC','Platoon CDR'),
    ('SL','Squad Leader'),
    ('PLTS','Platoon Sgt'),
    ('OOC','Out of Company'),
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
class Room(models.Model):
    RoomNumber = models.CharField(max_length=4,primary_key=True)
    maxOccupants = models.CharField(max_length=1)
    def __unicode__(self):
        return self.RoomNumber
    
class Mid(models.Model):
    Alpha = models.CharField(max_length=6,primary_key=True)
    L_Name = models.CharField(max_length=30)
    MI_Name = models.CharField(max_length=3)
    F_Name = models.CharField(max_length=30)
    PLT = models.CharField(max_length=1, choices=PLT_CHOICES,null=True)
    SQD = models.CharField(max_length=1, choices=SQD_CHOICES,null=True)
    #Billets = models.CharField(max_length=4, choices=BILLET_CHOICES) //this needs to be its own class because of inharitance
    RoomNumber = models.ForeignKey(Room,null=True)
    PhoneNumber = models.CharField(max_length=10,null=True)
    Weekends = models.IntegerField(null=True)
    AcSAT = models.BooleanField(null=True).default=True
    PRTSAT = models.BooleanField(null=True).default=True
    CQPR = models.DecimalField(max_digits=4, decimal_places=2,null=True)
    SQPR = models.DecimalField(max_digits=4, decimal_places=2,null=True)
    PerfGrade = models.CharField(max_length=1,null=True)
    ConductGrade = models.CharField(max_length=1,null=True)
    PRT = models.DecimalField(max_digits=3, decimal_places=2,null=True)
    def __unicode__(self):
        return self.L_Name + ", " + self.F_Name + " " + self.MI_Name + " - " + self.Alpha
    
class Billets(models.Model):
    mid = models.ForeignKey(Mid)
    Billet = models.CharField(max_length=4,choices=BILLET_CHOICES)
    startDate = models.DateField(null=True)
    endDate = models.DateField(null=True)
    Evaluation = models.TextField(null=True)
    Current = models.NullBooleanField()
    def __unicode__(self):
        return self.Billet
