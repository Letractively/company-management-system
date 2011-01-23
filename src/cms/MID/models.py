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
    )
SQD_CHOICES = (
    ('1','1st Squad'),
    ('2','2nd Squad'),
    ('3','3rd Squad'),
    )

class Mid(models.Model):
    Alpha = models.CharField(max_length=6,primary_key=True)
    L_Name = models.CharField(max_length=30)
    MI_Name = models.CharField(max_length=3)
    F_Name = models.CharField(max_length=30)
    PLT = models.CharField(max_length=1, choices=PLT_CHOICES)
    SQD = models.CharField(max_length=1, choices=SQD_CHOICES)
    #Billets = models.CharField(max_length=4, choices=BILLET_CHOICES) //this needs to be its own class because of inharitance
    RoomNumber = models.ForeignKey(Room)
    PhoneNumber = models.CharField(max_length=10)
    Weekends = models.IntegerField()
    AcSAT = models.BooleanField().default=True
    PRTSAT = models.BooleanField().default=True
    CQPR = models.DecimalField(max_digits=4, decimal_places=2)
    SQPR = models.DecimalField(max_digits=4, decimal_places=2)
    PerfGrade = models.CharField(max_length=1)
    ConductGrade = models.CharField(max_length=1)
    PRT = models.IntegerField(max_length=3)
    
class Billets(models.Model):
    mid = models.ForeignKey(Mid)
    Billet = models.CharField(max_length=4,choices=BILLET_CHOICES)
    startDate = models.DateField()
    endDate = models.DateField()
    Evaluation = models.TextField()
    Current = models.BooleanField()
